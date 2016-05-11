import glob, os, fnmatch, re, json, copy, shutil
import xml.etree.ElementTree
from optparse import OptionParser

parser = OptionParser()

#command line options
parser.add_option("-d", "--dal-headers",
                  action="store",
	              type="string",
                  dest="dal_headers",
                  default="",
                  help="The relative path to the headers for the microbit-dal.")

parser.add_option("-m", "--microbit-headers",
                  action="store",
	              type="string",
                  dest="microbit_headers",
                  default="",
                  help="The relative path to the headers for MicroBit (MicroBit.h), if not supplied, this will use the same location as specified by -d.")

parser.add_option("--no-clean",
                  action="store_true",
                  dest="no_clean",
                  help="If set, doxygen documentation will not be regenerated.")

parser.add_option("--no-filter",
                  action="store_true",
                  dest="no_filter",
                  help="If set, filters for member functions and header copying will not be applied")

parser.add_option("-g","--github-deploy",
                  action="store_true",
                  dest="github_deploy",
                  help="If set, filters for member functions and header copying will not be applied")

(options, args) = parser.parse_args()

if options.github_deploy:
    if options.dal_headers or options.microbit_headers:
        print "The -g flag only deploys, no documentation will be generated."

    os.system('mkdocs gh-deploy --clean')
    exit(0)


if not options.dal_headers:
    parser.error('A path was not given to the microbit-dal')

if not options.microbit_headers:
    options.microbit_headers = options.dal_headers

type_colour = "#a71d5d"
function_name_colour = "#795da3"

separate_defaults = True
display_defaults = False

filters = True

if options.no_filter:
    filters = False

generate_doxygen = True

if options.no_clean:
    generate_doxygen = False

member_func_filter = ["idleTick", "systemTick", "~"]
folder_filter = ["ble", "ble-nrf51822", "mbed-classic","nrf51-sdk"]

md_special_chars =[
    {
        "md_char": "*",
        "replacement": "&#42;"
    },
    {
        "md_char": "#",
        "replacement": "&#35;"
    },
    {
        "md_char": "`",
        "replacement": "&#183;"
    }
]

#http://stackoverflow.com/questions/2186525/use-a-glob-to-find-files-recursively-in-python
def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        if filters and any(dir in root for dir in folder_filter):
            continue

        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename

###
# removes files from a folder.
###
def clean_dir(dir):
    for root, dirs, files in os.walk(dir):
        for f in files:
            print "removing " + f
            os.remove(os.path.join(root, f))
        for d in dirs:
            print "removing " + d
            shutil.rmtree(os.path.join(root, d))

###
# this files from one location to another
###
def copy_files(from_dir, to_dir, pattern):
    files = find_files(from_dir, pattern)

    for file in files:
        shutil.copy(file,to_dir)

###
# this function copies headers recursively from a source director to a destination
# directory.
###
def get_headers(from_dir, to_dir):
    copy_files(from_dir, to_dir, "*.h")


###
# this function extracts data from an element tag ignoring the tag 'ref', but
# obtains the textual data it has inside the ref tag.
#
# @param element the element to process
#
# @return a list of extracted strings.
###
def extract_ignoring_refs(element):
    list = []

    if element.text is not None:
        list.append(element.text)

    for ref in element.iter(tag="ref"):
        list.append(ref.text)

    return list

###
# this function extracts data from an element tag including all sub elements
# (recursive)
#
# @param element the element to process
#
# @return a list of extracted strings.
###
def extract_with_subelements(element):
    list = []

    list.append(element.text or "")

    #if element.text is not None:
        #list.append(element.text)

    for subelement in element:
        if subelement is not None:
            list = list + extract_with_subelements(subelement)

    list.append(element.tail or "")

    return list

###
# this function was at one point intended to fetch a value of a default parameter
# it is now only used to fetch the default parameters' name.
#
# @param document_root the root of the entire document
# @param element the element containing the default parameter
#
# @return a dictionary containing:
# {
#     'name':'',
#     'value':''
# }
###
def extract_default(document_root, element):
    ref = element.find("ref")

    return_object = {'name':'', 'value':''}

    #check there is a ref tag in the given element
    if ref is None:
        return_object['name'] = ' '.join(element.itertext())
        return return_object

    #obtain the reference id attribute
    refid = ref.attrib['refid']

    file_ref = ""

    #find all elements matching the refid
    #(THERE CAN BE ONLY ONE)
    if len(document_root.findall("references[@refid='"+refid+"']")) is not 0:
        file_ref = document_root.findall("references[@refid='"+refid+"']")[0].attrib['compoundref']

    #if we find which file defines the default, extract, otherwise return
    if file_ref is "":
        return_object['name'] = ' '.join(element.itertext())
        return return_object

    #open the referenced file
    refed_file = xml.etree.ElementTree.parse("./xml/" + file_ref + ".xml").getroot()

    return_object['name'] = element.itertext()

    #attempt to find the value
    if len(refed_file.findall("*[@id='"+refid+"']")) is not 0:
        return_object['value'] = refed_file.findall("[@id='"+refid+"']")[0].text

    return return_object

