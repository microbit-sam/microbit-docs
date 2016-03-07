#uBit.thermometer

##Overview

##Message Bus ID

##Message Bus Events

##API
[comment]: <> ({"className":"MicroBitThermometer"})
____
##Constructor
<br/>
####MicroBitThermometer( <div style='color:#008080; display:inline-block'>uint16_t</div> id)
<br/>
#####Description
Constructor. Create new object that can sense temperature.  MicroBitThermometer

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *id* - the ID of the new  MicroBitThermometer  object.

<br/><br/>
#####Example
```c++
thermometer(MICROBIT_ID_THERMOMETER);

```

<br/><br/>
____
##setPeriod
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> setPeriod( <div style='color:#008080; display:inline-block'>int</div> period)
<br/>
#####Description
Set the sample rate at which the temperatureis read (in ms). n.b. the temperature is alwasy read in the background, so wis only updated when the processor is idle, or when the temperature is explicitly read. The default sample period is 1 second. 

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *period* - the requested time between samples, in milliseconds. 

<br/><br/>
____
##getPeriod
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getPeriod()
<br/>
#####Description
Reads the currently configured sample rate of the thermometer. 

<br/><br/>
#####Returns
The time between samples, in milliseconds. 

<br/><br/>
____
##getTemperature
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getTemperature()
<br/>
#####Description
Gets the current temperature of the microbit. 

<br/><br/>
#####Returns
the current temperature, in degrees celsius.

<br/><br/>
#####Example
```c++
uBit.thermometer.getTemperature();

```

<br/><br/>
____
##isIdleCallbackNeeded
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> isIdleCallbackNeeded()
<br/>
#####Description
Indicates if we'd like some processor time to sense the temperature. 0 means we're not due to read the tmeperature yet. 

<br/><br/>
#####Returns
1 if we'd like some processor time, 0 otherwise. 

<br/><br/>
____
[comment]: <> ({"end":"MicroBitThermometer"})
