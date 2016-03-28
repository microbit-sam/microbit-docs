#uBit

##Overview

uBit is the global singleton provided by the runtime and is an instance of the
MicroBit class.

The MicroBit class has a number of member variables, that operate as device drivers
to control the various features of the micro:bit.

>    uBit {<br/>
>    &emsp;&emsp;[.i2c](ubit/i2c.md),<br/>
>    &emsp;&emsp;[.serial](ubit/serial.md),<br/>
>    &emsp;&emsp;[.MessageBus](ubit/messageBus.md),<br/>
>    &emsp;&emsp;[.buttonA](ubit/button.md),<br/>
>    &emsp;&emsp;[.buttonB](ubit/button.md),<br/>
>    &emsp;&emsp;[.buttonAB](ubit/button.md),<br/>
>    &emsp;&emsp;[.display](ubit/display.md),<br/>
>    &emsp;&emsp;[.accelerometer](ubit/accelerometer.md),<br/>
>    &emsp;&emsp;[.compass](ubit/compass.md),<br/>
>    &emsp;&emsp;[.thermometer](ubit/thermometer.md),<br/>
>    &emsp;&emsp;[.io](ubit/io.md),<br/>
>    &emsp;&emsp;[.ble](ubit/ble.md),<br/>
>    &emsp;&emsp;[.BLEManager](ubit/blemanager.md),<br/>
>    &emsp;&emsp;[.radio](ubit/radio.md),<br/>
>    }

For example, if we needed to scroll some text across the display, we simply would
write the following:

```c++
uBit.display.scroll("HELLO!");
```

Similarly, if we wanted to send some text over serial, we could write the following
code:

```c++
for(int i = 3; i > 0; i--)
{
    uBit.serial.printf("%d...", i);
    uBit.sleep(1000);
}

uBit.serial.sendString("Code!");
```

uBit also provides a number of utility functions that allow the plug and play
of additional components that developers may create. These are namely <a href="#addsystemcomponent">addSystemComponent()</a>
and <a href="#addidlecomponent">addIdleComponent()</a>. [Read more about how to plug your own device drivers into the runtime.](todo.md)

The runtime also contains a scheduler, which uses lightweight threads (called fibers)
to control the rate of execution.

To place the current fiber into a power efficient <a href="#sleep">sleep</a> write the following:
```c++
// where X is an integer in milliseconds for the amount of time you would like to sleep for.
uBit.sleep(X);
```
[Read more about the scheduler.](todo.md)

##Message Bus ID

> None

##Message Bus Events

> None

##API
[comment]: <> ({"className":"MicroBit"})
##Constructor
<br/>
####MicroBit()
#####Description
Constructor. Create a representation of a  MicroBit MicroBitMessageBus
#####Example
```cpp
 uBit.messageBus; //The message bus where events are fired. 
 uBit.display; //The display object for the LED matrix. 
 uBit.buttonA; //The buttonA object for button a. 
 uBit.buttonB; //The buttonB object for button b. 
 uBit.resetButton; //The resetButton used for soft resets. 
 uBit.accelerometer; //The object that represents the inbuilt accelerometer 
 uBit.compass; //The object that represents the inbuilt compass(magnetometer) 
 uBit.io.P*; //Where P* is P0 to P16, P19 & P20 on the edge connector 

```
##init
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> init()
#####Description
Post constructor initialisation method. After 
#####Example
```cpp
 uBit.init(); 

```
##reset
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> reset()
#####Description
Will reset the micro:bit when called.
#####Example
```cpp
 uBit.reset(); 

```
##sleep
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> sleep( <div style='color:#008080; display:inline-block'>uint32_t</div> milliseconds)
#####Description
Delay for the given amount of time. If the scheduler is running, this will deschedule the current fiber and perform a power efficent, concurrent sleep operation. If the scheduler is disabled or we're running in an interrupt context, this will revert to a busy wait.
#####Parameters

>  <div style='color:#008080; display:inline-block'>uint32_t</div> *milliseconds* - the amount of time, in ms, to wait for. This number cannot be negative. 
#####Returns
MICROBIT_OK on success, MICROBIT_INVALID_PARAMETER milliseconds is less than zero.
#####Example
```cpp
 MicroBit::sleep(20); //sleep for 20ms 

```