###
# Strips out reserved characters used in markdown notation, and replaces them
# with html character codes.
#
# @param text the text to strip and replace the md special characters
#
# @return the stripped text.
###
def escape_md_chars(text):
    for char in md_special_chars:
        text = text.replace(char['md_char'], "\\" + char['md_char'])
    return text

###
# extracts a member function form the xml document
#
# @param root the document root
# @param xml_element the member function xml element.
#
# @return a function dictionary:
# {
#     'short_name':"",
#     'name':"",
#     'return_type':"",
#     'params':[],
#     'description':[],
#     'returns':"",
#     'notes':"",
#     'examples':""
# }
###
def extract_member_function(root, xml_element):

    function = {
        'short_name':"",
        'name':"",
        'return_type':"",
        'params':[],
        'description':[],
        'returns':"",
        'notes':"",
        'examples':"",
        'simulator':""
    }

    function['name'] = xml_element.find('definition').text
    function['short_name'] = xml_element.find('name').text

    if filters and any(filtered_func in function['short_name'] for filtered_func in member_func_filter):
        print "Filtered out: " + function['short_name']
        return

    print "Generating documentation for: " + function['short_name']

    if xml_element.find('type') is not None:
        function['return_type'] = escape_md_chars(' '.join(extract_ignoring_refs(xml_element.find('type'))))

    #extract our parameters for this member function
    for parameter in xml_element.iter('param'):

        type = ""
        name = ""

        if parameter.find('type') is not None:
            type = escape_md_chars(' '.join(parameter.find('type').itertext()))

        if parameter.find('declname') is not None:
            name = ' '.join(extract_ignoring_refs(parameter.find('declname')))

        param_object = {
            'type': type,
            'name': name,
            'default':{
                'name':"",
                'value':""
            }
        }

        if parameter.find('defval') is not None:
            extracted = extract_default(root, parameter.find('defval'))
            param_object['default']['name'] = extracted['name']
            param_object['default']['value'] = extracted['value']

        function['params'].append(param_object)


    detailed_description = xml_element.find('detaileddescription')

    if len(detailed_description.findall("para")) is not 0:
        for para in detailed_description.findall("para"):
            if len(para.findall("programlisting")) is 0 and len(para.findall("simplesect")) is 0 and len(para.findall("simulator")) is 0:
                function['description'] = function['description'] + extract_with_subelements(para)

            #para indicates a new paragraph - we should treat it as such... append \n!
            function['description'] = function['description'] + ["\n\n"]

    if len(detailed_description.findall("para/simplesect[@kind='return']/para")) is not 0:
         return_section = detailed_description.findall("para/simplesect[@kind='return']/para")[0]
         function['returns'] = ' '.join(return_section.itertext())

    if len(detailed_description.findall("para/simplesect[@kind='note']/para")) is not 0:
         return_section = detailed_description.findall("para/simplesect[@kind='note']/para")[0]
         function['notes'] =  ' '.join(return_section.itertext())

    examples = detailed_description.find('para/programlisting')
    simulator = detailed_description.find('para/simulator')

    if simulator is not None:
        function['simulator'] = simulator.text

    if examples is not None:
         function['examples'] = ''.join([('' if index is 0 else ' ')+word for index, word in enumerate(examples.itertext(),1) ])

    param_list = detailed_description.findall('para/parameterlist')

    if len(param_list) is not 0:
        for parameter_desc in param_list[0].findall('parameteritem'):

             param_descriptor = {
                 'name':'',
                 'description':''
             }

             param_name = parameter_desc.findall('parameternamelist/parametername')
             additional = parameter_desc.findall('parameterdescription/para')

             if len(param_name) is not 0:
                 param_descriptor['name'] = param_name[0].text

             if len(additional) is not 0:
                 param_descriptor['description'] = ' '.join(additional[0].itertext())

             for descriptor in function['params']:
                 if param_descriptor['name'] in descriptor['name']:
                     descriptor['description'] = param_descriptor['description']

    return function

