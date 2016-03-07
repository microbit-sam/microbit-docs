#uBit.thermometer

##Overview

##Message Bus ID

##Message Bus Events

##API
[comment]: <> ({"className":"MicroBitThermometer"})
##Constructor
<br/>
####MicroBitThermometer( <div style='color:#008080; display:inline-block'>uint16_t</div> id)
#####Description
Constructor. Create new object that can sense temperature.  MicroBitThermometer
#####Parameters

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *id* - the ID of the new  MicroBitThermometer  object.
#####Example
```c++
thermometer(MICROBIT_ID_THERMOMETER);

```
##setPeriod
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> setPeriod( <div style='color:#008080; display:inline-block'>int</div> period)
#####Description
Set the sample rate at which the temperatureis read (in ms). n.b. the temperature is alwasy read in the background, so wis only updated when the processor is idle, or when the temperature is explicitly read. The default sample period is 1 second. 
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *period* - the requested time between samples, in milliseconds. 
##getPeriod
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getPeriod()
#####Description
Reads the currently configured sample rate of the thermometer. 
#####Returns
The time between samples, in milliseconds. 
##getTemperature
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getTemperature()
#####Description
Gets the current temperature of the microbit. 
#####Returns
the current temperature, in degrees celsius.
#####Example
```c++
uBit.thermometer.getTemperature();

```
##isIdleCallbackNeeded
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> isIdleCallbackNeeded()
#####Description
Indicates if we'd like some processor time to sense the temperature. 0 means we're not due to read the tmeperature yet. 
#####Returns
1 if we'd like some processor time, 0 otherwise. 
____
[comment]: <> ({"end":"MicroBitThermometer"})
