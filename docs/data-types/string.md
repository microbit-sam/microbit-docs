#ManagedString

##Overview

ManagedString represents a text string in the micro:bit runtime. A string is simply a sequency of characters such as 'joe' or 'microbit'.
In the C language, and the end of the string is marked by a special character (a NULL character, with the value zero).
Simple strings are often represented as literal character arrays e.g.

```cpp
    uBit.display.scroll("HELLO");
```
is actually almost exactly the same as:

```cpp
    char message[6] = {'H', 'E', 'L', 'L', 'O', 0};
    uBit.display.scroll(message);
```

Although fantastically simple, strings of this form are well known to lead to memory leaks and be sources of bugs in code (especially when the programmers are still learning!), so most modern
high level languages such as Java, C#, Javascript and TouchDevelop do not use strings of this format. Instead, they provide code that is capable of ensuring strings remain safe. ManagedString
provides this equivalent functionality for the micro:bit, as a building block for these hgher level languages. However, it can also makes programming the micro:bit in C easier too!

!!! note
    This is a **managed type**. This means that it will automatically use and release memory as needed. There is no need for you to explicitly free or release memory when your done - the memory will be freed as soon as the last piece of code stops using the data.

## Creating Strings

Images are simple to create - just create them like a variable, and provide the text or number you would like to build the string from. For example:

```cpp
    ManagedString hi("HELLO");
    ManagedString message("micro:bit");
    ManagedString n(42);
```

The runtime will also create a ManagedString for you from a number or quoted literal anytime a function needs a ManagedString. For example, even though the scroll funciton in microBitDisplay expects a ManagedString,
it is totally fine to pass a literal value in quotes or a number (or in fact, any parameter that is listed in the API secion as a legal constructor will work). For example:


```cpp
    ManagedString hi("HELLO");
    ManagedString message("micro:bit");
    ManagedString n(42);

    // All these calls are legal:
    uBit.display.scroll(hi);
    uBit.display.scroll(n);
    uBit.display.scroll("THANKS!");
```

## Manipulating Strings

ManagedStrings are **immutable**, meaning that once created, they cannot be changed. However, you can join them, search them, extract characters from them and create other strings! The micro:bur runtime makes use of **operator overloading** to keep this easy to use. In other works, we make use of the '=' '+' '<' '>' and '==' operators to let you easily assign and compare strings. Although this may sound complex, it is easy once you see how to do it. For example, here is how you would join together more than one string, and assign it to a new one:

```cpp
    ManagedString hi("HELLO");
    ManagedString message("micro:bit");
    ManagedString space(" ");

    ManagedString s = hi + space + message;

    // This would say "HELLO micro:bit" on the LED display.
    uBit.display.scroll(s);
```

You can compare strings (alphabetically) in a similar way:

```cpp

    ManagedString hi("HELLO");
    ManagedString message("micro:bit");

    if (hi == message)
        uBit.display.scroll("SAME");

    if (hi < message)
        uBit.display.scroll("LESS");

    if (hi > message)
        uBit.display.scroll("MORE");

```

You can also determine the length of a string, extract parts of strings, retrieve individual characters at a given index or convert a ManagedString to a C-style character array using the **'length'**, **'substring'**, **'charAt'** and **'toCharArray'** functions respectively. See the API docuemntation below for further details.

#API
[comment]: <> ({"className":"ManagedString"})
##Constructor
<br/>
####ManagedString( <div style='color:#008080; display:inline-block'>StringData  *</div> ptr)
#####Description
Constructor. Create a managed string from a specially prepared string literal.
#####Parameters

>  <div style='color:#008080; display:inline-block'>StringData  *</div> *ptr* - The literal - first two bytes should be 0xff, then the length in little endian, then the literal. The literal has to be 4-byte aligned.
#####Example
```cpp
 static const char hello[] __attribute__ ((aligned (4))) = "\xff\xff\x05\x00" "Hello";
 ManagedString s((StringData*)(void*)hello);
```
##leakData
<br/>
####<div style='color:#FF69B4; display:inline-block'>StringData</div> leakData()
#####Description
Get current ptr, do not decr() it, and set the current instance to empty string.
##Constructor
<br/>
####ManagedString( <div style='color:#008080; display:inline-block'>const char *</div> str)
#####Description
Constructor.
#####Parameters