###
# removes previously generated markdown from the file.
#
# @param file_lines a list of lines representing a file.
# @param regexp the regular expression that dictates a match.
###
def clean(file_lines, regexp):
    start = 0
    end = 0

    for line_number, line in enumerate(file_lines, 1):
        result = re.findall(regexp,line)

        if len(result) is not 0:
            meta_data = json.loads(result[0])

            keys = meta_data.keys()

            #classname indicates the beginning of a meta_data section
            if 'className' in keys:
                start = line_number

            #end indicated the end of a meta_data section
            if 'end' in keys:
                end = line_number - 1

    return file_lines[:start] + file_lines[end:]

###
# writes a given set of lines to a path.
#
# @param path the path where the file is located
# @param lines the lines to write
###
def write(path, lines):
    print "Writing to: " + path + " \n"
    with open(path, 'w') as file:
        file.writelines(lines)

###
# reads a file and returns a list of lines
#
# @param path the path where the file is located
#
# @return the list of lines representing the file.
###
def read(path):
    print "Opening: " + path + " \n"
    with open(path, 'r') as file:
        return file.readlines()

###
# wraps text in a div element with a given color
#
# @param text the text to wrap
# @param color the desired text color
#
# @return a string representing the now wrapped text
###
def wrap_text(text, color):
    return "<div style='color:" + color + "; display:inline-block'>" + text + "</div>"

###
# given a member function, this function derives the alternative versions
#
# @param member_func the member function that is required to be derrived
#
# @return a list of function dictionaries that contain the alternatives, based on the original
###
def derive_functions(member_func):
    member_functions_derived = []

    if len(member_func['params']) is not 0:

        param_index = 0;

        for param in member_func['params']:
            if len(param['default']['name']) is 0:
                param_index = param_index + 1
            else:
                break

        bare_function = {
            'short_name' : member_func['short_name'],
            'name' : member_func['name'],
            'params' : [],
            'description' : member_func['description'],
            'returns' : member_func['returns'],
            'notes' : member_func['notes'],
            'examples' : member_func['examples'],
            'simulator' : member_func['simulator'],
            'return_type' : member_func['return_type']
        }

        for i in range(0, param_index):
            bare_function['params'] = bare_function['params'] + [member_func['params'][i]]

        member_functions_derived = member_functions_derived + [bare_function]

        current = copy.copy(bare_function)

        #lists retain references, so we have to copy objects to maintain separation
        for remainder in range(param_index, len(member_func['params'])):
            current['params'] = current['params'] + [member_func['params'][remainder]]
            member_functions_derived = member_functions_derived + [current]
            current = copy.copy(current)

    else:
        member_functions_derived = member_functions_derived + [member_func]

    return member_functions_derived

###
# given a parameter, this function generates text
#
# @param param the parameter that needs a textual translation
#
# @return a string representing the parameter
###
def gen_param_text(param):
    text = "\n> "

    if param['type'] is not None:
        text = text + " " + wrap_text(param['type'], type_colour)

    text = text + " " + param['name']

    if display_defaults:
        if len(param['default']['name']) is not 0:
            text = text + " `= " + param['default']['name']

            if len(param['default']['value']) is not 0:
                text = text + param['default']['value']

            text = text + "`"

    if 'description' in param.keys():
        text = text +" - " + param['description']

    text = text.encode('ascii','ignore')

    return text

