#ManagedString

##Overview

##Message Bus ID

##Message Bus Events

#API
[comment]: <> ({"className":"ManagedString"})
##Constructor
<br/>
####ManagedString( <div style='color:#008080; display:inline-block'>StringData  *</div> ptr)
#####Description
Constructor. Create a managed string from a specially prepared string literal. It will ptr->incr().
#####Parameters

>  <div style='color:#008080; display:inline-block'>StringData  *</div> *ptr* - The literal - first two bytes should be 0xff, then the length in little endian, then the literal. The literal has to be 4-byte aligned.
#####Example
```c++
staticconstcharhello[]__attribute__((aligned(4)))="\xff\xff\x05\x00""Hello";
ManagedStrings((StringData*)(void*)hello);

```
##leakData
<br/>
####<div style='color:#FF69B4; display:inline-block'>StringData</div> leakData()
#####Description
Get current ptr, do not decr() it, and set the current instance to empty string. This is to be used by specialized runtimes which pass  StringData
##Constructor
<br/>
####ManagedString( <div style='color:#008080; display:inline-block'>const char *</div> str)
#####Description
Constructor. Create a managed string from a pointer to an 8-bit character buffer. The buffer is copied to ensure safe memory management (the supplied character buffer may be decalred on the stack for instance).
#####Parameters

>  <div style='color:#008080; display:inline-block'>const char *</div> *str* - The character array on which to base the new  ManagedString .
#####Example
```c++
ManagedStrings("abcdefg");

```
<br/>
####ManagedString( <div style='color:#008080; display:inline-block'>const int</div> value)
#####Description
Constructor. Create a managed string from a given integer.
#####Parameters

>  <div style='color:#008080; display:inline-block'>const int</div> *value* - The integer from which to create the  ManagedString
#####Example
```c++
ManagedStrings(20);

```
<br/>
####ManagedString( <div style='color:#008080; display:inline-block'>const char</div> value)
#####Description
Constructor. Create a managed string from a given char.
#####Parameters

>  <div style='color:#008080; display:inline-block'>const char</div> *value* - The char from which to create the  ManagedString
#####Example
```c++
ManagedStrings('a');

```
<br/>
####ManagedString( <div style='color:#008080; display:inline-block'>const char *</div> str,  <div style='color:#008080; display:inline-block'>const int16_t</div> length)
#####Description
Constructor. Create a managed string from a pointer to an 8-bit character buffer of a given length. The buffer is copied to ensure sane memory management (the supplied character buffer may be declared on the stack for instance).
#####Parameters

>  <div style='color:#008080; display:inline-block'>const char *</div> *str* - The character array on which to base the new  ManagedString . 

>  <div style='color:#008080; display:inline-block'>const int16_t</div> *length* - The length of the character array
#####Example
```c++
ManagedStrings("abcdefg",7);//thisisgenerallyusedforsubstring...whynotuseanormalchar*constructor?

```
<br/>
####ManagedString( <div style='color:#008080; display:inline-block'>const  ManagedString  &</div> s)
#####Description
Copy constructor. Makes a new  ManagedString ManagedString
#####Parameters

>  <div style='color:#008080; display:inline-block'>const  ManagedString  &</div> *s* - The  ManagedString  to copy.
#####Example
```c++
ManagedStrings("abcdefg");
ManagedStringp(s);

```
<br/>
####ManagedString()
#####Description
Default constructor.
#####Example
```c++
ManagedStrings();

```
##~ManagedString
<br/>
####~ManagedString()
#####Description
Destructor.
##operator=
<br/>
####<div style='color:#FF69B4; display:inline-block'>ManagedString</div> operator=( <div style='color:#008080; display:inline-block'>const  ManagedString  &</div> s)
#####Description
Copy assign operation.
#####Parameters

>  <div style='color:#008080; display:inline-block'>const  ManagedString  &</div> *s* - The  ManagedString  to copy.
#####Example
```c++
ManagedStrings("abcd");
ManagedStringp("efgh");
p=s//pnowpointstos,s'refisincremented

```
##operator==
<br/>
####<div style='color:#FF69B4; display:inline-block'>bool</div> operator==( <div style='color:#008080; display:inline-block'>const  ManagedString  &</div> s)
#####Description
Equality operation.
#####Parameters