>  <div style='color:#008080; display:inline-block'>const char *</div> *str* - The character array on which to base the new  ManagedString .
#####Example
```cpp
 ManagedString s("abcdefg");
```
<br/>
####ManagedString( <div style='color:#008080; display:inline-block'>const int</div> value)
#####Description
Constructor.
#####Parameters

>  <div style='color:#008080; display:inline-block'>const int</div> *value* - The integer from which to create the  ManagedString .
#####Example
```cpp
 ManagedString s(20);
```
<br/>
####ManagedString( <div style='color:#008080; display:inline-block'>const char</div> value)
#####Description
Constructor. Create a managed string from a given char.
#####Parameters

>  <div style='color:#008080; display:inline-block'>const char</div> *value* - The character from which to create the  ManagedString .
#####Example
```cpp
 ManagedString s('a');
```
<br/>
####ManagedString( <div style='color:#008080; display:inline-block'>PacketBuffer</div> buffer)
#####Description
Constructor. Create a  ManagedString PacketBuffer PacketBuffer ManagedString
#####Parameters

>  <div style='color:#008080; display:inline-block'>PacketBuffer</div> *buffer* - The PacktBuffer from which to create the  ManagedString .
#####Example
```cpp
 ManagedString s = radio.datagram.recv();
```
<br/>
####ManagedString( <div style='color:#008080; display:inline-block'>const char *</div> str,  <div style='color:#008080; display:inline-block'>const int16_t</div> length)
#####Description
Constructor. Create a  ManagedString
#####Parameters

>  <div style='color:#008080; display:inline-block'>const char *</div> *str* - The character array on which to base the new  ManagedString .

>  <div style='color:#008080; display:inline-block'>const int16_t</div> *length* - The length of the character array
#####Example
```cpp
 ManagedString s("abcdefg",7);
```
<br/>
####ManagedString( <div style='color:#008080; display:inline-block'>const  ManagedString  &</div> s)
#####Description
Copy constructor. Makes a new  ManagedString
#####Parameters

>  <div style='color:#008080; display:inline-block'>const  ManagedString  &</div> *s* - The  ManagedString  to copy.
#####Example
```cpp
 ManagedString s("abcdefg");
 ManagedString p(s);
```
<br/>
####ManagedString()
#####Description
Default constructor.
#####Example
```cpp
 ManagedString s();
```
##operator=
<br/>
####<div style='color:#FF69B4; display:inline-block'>ManagedString</div> operator=( <div style='color:#008080; display:inline-block'>const  ManagedString  &</div> s)
#####Description
Copy assign operation.
#####Parameters

>  <div style='color:#008080; display:inline-block'>const  ManagedString  &</div> *s* - The  ManagedString  to copy.
#####Example
```cpp
 ManagedString s("abcd");
 ManagedString p("efgh");
 p = s // p now points to s, s' ref is incremented
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
```cpp
 MicroBitDisplay display;
 ManagedString s("abcd");
 ManagedString p("efgh");

 if(p == s)
 display.scroll("We are the same!");
 else
 display.scroll("We are different!"); //p is not equal to s - this will be called
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
```cpp
 MicroBitDisplay display;
 ManagedString s("a");
 ManagedString p("b");

 if(s < p)
 display.scroll("a is before b!"); //a is before b
 else
 display.scroll("b is before a!");
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
```cpp
 MicroBitDisplay display;
 ManagedString s("a");
 ManagedString p("b");

 if(p>a)
 display.scroll("b is after a!"); //b is after a
 else
 display.scroll("a is after b!");
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
```cpp
 MicroBitDisplay display;
 ManagedString s("abcdefg");

 display.scroll(s.substring(0,2)) // displays "ab"
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
```cpp
 MicroBitDisplay display;
 ManagedString s("abcd");
 ManagedString p("efgh")

 display.scroll(s + p) // scrolls "abcdefgh"
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
```cpp
 MicroBitDisplay display;
 ManagedString s("abcd");

 display.scroll(s.charAt(1)) // scrolls "b"
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
```cpp
 MicroBitDisplay display;
 ManagedString s("abcd");

 display.scroll(s.length()) // scrolls "4"
```
____
[comment]: <> ({"end":"ManagedString"})
