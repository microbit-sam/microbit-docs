#PacketBuffer

##Overview

The [MicroBitRadio](/ubit/radio.md) classes provided direct micro:bit to micro:bit communication. It is often beneficial in both wired and wireless communication
protocols to send and receive data in a raw format, viewed as an ordered sequence of bytes. This class provies a basic set of functions for the creation, manipulation and
accessing of a managed type for byte arrays used to hold network data packets.

!!! note
    This is a **managed type**. This means that it will automatically use and release memory as needed. There is no need for you to explicitly free or release memory when your done - the memory will be freed as soon as the last piece of code stops using the data.


## Creating PacketBuffers

PacketBuffers are simple to create - just create them like a variable, and provide the size (in bytes) of the buffer you want to create.

```c++
    PacketBuffer b(16);
```

Alternatively, if you already have an array of bytes allocated, then you can somply refer to that using a slightly different form:

```c++
    uint8_t data[16];
    PacketBuffer b(data,16);
```

## Manipulating PacketBuffers

Once created, the data inside PacketBuffers can be freely changed at any time. The simplest way to do this is through the array operators '[' and ']'. 
You can read or write bytes to the buffer by simply dereferencing it with square bracket. e.g. to create, set and send a PacketBuffer on the micro:bit radio:

```c++
    PacketBuffer b(2);
    b[0] = 255;
    b[1] = 10;

    uBit.radio.datagram.send(b);
```

PacketBuffers can also be assigned a value. For example, all these are legal:

```c++
    PacketBuffer b;
    b = uBit.radio.datagram.recv();
```

If you need more granualar access, the getBytes function provides direct access to the memory buffer, presented as a byte array:

```c++
    PacketBuffer b(16);
    uint8_t *buf = b.getBytes();

    memcpy(buf, "HI", 2);
```

Finally, it is also possible to extract the received signal strength of a packet from a PakcetBuffer. This can provide both a rough indicaiton of the reliability of the link, and a crude but moderatley effective mechanism to estimate the distance between two micro:bts.

```c++
    PacketBuffer b;
    b = uBit.radio.datagram.recv();

    uBit.display.scroll(b.getRSSI());
```

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
```cpp
 static const char hello[] __attribute__ ((aligned (4))) = "\xff\xff\x05\x00" "Hello"; 
 ManagedString s((StringData*)(void*)hello); 

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
```cpp
 ManagedString s("abcdefg"); 

```
<br/>
####ManagedString( <div style='color:#008080; display:inline-block'>const int</div> value)
#####Description
Constructor. Create a managed string from a given integer.
#####Parameters

>  <div style='color:#008080; display:inline-block'>const int</div> *value* - The integer from which to create the  ManagedString
#####Example
```cpp
 ManagedString s(20); 

```
<br/>
####ManagedString( <div style='color:#008080; display:inline-block'>const char</div> value)
#####Description
Constructor. Create a managed string from a given char.
#####Parameters

>  <div style='color:#008080; display:inline-block'>const char</div> *value* - The char from which to create the  ManagedString
#####Example
```cpp
 ManagedString s('a'); 

```
<br/>
####ManagedString( <div style='color:#008080; display:inline-block'>PacketBuffer</div> buffer)
#####Description
Constructor. Create a  ManagedString PacketBuffer PacketBuffer ManagedString
#####Parameters

>  <div style='color:#008080; display:inline-block'>PacketBuffer</div> *buffer* - The PacktBuffer to generate the  ManagedString  from.
#####Example
```cpp
 ManagedString s = uBit.radio.datagram.recv(); 

```
<br/>
####ManagedString( <div style='color:#008080; display:inline-block'>const char *</div> str,  <div style='color:#008080; display:inline-block'>const int16_t</div> length)
#####Description
Constructor. Create a managed string from a pointer to an 8-bit character buffer of a given length. The buffer is copied to ensure sane memory management (the supplied character buffer may be declared on the stack for instance).
#####Parameters

>  <div style='color:#008080; display:inline-block'>const char *</div> *str* - The character array on which to base the new  ManagedString . 

>  <div style='color:#008080; display:inline-block'>const int16_t</div> *length* - The length of the character array
#####Example
```cpp
 ManagedString s("abcdefg",7); // this is generally used for substring... why not use a normal char * constructor? 

```
<br/>
####ManagedString( <div style='color:#008080; display:inline-block'>const  ManagedString  &</div> s)
#####Description
Copy constructor. Makes a new  ManagedString ManagedString
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
 ManagedString s("abcd"); 
 ManagedString p("efgh"); 
 
 if(p==s) 
 print("We are the same!"); 
 else 
 print("We are different!"); //p is not equal to s - this will be called 

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
 ManagedString s("a"); 
 ManagedString p("b"); 
 
 if(s<p) 
 print("a is before b!"); //a is before b 
 else 
 print("b is before a!"); 

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
 ManagedString s("a"); 
 ManagedString p("b"); 
 
 if(p>a) 
 print("b is after a!"); //b is after a 
 else 
 print("a is after b!"); 

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
 ManagedString s("abcdefg"); 
 
 print(s.substring(0,2)) // prints "ab" 

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
 ManagedString s("abcd"); 
 ManagedString p("efgh") 
 
 print(s + p) // prints "abcdefgh" 

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
 ManagedString s("abcd"); 
 
 print(s.charAt(1)) // prints "b" 

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
 ManagedString s("abcd"); 
 
 print(s.length()) // prints "4" 

```
____
[comment]: <> ({"end":"ManagedString"})