>  <div style='color:#008080; display:inline-block'>const  ManagedString  &</div> *s* - The  ManagedString  to test ourselves against. 
#####Returns
true if this  ManagedString  is identical to the one supplied, false otherwise.
#####Example
```c++
ManagedStrings("abcd");
ManagedStringp("efgh");

if(p==s)
print("Wearethesame!");
else
print("Wearedifferent!");//pisnotequaltos-thiswillbecalled

```
##operator<
<br/>
####<div style='color:#FF69B4; display:inline-block'>bool</div> operator<( <div style='color:#008080; display:inline-block'>const  ManagedString  &</div> s)
#####Description
Inequality operation.
#####Parameters

>  <div style='color:#008080; display:inline-block'>const  ManagedString  &</div> *s* - The  ManagedString  to test ourselves against. 
#####Returns
true if this  ManagedString  is alphabetically less than to the one supplied, false otherwise.
#####Example
```c++
ManagedStrings("a");
ManagedStringp("b");

if(s<p)
print("aisbeforeb!");//aisbeforeb
else
print("bisbeforea!");

```
##operator>
<br/>
####<div style='color:#FF69B4; display:inline-block'>bool</div> operator>( <div style='color:#008080; display:inline-block'>const  ManagedString  &</div> s)
#####Description
Inequality operation.
#####Parameters

>  <div style='color:#008080; display:inline-block'>const  ManagedString  &</div> *s* - The  ManagedString  to test ourselves against. 
#####Returns
true if this  ManagedString  is alphabetically greater than to the one supplied, false otherwise.
#####Example
```c++
ManagedStrings("a");
ManagedStringp("b");

if(p>a)
print("bisaftera!");//bisaftera
else
print("aisafterb!");

```
##substring
<br/>
####<div style='color:#FF69B4; display:inline-block'>ManagedString</div> substring( <div style='color:#008080; display:inline-block'>int16_t</div> start,  <div style='color:#008080; display:inline-block'>int16_t</div> length)
#####Description
Extracts a  ManagedString
#####Parameters

>  <div style='color:#008080; display:inline-block'>int16_t</div> *start* - The index of the first character to extract, indexed from zero. 

>  <div style='color:#008080; display:inline-block'>int16_t</div> *length* - The number of characters to extract from the start position 
#####Returns
a  ManagedString  representing the requested substring.
#####Example
```c++
ManagedStrings("abcdefg");

print(s.substring(0,2))//prints"ab"

```
##operator+
<br/>
####<div style='color:#FF69B4; display:inline-block'>ManagedString</div> operator+( <div style='color:#008080; display:inline-block'>ManagedString  &</div> s)
#####Description
Concatenates this string with the one provided.
#####Parameters

>  <div style='color:#008080; display:inline-block'>ManagedString  &</div> *s* - The  ManagedString  to concatenate. 
#####Returns
a new  ManagedString  representing the joined strings.
#####Example
```c++
ManagedStrings("abcd");
ManagedStringp("efgh")

print(s+p)//prints"abcdefgh"

```
##charAt
<br/>
####<div style='color:#FF69B4; display:inline-block'>char</div> charAt( <div style='color:#008080; display:inline-block'>int16_t</div> index)
#####Description
Provides a character value at a given position in the string, indexed from zero.
#####Parameters

>  <div style='color:#008080; display:inline-block'>int16_t</div> *index* - The position of the character to return. 
#####Returns
the character at posisiton index, zero if index is invalid.
#####Example
```c++
ManagedStrings("abcd");

print(s.charAt(1))//prints"b"

```
##toCharArray
<br/>
####<div style='color:#FF69B4; display:inline-block'>const char *</div> toCharArray()
#####Description
Provides an immutable 8 bit wide character buffer representing this string.
#####Returns
a pointer to the character buffer. 
##length
<br/>
####<div style='color:#FF69B4; display:inline-block'>int16_t</div> length()
#####Description
Determines the length of this  ManagedString
#####Returns
the length of the string in characters.
#####Example
```c++
ManagedStrings("abcd");

print(s.length())//prints"4"

```
____
[comment]: <> ({"end":"ManagedString"})
