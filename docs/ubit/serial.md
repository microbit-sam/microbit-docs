#uBit.serial

##Overview

Serial communication provides a simple way to exchange a series of bytes between one computer and another.  The runtime's implementation of serial is general purpose and supports a number of different modes. It has a circular buffer for both the reception and transmission of data, and provides notifications to the user through the MessageBus.

By default, the baud rate for MicroBitSerial is `115200` and has very little overhead up until
it is used to `send()` or `read()`, at which point buffers are allocated in order
to accommodate incoming or outgoing data.

MicroBitSerial inherits from mbeds' [`RawSerial`](https://developer.mbed.org/users/mbed_official/code/mbed/docs/252557024ec3/classmbed_1_1RawSerial.html)
class, which exposes a lightweight version of `printf()` and incurs minimal overhead
as MicroBitSerial's buffers will not be allocated.

The MicroBitSerial class supports multithreaded operation, ensuring that only
one fiber can access the Serial port at a time.

The USB interface on the micro:bit is the [KL26Z](https://www.mbed.com/en/development/hardware/prototyping-production/daplink/daplink-on-kl26z/#Updating_your_DAPLink_firmware).

!!! note
    On Mac OSX and Linux Serial communication works out of the box, however on Windows an additional
    **[driver](https://developer.mbed.org/handbook/Windows-serial-configuration)** is required.

!!! warning
    The baud rate is shared across all instances of MicroBitSerial (this is enforced in hardware).

### Serial modes

There are three modes of operation for all `send()` or `read()` calls:

- `ASYNC` - Returns immediately after fetching any available data for a given call
- `SYNC_SPINWAIT` - Synchronously access the serial port until the selected operation is complete.
                    This mode will lock up the processor, and isn't recommended if multiple fibers are in use.
- `SYNC_SLEEP` - Blocks the current fiber until the selected operation is complete. This mode cooperates with the
                 Fiber scheduler, and should be used in a multi-fiber program.

### Serial debug

In MicroBitConfig.h, the configuration option `MICROBIT_DEBUG` can be used to activate serial debugging
for many of the components in the runtime.


##Message Bus ID

| Constant | Value |
| ------------- |-------------|
| MICROBIT_ID_SERIAL | 32 |

##Message Bus Events

| Constant | Value |
| ------------- |-------------|
| MICROBIT_SERIAL_EVT_DELIM_MATCH | 1 |
| MICROBIT_SERIAL_EVT_HEAD_MATCH | 2 |
| MICROBIT_SERIAL_EVT_RX_FULL | 3 |

## Notify Events

These events use the notification channel `MICROBIT_ID_NOTIFY`, which provides
general purpose synchronisation.

| Constant | Value |
| ------------- |-------------|
| MICROBIT_SERIAL_EVT_TX_EMPTY | 2 |

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
