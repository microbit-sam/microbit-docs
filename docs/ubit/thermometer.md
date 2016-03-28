#uBit.thermometer

##Overview

MicroBitThermometer provides access to the surface temperature of the nrf51822.
The temperature reading therefore is not representative of the ambient temperature,
but rather the temperature relative to the surface temperature of the chip.

However, we can make it representative of the ambient temperature in software
through "calibrating" the thermometer.

Calibration is very simple, and is calculated by giving the current temperature
to the `setCalibration()` member function. From the temperature, an offset is
calculated, and is subsequently used to offset future temperature readings.


### Real time updates

When using the standard uBit presentation, the thermometer is continuously updated
in the background using an idle thread (after it is first used), which is executed
whenever the micro:bit has no other tasks to perform.

If there is no scheduler running, the values are synchronously read on `getTemperature()`
calls. Additionally, if you would like to drive thermometer updates manually `updateSample()`
can be used.

##Message Bus ID

| Constant | Value |
| ------------- |-------------|
| MICROBIT_ID_THERMOMETER | 28 |

##Message Bus Events

| Constant | Value |
| ------------- |-------------|
| MICROBIT_THERMOMETER_EVT_UPDATE | 1 |

##API
[comment]: <> ({"className":"MicroBitThermometer"})
##Constructor
<br/>
####MicroBitThermometer( <div style='color:#008080; display:inline-block'>MicroBitStorage  &</div> _storage)
#####Description
Constructor. Create new object that can sense temperature.  MicroBitThermometer MicroBitStorage
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitStorage  &</div> *_storage* - an instance of  MicroBitStorage  used to persist temperature offset data
#####Example
```cpp
 thermometer(MICROBIT_ID_THERMOMETER); 

```
<br/>
####MicroBitThermometer( <div style='color:#008080; display:inline-block'>MicroBitStorage  &</div> _storage,  <div style='color:#008080; display:inline-block'>uint16_t</div> id)
#####Description
Constructor. Create new object that can sense temperature.  MicroBitThermometer MicroBitStorage
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitStorage  &</div> *_storage* - an instance of  MicroBitStorage  used to persist temperature offset data

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *id* - the ID of the new  MicroBitThermometer  object. 
#####Example
```cpp
 thermometer(MICROBIT_ID_THERMOMETER); 

```
<br/>
####MicroBitThermometer()
#####Description
Constructor. Create new object that can sense temperature.  MicroBitThermometer
#####Example
```cpp
 thermometer(MICROBIT_ID_THERMOMETER); 

```
<br/>
####MicroBitThermometer( <div style='color:#008080; display:inline-block'>uint16_t</div> id)
#####Description
Constructor. Create new object that can sense temperature.  MicroBitThermometer
#####Parameters

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *id* - the ID of the new  MicroBitThermometer  object.
#####Example
```cpp
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
##setOffset
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> setOffset( <div style='color:#008080; display:inline-block'>int</div> offset)
#####Description
Set the value that is used to offset the raw silicon temperature.
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *offset* - the offset for the silicon temperature
#####Returns
MICROBIT_OK on success 
##getOffset
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getOffset()
#####Description
Retreive the value that is used to offset the raw silicon temperature.
##setCalibration
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> setCalibration( <div style='color:#008080; display:inline-block'>int</div> calibrationTemp)
#####Description
This member function fetches the raw silicon temperature, and calculates the value used to offset the raw silicon temperature based on a given temperature.
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *calibrationTemp* - the temperature used to calculate the raw silicon temperature offset.
#####Returns
MICROBIT_OK on success 
##getTemperature
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getTemperature()
#####Description
Gets the current temperature of the microbit. 
#####Returns
the current temperature, in degrees celsius.
#####Example
```cpp
 uBit.thermometer.getTemperature(); 

```
##updateSample
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> updateSample()
#####Description
Updates the temperature sample of this instance of  MicroBitThermometer isSampleNeeded()
#####Returns
MICROBIT_OK on success. 
##isIdleCallbackNeeded
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> isIdleCallbackNeeded()
#####Description
Indicates if we'd like some processor time to sense the temperature. 0 means we're not due to read the tmeperature yet. 
#####Returns
1 if we'd like some processor time, 0 otherwise. 
____
[comment]: <> ({"end":"MicroBitThermometer"})
