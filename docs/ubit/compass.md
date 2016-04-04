#uBit.compass

##Overview

Onboard the micro:bit is an electronic magnetometer. Like the [accelerometer](accelerometer.md), the  
magnetometer is linked to the [i2c](i2c.md) bus, which is used to access data
on the magnetometer.

The magnetometer provides information about the magnetic field where a micro:bit
is situated, crucially providing an indication of where magnetic North is located.

Raw magnetic field information alone is not enough to provide accurate
compass headings. Therefore, the [accelerometer](accelerometer.md) is used in
conjunction with the magnetometer to reduce the inaccuracy of the magnetometer reading.

The magnetometer is inaccurate because it considers all 3 planes: x, y and z.
The heading North only exists in the horizontal planes (x and y), therefore we only
need values in these planes. The accelerometer is used to filter out the vertical plane (z)
to make our headings far more accurate. You can see this in action when calibrating the compass.

After calibration has been performed, the end product is an e-compass!

The micro:bit uses the [NXP MAG3110](http://www.nxp.com/products/sensors/magnetometers/sample-data-sets-for-inertial-and-magnetic-sensors/freescale-high-accuracy-3d-magnetometer:MAG3110).

### Real time updates

When using the standard uBit presentation, the compass is continuously updated
in the background using an idle thread (after it is first used), which is executed
whenever the micro:bit has no other tasks to perform.

If there is no scheduler running, the values are synchronously read on `get[X,Y,Z]()` and `heading()`
calls. Additionally, if you would like to drive compass updates manually `updateSample()`
can be used.


##Message Bus ID

| Constant | Value |
| ------------- |-------------|
| MICROBIT_ID_COMPASS | 5 |

##Message Bus Events

| Constant | Value |
| ------------- |-------------|
| MICROBIT_COMPASS_EVT_CAL_REQUIRED | 1 **(DEPRECATED)**|
| MICROBIT_COMPASS_EVT_CAL_START | 2 **(DEPRECATED)** |
| MICROBIT_COMPASS_EVT_CAL_END | 3 **(DEPRECATED)** |
| MICROBIT_COMPASS_EVT_DATA_UPDATE | 4 |
| MICROBIT_COMPASS_EVT_CONFIG_NEEDED | 5 |
| MICROBIT_COMPASS_EVT_CALIBRATE | 6 |

##API
[comment]: <> ({"className":"MicroBitCompass"})
##Constructor
<br/>
####MicroBitCompass( <div style='color:#008080; display:inline-block'>MicroBitI2C  &</div> _i2c,  <div style='color:#008080; display:inline-block'>MicroBitAccelerometer  &</div> _accelerometer,  <div style='color:#008080; display:inline-block'>MicroBitStorage  &</div> _storage)
#####Description
Constructor. Create a software representation of an e-compass.
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitI2C  &</div> *_i2c* - an instance of i2c, which the compass is accessible from.

>  <div style='color:#008080; display:inline-block'>MicroBitAccelerometer  &</div> *_accelerometer* - an instance of the accelerometer, used for tilt compensation.

>  <div style='color:#008080; display:inline-block'>MicroBitStorage  &</div> *_storage* - an instance of  MicroBitStorage , used to persist calibration data across resets.
#####Example
```cpp
 MicroBitI2C i2c(I2C_SDA0, I2C_SCL0); 
 
 MicroBitAccelerometer accelerometer(i2c); 
 
 MicroBitStorage storage; 
 
 MicroBitCompass compass(i2c, accelerometer, storage); 
```
<br/>
####MicroBitCompass( <div style='color:#008080; display:inline-block'>MicroBitI2C  &</div> _i2c,  <div style='color:#008080; display:inline-block'>MicroBitAccelerometer  &</div> _accelerometer,  <div style='color:#008080; display:inline-block'>MicroBitStorage  &</div> _storage,  <div style='color:#008080; display:inline-block'>uint16_t</div> address)
#####Description
Constructor. Create a software representation of an e-compass.
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitI2C  &</div> *_i2c* - an instance of i2c, which the compass is accessible from.

>  <div style='color:#008080; display:inline-block'>MicroBitAccelerometer  &</div> *_accelerometer* - an instance of the accelerometer, used for tilt compensation.

>  <div style='color:#008080; display:inline-block'>MicroBitStorage  &</div> *_storage* - an instance of  MicroBitStorage , used to persist calibration data across resets.

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *address* - the default address for the compass register on the i2c bus. Defaults to MAG3110_DEFAULT_ADDR.
#####Example
```cpp
 MicroBitI2C i2c(I2C_SDA0, I2C_SCL0); 
 
 MicroBitAccelerometer accelerometer(i2c); 
 
 MicroBitStorage storage; 
 
 MicroBitCompass compass(i2c, accelerometer, storage); 
```
<br/>
####MicroBitCompass( <div style='color:#008080; display:inline-block'>MicroBitI2C  &</div> _i2c,  <div style='color:#008080; display:inline-block'>MicroBitAccelerometer  &</div> _accelerometer,  <div style='color:#008080; display:inline-block'>MicroBitStorage  &</div> _storage,  <div style='color:#008080; display:inline-block'>uint16_t</div> address,  <div style='color:#008080; display:inline-block'>uint16_t</div> id)
#####Description
Constructor. Create a software representation of an e-compass.
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitI2C  &</div> *_i2c* - an instance of i2c, which the compass is accessible from.

>  <div style='color:#008080; display:inline-block'>MicroBitAccelerometer  &</div> *_accelerometer* - an instance of the accelerometer, used for tilt compensation.

>  <div style='color:#008080; display:inline-block'>MicroBitStorage  &</div> *_storage* - an instance of  MicroBitStorage , used to persist calibration data across resets.

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *address* - the default address for the compass register on the i2c bus. Defaults to MAG3110_DEFAULT_ADDR.

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *id* - the ID of the new  MicroBitCompass  object. Defaults to MAG3110_DEFAULT_ADDR.
#####Example
```cpp
 MicroBitI2C i2c(I2C_SDA0, I2C_SCL0); 
 
 MicroBitAccelerometer accelerometer(i2c); 
 
 MicroBitStorage storage; 
 
 MicroBitCompass compass(i2c, accelerometer, storage); 
```
<br/>
####MicroBitCompass( <div style='color:#008080; display:inline-block'>MicroBitI2C  &</div> _i2c,  <div style='color:#008080; display:inline-block'>MicroBitAccelerometer  &</div> _accelerometer)
#####Description
Constructor. Create a software representation of an e-compass.
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitI2C  &</div> *_i2c* - an instance of i2c, which the compass is accessible from.

>  <div style='color:#008080; display:inline-block'>MicroBitAccelerometer  &</div> *_accelerometer* - an instance of the accelerometer, used for tilt compensation.
#####Example
```cpp
 MicroBitI2C i2c(I2C_SDA0, I2C_SCL0); 
 
 MicroBitAccelerometer accelerometer(i2c); 
 
 MicroBitCompass compass(i2c, accelerometer, storage); 
```
<br/>
####MicroBitCompass( <div style='color:#008080; display:inline-block'>MicroBitI2C  &</div> _i2c,  <div style='color:#008080; display:inline-block'>MicroBitAccelerometer  &</div> _accelerometer,  <div style='color:#008080; display:inline-block'>uint16_t</div> address)
#####Description
Constructor. Create a software representation of an e-compass.
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitI2C  &</div> *_i2c* - an instance of i2c, which the compass is accessible from.

>  <div style='color:#008080; display:inline-block'>MicroBitAccelerometer  &</div> *_accelerometer* - an instance of the accelerometer, used for tilt compensation.

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *address* - the default address for the compass register on the i2c bus. Defaults to MAG3110_DEFAULT_ADDR.
#####Example
```cpp
 MicroBitI2C i2c(I2C_SDA0, I2C_SCL0); 
 
 MicroBitAccelerometer accelerometer(i2c); 
 
 MicroBitCompass compass(i2c, accelerometer, storage); 
```
<br/>
####MicroBitCompass( <div style='color:#008080; display:inline-block'>MicroBitI2C  &</div> _i2c,  <div style='color:#008080; display:inline-block'>MicroBitAccelerometer  &</div> _accelerometer,  <div style='color:#008080; display:inline-block'>uint16_t</div> address,  <div style='color:#008080; display:inline-block'>uint16_t</div> id)
#####Description
Constructor. Create a software representation of an e-compass.
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitI2C  &</div> *_i2c* - an instance of i2c, which the compass is accessible from.

>  <div style='color:#008080; display:inline-block'>MicroBitAccelerometer  &</div> *_accelerometer* - an instance of the accelerometer, used for tilt compensation.

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *address* - the default address for the compass register on the i2c bus. Defaults to MAG3110_DEFAULT_ADDR.

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *id* - the ID of the new  MicroBitCompass  object. Defaults to MAG3110_DEFAULT_ADDR.
#####Example
```cpp
 MicroBitI2C i2c(I2C_SDA0, I2C_SCL0); 
 
 MicroBitAccelerometer accelerometer(i2c); 
 
 MicroBitCompass compass(i2c, accelerometer, storage); 
```
<br/>
####MicroBitCompass( <div style='color:#008080; display:inline-block'>MicroBitI2C  &</div> _i2c,  <div style='color:#008080; display:inline-block'>MicroBitStorage  &</div> _storage)
#####Description
Constructor. Create a software representation of an e-compass.
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitI2C  &</div> *_i2c* - an instance of i2c, which the compass is accessible from.

>  <div style='color:#008080; display:inline-block'>MicroBitStorage  &</div> *_storage* - an instance of  MicroBitStorage , used to persist calibration data across resets.
#####Example
```cpp
 MicroBitI2C i2c(I2C_SDA0, I2C_SCL0); 
 
 MicroBitStorage storage; 
 
 MicroBitCompass compass(i2c, storage); 
```
<br/>
####MicroBitCompass( <div style='color:#008080; display:inline-block'>MicroBitI2C  &</div> _i2c,  <div style='color:#008080; display:inline-block'>MicroBitStorage  &</div> _storage,  <div style='color:#008080; display:inline-block'>uint16_t</div> address)
#####Description
Constructor. Create a software representation of an e-compass.
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitI2C  &</div> *_i2c* - an instance of i2c, which the compass is accessible from.

>  <div style='color:#008080; display:inline-block'>MicroBitStorage  &</div> *_storage* - an instance of  MicroBitStorage , used to persist calibration data across resets.

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *address* - the default address for the compass register on the i2c bus. Defaults to MAG3110_DEFAULT_ADDR.
#####Example
```cpp
 MicroBitI2C i2c(I2C_SDA0, I2C_SCL0); 
 
 MicroBitStorage storage; 
 
 MicroBitCompass compass(i2c, storage); 
```
<br/>
####MicroBitCompass( <div style='color:#008080; display:inline-block'>MicroBitI2C  &</div> _i2c,  <div style='color:#008080; display:inline-block'>MicroBitStorage  &</div> _storage,  <div style='color:#008080; display:inline-block'>uint16_t</div> address,  <div style='color:#008080; display:inline-block'>uint16_t</div> id)
#####Description
Constructor. Create a software representation of an e-compass.
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitI2C  &</div> *_i2c* - an instance of i2c, which the compass is accessible from.

>  <div style='color:#008080; display:inline-block'>MicroBitStorage  &</div> *_storage* - an instance of  MicroBitStorage , used to persist calibration data across resets.

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *address* - the default address for the compass register on the i2c bus. Defaults to MAG3110_DEFAULT_ADDR.

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *id* - the ID of the new  MicroBitCompass  object. Defaults to MAG3110_DEFAULT_ADDR.
#####Example
```cpp
 MicroBitI2C i2c(I2C_SDA0, I2C_SCL0); 
 
 MicroBitStorage storage; 
 
 MicroBitCompass compass(i2c, storage); 
```
<br/>
####MicroBitCompass( <div style='color:#008080; display:inline-block'>MicroBitI2C  &</div> _i2c)
#####Description
Constructor. Create a software representation of an e-compass.
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitI2C  &</div> *_i2c* - an instance of i2c, which the compass is accessible from.
#####Example
```cpp
 MicroBitI2C i2c(I2C_SDA0, I2C_SCL0); 
 
 MicroBitCompass compass(i2c); 
```
<br/>
####MicroBitCompass( <div style='color:#008080; display:inline-block'>MicroBitI2C  &</div> _i2c,  <div style='color:#008080; display:inline-block'>uint16_t</div> address)
#####Description
Constructor. Create a software representation of an e-compass.
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitI2C  &</div> *_i2c* - an instance of i2c, which the compass is accessible from.

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *address* - the default address for the compass register on the i2c bus. Defaults to MAG3110_DEFAULT_ADDR.
#####Example
```cpp
 MicroBitI2C i2c(I2C_SDA0, I2C_SCL0); 
 
 MicroBitCompass compass(i2c); 
```
<br/>
####MicroBitCompass( <div style='color:#008080; display:inline-block'>MicroBitI2C  &</div> _i2c,  <div style='color:#008080; display:inline-block'>uint16_t</div> address,  <div style='color:#008080; display:inline-block'>uint16_t</div> id)
#####Description
Constructor. Create a software representation of an e-compass.
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitI2C  &</div> *_i2c* - an instance of i2c, which the compass is accessible from.

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *address* - the default address for the compass register on the i2c bus. Defaults to MAG3110_DEFAULT_ADDR.

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *id* - the ID of the new  MicroBitCompass  object. Defaults to MAG3110_DEFAULT_ADDR.
#####Example
```cpp
 MicroBitI2C i2c(I2C_SDA0, I2C_SCL0); 
 
 MicroBitCompass compass(i2c); 
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
Attempts to set the sample rate of the compass to the specified value (in ms).
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *period* - the requested time between samples, in milliseconds.
#####Returns
MICROBIT_OK or MICROBIT_I2C_ERROR if the magnetometer could not be updated.
#####Example
```cpp
 // sample rate is now 20 ms. 
 compass.setPeriod(20); 
```

!!! note
    The requested rate may not be possible on the hardware. In this case, the nearest lower rate is chosen. 

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
Gets the current heading of the device, relative to magnetic north.
#####Returns
the current heading, in degrees. Or MICROBIT_CALIBRATION_IN_PROGRESS if the compass is calibrating.
#####Example
```cpp
 compass.heading(); 
```
##whoAmI
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> whoAmI()
#####Description
Attempts to read the 8 bit ID from the magnetometer, this can be used for validation purposes.
#####Returns
the 8 bit ID returned by the magnetometer, or MICROBIT_I2C_ERROR if the request fails.
#####Example
```cpp
 compass.whoAmI(); 
```
##getX
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getX()
#####Description
Reads the value of the X axis from the latest update retrieved from the magnetometer.
#####Returns
The magnetic force measured in the X axis, in nano teslas.
#####Example
```cpp
 compass.getX(); 
```
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getX( <div style='color:#008080; display:inline-block'>MicroBitCoordinateSystem</div> system)
#####Description
Reads the value of the X axis from the latest update retrieved from the magnetometer.
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitCoordinateSystem</div> *system* - The coordinate system to use. By default, a simple cartesian system is provided.
#####Returns
The magnetic force measured in the X axis, in nano teslas.
#####Example
```cpp
 compass.getX(); 
```
##getY
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getY()
#####Description
Reads the value of the Y axis from the latest update retrieved from the magnetometer.
#####Returns
The magnetic force measured in the Y axis, in nano teslas.
#####Example
```cpp
 compass.getY(); 
```
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getY( <div style='color:#008080; display:inline-block'>MicroBitCoordinateSystem</div> system)
#####Description
Reads the value of the Y axis from the latest update retrieved from the magnetometer.
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitCoordinateSystem</div> *system* - The coordinate system to use. By default, a simple cartesian system is provided.
#####Returns
The magnetic force measured in the Y axis, in nano teslas.
#####Example
```cpp
 compass.getY(); 
```
##getZ
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getZ()
#####Description
Reads the value of the Z axis from the latest update retrieved from the magnetometer.
#####Returns
The magnetic force measured in the Z axis, in nano teslas.
#####Example
```cpp
 compass.getZ(); 
```
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getZ( <div style='color:#008080; display:inline-block'>MicroBitCoordinateSystem</div> system)
#####Description
Reads the value of the Z axis from the latest update retrieved from the magnetometer.
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitCoordinateSystem</div> *system* - The coordinate system to use. By default, a simple cartesian system is provided.
#####Returns
The magnetic force measured in the Z axis, in nano teslas.
#####Example
```cpp
 compass.getZ(); 
```
##getFieldStrength
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getFieldStrength()
#####Description
Determines the overall magnetic field strength based on the latest update from the magnetometer.
#####Returns
The magnetic force measured across all axis, in nano teslas.
#####Example
```cpp
 compass.getFieldStrength(); 
```
##readTemperature
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> readTemperature()
#####Description
Reads the current die temperature of the compass.
#####Returns
the temperature in degrees celsius, or MICROBIT_I2C_ERROR if the temperature reading could not be retreived from the accelerometer. 
##calibrate
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> calibrate()
#####Description
Perform a calibration of the compass.
#####Returns
MICROBIT_OK, MICROBIT_I2C_ERROR if the magnetometer could not be accessed, or MICROBIT_CALIBRATION_REQUIRED if the calibration algorithm failed to complete successfully.

!!! note
    THIS MUST BE CALLED TO GAIN RELIABLE VALUES FROM THE COMPASS 

##setCalibration
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> setCalibration( <div style='color:#008080; display:inline-block'>CompassSample</div> calibration)
#####Description
Configure the compass to use the calibration data that is supplied to this call.
#####Parameters

>  <div style='color:#008080; display:inline-block'>CompassSample</div> *calibration* - A  CompassSample  containing the offsets for the x, y and z axis. 
##getCalibration
<br/>
####<div style='color:#FF69B4; display:inline-block'>CompassSample</div> getCalibration()
#####Description
Provides the calibration data currently in use by the compass.
#####Returns
calibration A  CompassSample  containing the offsets for the x, y and z axis. 
##updateSample
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> updateSample()
#####Description
Updates the local sample, only if the compass indicates that data is stale.

!!! note
    Can be used to trigger manual updates, if the device is running without a scheduler. Also called internally by all get[X,Y,Z]() member functions. 

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
____
[comment]: <> ({"end":"MicroBitCompass"})
