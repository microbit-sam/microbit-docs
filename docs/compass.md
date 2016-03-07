#uBit.compass

##Overview

##Message Bus ID

##Message Bus Events

##API
[comment]: <> ({"className":"MicroBitCompass"})
##Constructor
<br/>
####MicroBitCompass( <div style='color:#008080; display:inline-block'>uint16_t</div> id,  <div style='color:#008080; display:inline-block'>uint16_t</div> address)
#####Description
Constructor. Create a compass representation with the given ID. 
#####Parameters

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *id* - the event ID of the compass object. 

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *address* - the default address for the compass register
#####Example
```c++
compass(MICROBIT_ID_COMPASS,MAG3110_DEFAULT_ADDR);

```
##configure
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> configure()
#####Description
Configures the compass for the sample rate defined in this object. The nearest values are chosen to those defined that are supported by the hardware. The instance variables are then updated to reflect reality. 
#####Returns
MICROBIT_OK or MICROBIT_I2C_ERROR if the magnetometer could not be configured. 
##setPeriod
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> setPeriod( <div style='color:#008080; display:inline-block'>int</div> period)
#####Description
Attempts to set the sample rate of the compass to the specified value (in ms). n.b. the requested rate may not be possible on the hardware. In this case, the nearest lower rate is chosen. 
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *period* - the requested time between samples, in milliseconds. 
#####Returns
MICROBIT_OK or MICROBIT_I2C_ERROR if the magnetometer could not be updated. 
##getPeriod
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getPeriod()
#####Description
Reads the currently configured sample rate of the compass. 
#####Returns
The time between samples, in milliseconds. 
##heading
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> heading()
#####Description
Gets the current heading of the device, relative to magnetic north. If the compass is not calibrated, it will raise the MICROBIT_COMPASS_EVT_CALIBRATE event. Users wishing to implement their own calibration algorithms should listen for this event, using MESSAGE_BUS_LISTENER_IMMEDIATE model. This ensures that calibration is complete before the user program continues.
#####Returns
the current heading, in degrees. Or MICROBIT_CALIBRATION_IN_PROGRESS if the compass is calibrating.
#####Example
```c++
uBit.compass.heading();

```
##whoAmI
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> whoAmI()
#####Description
Attempts to determine the 8 bit ID from the magnetometer. 
#####Returns
the id of the compass (magnetometer), or MICROBIT_I2C_ERROR if the magnetometer could not be updated.
#####Example
```c++
uBit.compass.whoAmI();

```
##getX
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getX()
#####Description
Reads the X axis value of the latest update from the compass. 
#####Returns
The magnetic force measured in the X axis, in nano teslas.
#####Example
```c++
uBit.compass.getX();

```
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getX( <div style='color:#008080; display:inline-block'>MicroBitCoordinateSystem</div> system)
#####Description
Reads the X axis value of the latest update from the compass. 
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitCoordinateSystem</div> *system*
#####Returns
The magnetic force measured in the X axis, in nano teslas.
#####Example
```c++
uBit.compass.getX();

```
##getY
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getY()
#####Description
Reads the Y axis value of the latest update from the compass. 
#####Returns
The magnetic force measured in the Y axis, in nano teslas.
#####Example
```c++
uBit.compass.getY();

```
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getY( <div style='color:#008080; display:inline-block'>MicroBitCoordinateSystem</div> system)
#####Description
Reads the Y axis value of the latest update from the compass. 
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitCoordinateSystem</div> *system*
#####Returns
The magnetic force measured in the Y axis, in nano teslas.
#####Example
```c++
uBit.compass.getY();

```
##getZ
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getZ()
#####Description
Reads the Z axis value of the latest update from the compass. 
#####Returns
The magnetic force measured in the Z axis, in nano teslas.
#####Example
```c++
uBit.compass.getZ();

```
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getZ( <div style='color:#008080; display:inline-block'>MicroBitCoordinateSystem</div> system)
#####Description
Reads the Z axis value of the latest update from the compass. 
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitCoordinateSystem</div> *system*
#####Returns
The magnetic force measured in the Z axis, in nano teslas.
#####Example
```c++
uBit.compass.getZ();

```
##getFieldStrength
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getFieldStrength()
#####Description
Determines the overall magnetic field strength based on the latest update from the compass. 
#####Returns
The magnetic force measured across all axes, in nano teslas.
#####Example
```c++
uBit.compass.getFieldStrength();

```
##readTemperature
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> readTemperature()
#####Description
Reads the current die temperature of the compass. 
#####Returns
the temperature in degrees celsius, or MICROBIT_I2C_ERROR if the magnetometer could not be updated. 
##calibrate
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> calibrate()
#####Description
Perform a calibration of the compass.
#####Returns
MICROBIT_OK, MICROBIT_I2C_ERROR if the magnetometer could not be accessed, or MICROBIT_CALIBRATION_REQUIRED if the calibration algorithm failed to complete succesfully. 

