#uBit.compass

##Overview

##Message Bus ID

##Message Bus Events

##API
[comment]: <> ({"className":"MicroBitCompass"})
____
##Constructor
<br/>
####MicroBitCompass( <div style='color:#008080; display:inline-block'>uint16_t</div> id,  <div style='color:#008080; display:inline-block'>uint16_t</div> address)
<br/>
#####Description
Constructor. Create a compass representation with the given ID. 

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *id* - the event ID of the compass object. 

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *address* - the default address for the compass register

<br/><br/>
#####Example
```c++
compass(MICROBIT_ID_COMPASS,MAG3110_DEFAULT_ADDR);

```

<br/><br/>
____
##configure
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> configure()
<br/>
#####Description
Configures the compass for the sample rate defined in this object. The nearest values are chosen to those defined that are supported by the hardware. The instance variables are then updated to reflect reality. 

<br/><br/>
#####Returns
MICROBIT_OK or MICROBIT_I2C_ERROR if the magnetometer could not be configured. 

<br/><br/>
____
##setPeriod
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> setPeriod( <div style='color:#008080; display:inline-block'>int</div> period)
<br/>
#####Description
Attempts to set the sample rate of the compass to the specified value (in ms). n.b. the requested rate may not be possible on the hardware. In this case, the nearest lower rate is chosen. 

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *period* - the requested time between samples, in milliseconds. 

<br/><br/>
#####Returns
MICROBIT_OK or MICROBIT_I2C_ERROR if the magnetometer could not be updated. 

<br/><br/>
____
##getPeriod
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getPeriod()
<br/>
#####Description
Reads the currently configured sample rate of the compass. 

<br/><br/>
#####Returns
The time between samples, in milliseconds. 

<br/><br/>
____
##heading
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> heading()
<br/>
#####Description
Gets the current heading of the device, relative to magnetic north. If the compass is not calibrated, it will raise the MICROBIT_COMPASS_EVT_CALIBRATE event. Users wishing to implement their own calibration algorithms should listen for this event, using MESSAGE_BUS_LISTENER_IMMEDIATE model. This ensures that calibration is complete before the user program continues.

<br/><br/>
#####Returns
the current heading, in degrees. Or MICROBIT_CALIBRATION_IN_PROGRESS if the compass is calibrating.

<br/><br/>
#####Example
```c++
uBit.compass.heading();

```

<br/><br/>
____
##whoAmI
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> whoAmI()
<br/>
#####Description
Attempts to determine the 8 bit ID from the magnetometer. 

<br/><br/>
#####Returns
the id of the compass (magnetometer), or MICROBIT_I2C_ERROR if the magnetometer could not be updated.

<br/><br/>
#####Example
```c++
uBit.compass.whoAmI();

```

<br/><br/>
____
##getX
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getX()
<br/>
#####Description
Reads the X axis value of the latest update from the compass. 

<br/><br/>
#####Returns
The magnetic force measured in the X axis, in nano teslas.

<br/><br/>
#####Example
```c++
uBit.compass.getX();

```

<br/><br/>
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getX( <div style='color:#008080; display:inline-block'>MicroBitCoordinateSystem</div> system)
<br/>
#####Description
Reads the X axis value of the latest update from the compass. 

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitCoordinateSystem</div> *system*

<br/><br/>
#####Returns
The magnetic force measured in the X axis, in nano teslas.

<br/><br/>
#####Example
```c++
uBit.compass.getX();

```

<br/><br/>
____
##getY
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getY()
<br/>
#####Description
Reads the Y axis value of the latest update from the compass. 

<br/><br/>
#####Returns
The magnetic force measured in the Y axis, in nano teslas.

<br/><br/>
#####Example
```c++
uBit.compass.getY();

```

<br/><br/>
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getY( <div style='color:#008080; display:inline-block'>MicroBitCoordinateSystem</div> system)
<br/>
#####Description
Reads the Y axis value of the latest update from the compass. 

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitCoordinateSystem</div> *system*

<br/><br/>
#####Returns
The magnetic force measured in the Y axis, in nano teslas.

<br/><br/>
#####Example
```c++
uBit.compass.getY();

```

<br/><br/>
____
##getZ
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getZ()
<br/>
#####Description
Reads the Z axis value of the latest update from the compass. 

<br/><br/>
#####Returns
The magnetic force measured in the Z axis, in nano teslas.

<br/><br/>
#####Example
```c++
uBit.compass.getZ();

```

<br/><br/>
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getZ( <div style='color:#008080; display:inline-block'>MicroBitCoordinateSystem</div> system)
<br/>
#####Description
Reads the Z axis value of the latest update from the compass. 

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitCoordinateSystem</div> *system*