!!! note
    Values of 6 and below tend to lose resolution - do you really need to sleep for this short amount of time?

##seedRandom
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> seedRandom()
#####Description
Seed the pseudo random number generator using the hardware generator.
#####Example
```cpp
 uBit.seedRandom(); 

```
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> seedRandom( <div style='color:#008080; display:inline-block'>uint32_t</div> seed)
#####Description
Seed the pseudo random number generator using the given value.
#####Parameters

>  <div style='color:#008080; display:inline-block'>uint32_t</div> *seed* - The 32-bit value to seed the generator with.
#####Example
```cpp
 uBit.seedRandom(0x12345678); 

```
##random
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> random( <div style='color:#008080; display:inline-block'>int</div> max)
#####Description
Generate a random number in the given range. We use the NRF51822 in built random number generator here TODO: Determine if we want to, given its relatively high power consumption!
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *max* - the upper range to generate a number for. This number cannot be negative 
#####Returns
A random, natural number between 0 and the max-1. Or MICROBIT_INVALID_PARAMETER if max is <= 0.
#####Example
```cpp
 uBit.random(200); //a number between 0 and 199 

```
##systemTime
<br/>
####<div style='color:#FF69B4; display:inline-block'>unsigned long</div> systemTime()
#####Description
Determine the time since this  MicroBit
#####Returns
The time since the last reset, in milliseconds. This will result in overflow after 1.6 months. TODO: handle overflow case. 
##systemVersion
<br/>
####<div style='color:#FF69B4; display:inline-block'>const char *</div> systemVersion()
#####Description
Determine the version of the micro:bit runtime currently in use.
#####Returns
A textual description of the currentlt executing micro:bit runtime. TODO: handle overflow case. 
##panic
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> panic()
#####Description
Triggers a microbit panic where an infinite loop will occur swapping between the panicFace and statusCode if provided.
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> panic( <div style='color:#008080; display:inline-block'>int</div> statusCode)
#####Description
Triggers a microbit panic where an infinite loop will occur swapping between the panicFace and statusCode if provided.
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *statusCode* - the status code of the associated error. Status codes must be in the range 0-255.
##addSystemComponent
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> addSystemComponent( <div style='color:#008080; display:inline-block'>MicroBitComponent  *</div> component)
#####Description
add a component to the array of components which invocate the systemTick member function during a systemTick 
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitComponent  *</div> *component* - The component to add. 
#####Returns
MICROBIT_OK on success. MICROBIT_NO_RESOURCES is returned if further components cannot be supported. 

!!! note
    This interface is now deprecated. See fiber_add_system_component().

##removeSystemComponent
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> removeSystemComponent( <div style='color:#008080; display:inline-block'>MicroBitComponent  *</div> component)
#####Description
remove a component from the array of components 
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitComponent  *</div> *component* - The component to remove. 
#####Returns
MICROBIT_OK on success. MICROBIT_INVALID_PARAMTER is returned if the given component has not been previous added. 

!!! note
    This interface is now deprecated. See fiber_remove_system_component().

##addIdleComponent
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> addIdleComponent( <div style='color:#008080; display:inline-block'>MicroBitComponent  *</div> component)
#####Description
add a component to the array of components which invocate the systemTick member function during a systemTick  fiber_add_idle_component()
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitComponent  *</div> *component* - The component to add. 
#####Returns
MICROBIT_OK on success. MICROBIT_NO_RESOURCES is returned if further components cannot be supported. 

!!! note
    This interface is now deprecated. See  fiber_add_idle_component() .

##removeIdleComponent
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> removeIdleComponent( <div style='color:#008080; display:inline-block'>MicroBitComponent  *</div> component)
#####Description
remove a component from the array of components  fiber_remove_idle_component()
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitComponent  *</div> *component* - The component to remove. 
#####Returns
MICROBIT_OK on success. MICROBIT_INVALID_PARAMTER is returned if the given component has not been previous added. 

!!! note
    This interface is now deprecated. See  fiber_remove_idle_component() .

____
[comment]: <> ({"end":"MicroBit"})