!!! note
    THIS MUST BE CALLED TO GAIN RELIABLE VALUES FROM THE COMPASS ##calibrateAsync
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> calibrateAsync()
#####Description
Perform the asynchronous calibration of the compass. This will fire MICROBIT_COMPASS_EVT_CAL_START and MICROBIT_COMPASS_EVT_CAL_END when finished.  calibrate()
#####Returns
MICROBIT_OK, or MICROBIT_I2C_ERROR if the magnetometer could not be accessed.

!!! note
    *** THIS FUNCITON IS NOW DEPRECATED AND WILL BE REMOVED IN THE NEXT MAJOR RELEASE *** ##calibrateStart
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> calibrateStart()
#####Description
Perform a calibration of the compass. This will fire MICROBIT_COMPASS_EVT_CAL_START.
#####Returns
MICROBIT_OK, or MICROBIT_I2C_ERROR if the magnetometer could not be accessed.

!!! note
    *** THIS FUNCITON IS NOW DEPRECATED AND WILL BE REMOVED IN THE NEXT MAJOR RELEASE *** ##calibrateEnd
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> calibrateEnd()
#####Description
Complete the calibration of the compass. This will fire MICROBIT_COMPASS_EVT_CAL_END.

!!! note
    *** THIS FUNCITON IS NOW DEPRECATED AND WILL BE REMOVED IN THE NEXT MAJOR RELEASE ***##setCalibration
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> setCalibration( <div style='color:#008080; display:inline-block'>CompassSample</div> calibration)
#####Description
Configure the compass to use the given calibration data. Calibration data is comprised of the perceived zero offset of each axis of the compass. After calibration this should now take into account trimming errors in the magnetometer, and any "hard iron" offsets on the device.
#####Parameters

>  <div style='color:#008080; display:inline-block'>CompassSample</div> *calibration*
##getCalibration
<br/>
####<div style='color:#FF69B4; display:inline-block'>CompassSample</div> getCalibration()
#####Description
Provides the calibration data currently in use by the compass. More specifically, the x, y and z zero offsets of the compass.
#####Returns
The x, y and z xero offsets of the compass. 
##isCalibrated
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> isCalibrated()
#####Description
Returns 0 or 1. 1 indicates that the compass is calibrated, zero means the compass requires calibration. 
##isCalibrating
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> isCalibrating()
#####Description
Returns 0 or 1. 1 indicates that the compass is calibrating, zero means the compass is not currently calibrating. 
##clearCalibration
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> clearCalibration()
#####Description
Clears the calibration held in persistent storage, and sets the calibrated flag to zero. 
##isIdleCallbackNeeded
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> isIdleCallbackNeeded()
#####Description
Returns 0 or 1. 1 indicates data is waiting to be read, zero means data is not ready to be read. 
##~MicroBitCompass
<br/>
####~MicroBitCompass()
#####Description
Destructor for  MicroBitCompass
____
[comment]: <> ({"end":"MicroBitCompass"})
