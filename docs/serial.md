#uBit.serial

##Overview

##Message Bus ID

##Message Bus Events

##API
[comment]: <> ({"className":"MicroBitSerial"})
____
##Constructor
<br/>
####MicroBitSerial( <div style='color:#008080; display:inline-block'>PinName</div> tx,  <div style='color:#008080; display:inline-block'>PinName</div> rx)
<br/>
#####Description
Constructor. Create an instance of  MicroBitSerial MicroBitSerial

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>PinName</div> *tx*

>  <div style='color:#008080; display:inline-block'>PinName</div> *rx*

<br/><br/>
#####Example
```c++
MicroBitSerialserial(USBTX,USBRX);

```

<br/><br/>

!!! note
    the default baud rate is 115200 
<br/><br/>
____
##sendString
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> sendString( <div style='color:#008080; display:inline-block'>ManagedString</div> s)
<br/>
#####Description
Sends a managed string over serial.

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>ManagedString</div> *s* - the  ManagedString  to send

<br/><br/>
#####Example
```c++
uBit.serial.printString("abc123");

```

<br/><br/>
____
##readString
<br/>
####<div style='color:#FF69B4; display:inline-block'>ManagedString</div> readString()
<br/>
#####Description
Reads a  ManagedString

<br/><br/>
#####Example
```c++
uBit.serial.readString();

```

<br/><br/>

!!! note
    this member function will wait until either the buffer is full, or a  
     is received 
<br/><br/>
<br/>
####<div style='color:#FF69B4; display:inline-block'>ManagedString</div> readString( <div style='color:#008080; display:inline-block'>int</div> len)
<br/>
#####Description
Reads a  ManagedString

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *len* - the buffer size for the string, default is defined by MICROBIT_SERIAL_BUFFER_SIZE

<br/><br/>
#####Example
```c++
uBit.serial.readString();

```

<br/><br/>

!!! note
    this member function will wait until either the buffer is full, or a  
     is received 
<br/><br/>
____
##sendImage
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> sendImage( <div style='color:#008080; display:inline-block'>MicroBitImage</div> i)
<br/>
#####Description
Sends a  MicroBitImage

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitImage</div> *i* - the instance of  MicroBitImage  you would like to send.

<br/><br/>
#####Example
```c++
constuint8_theart[]={0,1,0,1,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,0,1,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,};//acuteheart
MicroBitImagei(10,5,heart);
uBit.serial.sendImage(i);

```

<br/><br/>
____
##readImage
<br/>
####<div style='color:#FF69B4; display:inline-block'>MicroBitImage</div> readImage( <div style='color:#008080; display:inline-block'>int</div> width,  <div style='color:#008080; display:inline-block'>int</div> height)
<br/>
#####Description
Reads a  MicroBitImage

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *width*

>  <div style='color:#008080; display:inline-block'>int</div> *height*

<br/><br/>
#####Returns
a  MicroBitImage  with the format described over serial

<br/><br/>
#####Example
```c++
MicroBitImagei=uBit.serial.readImage(2,2);

```

<br/><br/>

!!! note
    this will finish once the dimensions are met.
<br/><br/>
____
##sendDisplayState
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> sendDisplayState()
<br/>
#####Description
Sends the current pixel values, byte-per-pixel, over serial

<br/><br/>
#####Example
```c++
uBit.serial.sendDisplayState();

```

<br/><br/>
____
##readDisplayState
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> readDisplayState()
<br/>
#####Description
Reads pixel values, byte-per-pixel, from serial, and sets the display.

<br/><br/>
#####Example
```c++
uBit.serial.readDisplayState();

```

<br/><br/>
____
[comment]: <> ({"end":"MicroBitSerial"})
