import os, re, json, xml.etree.ElementTree
from optparse import OptionParser

from DocumentationGenerator.doxygen_extractor import DoxygenExtractor
from DocumentationGenerator.md_converter import MarkdownConverter
from DocumentationGenerator.system_utils import SystemUtils

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

parser.add_option("-g","--github-deploy",
                  action="store_true",
                  dest="github_deploy",
                  help="If set, filters for member functions and header copying will not be applied")

parser.add_option("--no-filter",
                  action="store_true",
                  dest="no_filter",
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

utils = SystemUtils()

header_paths = []

if options.dal_headers == options.microbit_headers:
    header_paths = header_paths + [options.dal_headers +"/microbit-dal", options.dal_headers + "/microbit"]
else:
    header_paths = header_paths + [options.dal_headers, options.microbit_headers]

doxygen = DoxygenExtractor(os.path.abspath("."), header_paths)
markdown = MarkdownConverter(type_colour, function_name_colour, separate_defaults = separate_defaults, display_defaults = display_defaults)

###
# the trigger for generating our documentation
###
def generate_mkdocs():
    global member_func_filter

    file_names = utils.find_files('docs','*.md')
    section_kind = ["public-func"]
    meta_data_regex = re.compile( r'\[comment\]: <> \((.*?)\)', re.MULTILINE | re.DOTALL )

    for filename in file_names:
        print(filename)

        read_lines = utils.read(filename)

        file_lines = markdown.clean(read_lines, meta_data_regex)

        utils.write(filename, file_lines)

        previous = ""

        for line_number, line in enumerate(file_lines, 1):

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

                local_filter = member_func_filter

                if "filter" in meta_data:
                    for member_function in meta_data["filter"]:
                        local_filter = local_filter + [ str(member_function) ]

                    print "Custom filter applied: " + str(member_func_filter)

                doxygen_class_xml = xml.etree.ElementTree.parse("./xml/class" + meta_data['className'] + ".xml").getroot()

                member_functions = []

                for section_def in doxygen_class_xml.iter('sectiondef'):
                    if section_def.attrib['kind'] in section_kind:
                        for member_func in section_def.iter('memberdef'):
                            new_member = doxygen.extract_member_function(member_func, local_filter, filter= filters)
                            if new_member is not None:
                                member_functions.append(new_member)

                before = file_lines[:line_number]
                after = file_lines[line_number:]

                between = markdown.gen_member_func_doc(meta_data['className'], member_functions)

                utils.write(filename, before + between + after)

if generate_doxygen:
    doxygen.generate_doxygen()
    utils.validate_version(doxygen.working_dir, header_paths, "./docs/archive")

generate_mkdocs()