###
# given a list of member functions, this function returns a list of new lines for the
# file currently being processed.
#
# @param class_name the name of the current class (found in the meta data)
# @param member_functions the list of member_functions extracted from XML
#
# @return a list containing the new lines to be inserted into the current file.
###
def gen_member_func_doc(class_name, member_functions):

    # this is what a member function dictionary contains.
    # function = {
    #     'short_name':"",
    #     'name':"",
    #     'return_type':"",
    #     'params':[],
    #     'description':[],
    #     'returns':"",
    #     'notes':"",
    #     'examples':"",
    #     'default':None
    # }

    lines = []

    for index, member_func in enumerate(member_functions,0):

        member_functions_derived = []

        if index is 0 or member_func['short_name'] != member_functions[index - 1]['short_name']:
            if class_name == member_func["short_name"]:
                lines.append("##Constructor\n")
            else:
                lines.append("##" + member_func["short_name"]+"\n")

        #we want to clearly separate our different level of functions in the DAL
        #so we present methods with defaults as overloads.
        if separate_defaults is True:
            member_functions_derived = member_functions_derived + derive_functions(member_func)

        for derived_func in member_functions_derived:
            #---- short name for urls ----
            lines.append("<br/>\n")

            short_name = ""

            if len(derived_func["return_type"]) is not 0:
                short_name = "####" + wrap_text(derived_func["return_type"],type_colour) + " " +wrap_text(derived_func["short_name"], function_name_colour)  + "("
            else:
                short_name = "####" + derived_func["short_name"] + "("

            last_param = None

            if len(derived_func['params']) is not 0:
                last_param = derived_func['params'][-1]

            #generate parameters for the name of this function
            for param in derived_func['params']:
                text = ""

                if param['type'] is not None:
                    text = text + " " + wrap_text(param['type'], type_colour)

                text = text + " " + param['name']

                if param is not last_param:
                    short_name = short_name + text +", "
                else:
                    short_name = short_name + text

            lines.append(short_name + ")\n")
            #-----------------------------

            #---- description ----
            if len(derived_func['description']) is not 0:
                lines.append("#####Description\n")
                lines.append(' '.join(derived_func['description']) + "\n")
            #-----------------------------

            #---- parameters ----
            if len(derived_func['params']) is not 0:
                lines.append("#####Parameters\n")

                for param in derived_func['params']:
                    lines.append(gen_param_text(param) + "\n")
            #-----------------------------

            #---- returns ----
            if len(derived_func['returns']) is not 0:
                lines.append("#####Returns\n")
                lines.append(derived_func['returns'] + "\n")
            #-----------------------------

            #---- examples ----
            if len(derived_func['examples']) is not 0:
                lines.append("#####Example\n")
                lines.append("```cpp\n")
                lines.append(derived_func['examples'])
                lines.append("```\n")
            #-----------------------------

            #---- simulator ----
            if len(derived_func['simulator']) is not 0:
                lines.append("#####Simulation\n")
                lines.append("```sim\n")
                lines.append(derived_func['simulator'])
                lines.append("```\n")
            #-----------------------------

            #---- notes ----
            if len(derived_func['notes']) is not 0:
                lines.append("\n!!! note\n")
                lines.append("    " + derived_func['notes'].replace('\n','\n    '))
                lines.append('\n\n')
            #-----------------------------

    lines.append("____\n")

    return lines

###
# the trigger for generating our documentation
###
def generate_mkdocs():
    global member_func_filter

    file_names = find_files('docs','*.md')
    section_kind = ["public-func"]
    meta_data_regex = re.compile( r'\[comment\]: <> \((.*?)\)', re.MULTILINE | re.DOTALL )

    for filename in file_names:
        print(filename)

        read_lines = read(filename)

        file_lines = clean(read_lines, meta_data_regex)

        write(filename, file_lines)

        previous = ""

        for line_number, line in enumerate(file_lines, 1):

            filter_preserved = member_func_filter

            result = re.findall(meta_data_regex,line)

            if len(result) is not 0:

                meta_data = json.loads(result[0])

                if previous is not "" and "end" in meta_data.keys() and meta_data['end'] == previous:
                    previous = ""
                    continue
                elif previous is "":
                    try:
                        previous = meta_data['className']
                    except:
                        raise Exception('There isn\'t a match for the meta_data '+ meta_data)
                else:
                    raise Exception('There isn\'t a match for the meta_data \''+ previous + "'")

                if "filter" in meta_data:
                    for member_function in meta_data["filter"]:
                        member_func_filter = member_func_filter + [ str(member_function) ]

                    print "Custom filter applied: " + str(member_func_filter)

                doxygen_class_xml = xml.etree.ElementTree.parse("./xml/class" + meta_data['className'] + ".xml").getroot()

                member_functions = []

                for section_def in doxygen_class_xml.iter('sectiondef'):
                    if section_def.attrib['kind'] in section_kind:
                        for member_func in section_def.iter('memberdef'):
                            new_member = extract_member_function(doxygen_class_xml,member_func)
                            if new_member is not None:
                                member_functions.append(new_member)

                if meta_data['className'] is "MicroBit":
                    print str(member_functions)
                    exit(1)

                before = file_lines[:line_number]
                after = file_lines[line_number:]

                between = gen_member_func_doc(meta_data['className'] ,member_functions)

                write(filename, before + between + after)

                #restore our default filter.
                member_func_filter = filter_preserved

if generate_doxygen:
    header_dest = "./inc"
    doxygen_dest = "./xml"

    if not os.path.exists(header_dest):
        os.makedirs(header_dest)

    clean_dir(header_dest)

    get_headers(options.dal_headers, header_dest)
    get_headers(options.microbit_headers, header_dest)


    if os.path.exists(doxygen_dest):
        clean_dir(doxygen_dest)

    os.system('doxygen doxy-config.cfg')

generate_mkdocs()
