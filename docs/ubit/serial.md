#uBit.serial

##Overview

##Message Bus ID

##Message Bus Events

##API
[comment]: <> ({"className":"MicroBitSerial"})
##Constructor
<br/>
####MicroBitSerial( <div style='color:#008080; display:inline-block'>PinName</div> tx,  <div style='color:#008080; display:inline-block'>PinName</div> rx)
#####Description
Constructor. Create an instance of  MicroBitSerial MicroBitSerial
#####Parameters

>  <div style='color:#008080; display:inline-block'>PinName</div> *tx*

>  <div style='color:#008080; display:inline-block'>PinName</div> *rx*
#####Example
```c++
 MicroBitSerial serial(USBTX, USBRX); 

```

!!! note
    the default baud rate is 115200 

##sendString
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> sendString( <div style='color:#008080; display:inline-block'>ManagedString</div> s)
#####Description
Sends a managed string over serial.
#####Parameters

>  <div style='color:#008080; display:inline-block'>ManagedString</div> *s* - the  ManagedString  to send
#####Example
```c++
 uBit.serial.printString("abc123"); 

```
##readString
<br/>
####<div style='color:#FF69B4; display:inline-block'>ManagedString</div> readString()
#####Description
Reads a  ManagedString
#####Example
```c++
 uBit.serial.readString(); 

```

!!! note
    this member function will wait until either the buffer is full, or a  
     is received 

<br/>
####<div style='color:#FF69B4; display:inline-block'>ManagedString</div> readString( <div style='color:#008080; display:inline-block'>int</div> len)
#####Description
Reads a  ManagedString
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *len* - the buffer size for the string, default is defined by MICROBIT_SERIAL_BUFFER_SIZE
#####Example
```c++
 uBit.serial.readString(); 

```

!!! note
    this member function will wait until either the buffer is full, or a  
     is received 

##sendImage
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> sendImage( <div style='color:#008080; display:inline-block'>MicroBitImage</div> i)
#####Description
Sends a  MicroBitImage
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitImage</div> *i* - the instance of  MicroBitImage  you would like to send.
#####Example
```c++
 const uint8_t heart[] = { 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, }; // a cute heart 
 MicroBitImage i(10,5,heart); 
 uBit.serial.sendImage(i); 

```
##readImage
<br/>
####<div style='color:#FF69B4; display:inline-block'>MicroBitImage</div> readImage( <div style='color:#008080; display:inline-block'>int</div> width,  <div style='color:#008080; display:inline-block'>int</div> height)
#####Description
Reads a  MicroBitImage
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *width*

>  <div style='color:#008080; display:inline-block'>int</div> *height*
#####Returns
a  MicroBitImage  with the format described over serial
#####Example
```c++
 MicroBitImage i = uBit.serial.readImage(2,2); 

```

!!! note
    this will finish once the dimensions are met.

##sendDisplayState
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> sendDisplayState()
#####Description
Sends the current pixel values, byte-per-pixel, over serial
#####Example
```c++
 uBit.serial.sendDisplayState(); 

```
##readDisplayState
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> readDisplayState()
#####Description
Reads pixel values, byte-per-pixel, from serial, and sets the display.
#####Example
```c++
 uBit.serial.readDisplayState(); 

```
____
[comment]: <> ({"end":"MicroBitSerial"})