<br/><br/>
#####Returns
The magnetic force measured in the Z axis, in nano teslas.

<br/><br/>
#####Example
```c++
uBit.compass.getZ();

```

<br/><br/>
____
##getFieldStrength
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getFieldStrength()
<br/>
#####Description
Determines the overall magnetic field strength based on the latest update from the compass. 

<br/><br/>
#####Returns
The magnetic force measured across all axes, in nano teslas.

<br/><br/>
#####Example
```c++
uBit.compass.getFieldStrength();

```

<br/><br/>
____
##readTemperature
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> readTemperature()
<br/>
#####Description
Reads the current die temperature of the compass. 

<br/><br/>
#####Returns
the temperature in degrees celsius, or MICROBIT_I2C_ERROR if the magnetometer could not be updated. 

<br/><br/>
____
##calibrate
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> calibrate()
<br/>
#####Description
Perform a calibration of the compass.

<br/><br/>
#####Returns
MICROBIT_OK, MICROBIT_I2C_ERROR if the magnetometer could not be accessed, or MICROBIT_CALIBRATION_REQUIRED if the calibration algorithm failed to complete succesfully. 

<br/><br/>

!!! note
    THIS MUST BE CALLED TO GAIN RELIABLE VALUES FROM THE COMPASS 
<br/><br/>
____
##calibrateAsync
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> calibrateAsync()
<br/>
#####Description
Perform the asynchronous calibration of the compass. This will fire MICROBIT_COMPASS_EVT_CAL_START and MICROBIT_COMPASS_EVT_CAL_END when finished.  calibrate()

<br/><br/>
#####Returns
MICROBIT_OK, or MICROBIT_I2C_ERROR if the magnetometer could not be accessed.

<br/><br/>

!!! note
    *** THIS FUNCITON IS NOW DEPRECATED AND WILL BE REMOVED IN THE NEXT MAJOR RELEASE *** 
<br/><br/>
____
##calibrateStart
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> calibrateStart()
<br/>
#####Description
Perform a calibration of the compass. This will fire MICROBIT_COMPASS_EVT_CAL_START.

<br/><br/>
#####Returns
MICROBIT_OK, or MICROBIT_I2C_ERROR if the magnetometer could not be accessed.

<br/><br/>

!!! note
    *** THIS FUNCITON IS NOW DEPRECATED AND WILL BE REMOVED IN THE NEXT MAJOR RELEASE *** 
<br/><br/>
____
##calibrateEnd
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> calibrateEnd()
<br/>
#####Description
Complete the calibration of the compass. This will fire MICROBIT_COMPASS_EVT_CAL_END.

<br/><br/>

!!! note
    *** THIS FUNCITON IS NOW DEPRECATED AND WILL BE REMOVED IN THE NEXT MAJOR RELEASE ***
<br/><br/>
____
##setCalibration
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> setCalibration( <div style='color:#008080; display:inline-block'>CompassSample</div> calibration)
<br/>
#####Description
Configure the compass to use the given calibration data. Calibration data is comprised of the perceived zero offset of each axis of the compass. After calibration this should now take into account trimming errors in the magnetometer, and any "hard iron" offsets on the device.

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>CompassSample</div> *calibration*

<br/><br/>
____
##getCalibration
<br/>
####<div style='color:#FF69B4; display:inline-block'>CompassSample</div> getCalibration()
<br/>
#####Description
Provides the calibration data currently in use by the compass. More specifically, the x, y and z zero offsets of the compass.

<br/><br/>
#####Returns
The x, y and z xero offsets of the compass. 

<br/><br/>
____
##isCalibrated
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> isCalibrated()
<br/>
#####Description
Returns 0 or 1. 1 indicates that the compass is calibrated, zero means the compass requires calibration. 

<br/><br/>
____
##isCalibrating
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> isCalibrating()
<br/>
#####Description
Returns 0 or 1. 1 indicates that the compass is calibrating, zero means the compass is not currently calibrating. 

<br/><br/>
____
##clearCalibration
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> clearCalibration()
<br/>
#####Description
Clears the calibration held in persistent storage, and sets the calibrated flag to zero. 

<br/><br/>
____
##isIdleCallbackNeeded
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> isIdleCallbackNeeded()
<br/>
#####Description
Returns 0 or 1. 1 indicates data is waiting to be read, zero means data is not ready to be read. 

<br/><br/>
____
##~MicroBitCompass
<br/>
####~MicroBitCompass()
<br/>
#####Description
Destructor for  MicroBitCompass

<br/><br/>
____
[comment]: <> ({"end":"MicroBitCompass"})
