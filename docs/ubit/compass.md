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

The micro:bit uses the NXP [MAG3110](../resources/datasheets/MAG3110.pdf).

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
####MicroBitCompass( <div style='color:#a71d5d; display:inline-block'>CoordinateSpace  &</div> coordinateSpace)
#####Description
Constructor. Create a software abstraction of an e-compass.  

   
 
 id 
 
 
 the unique  EventModel  id of this component. Defaults to: MICROBIT_ID_COMPASS   
 
 
 
 coordinateSpace 
 
 
 the orientation of the sensor. Defaults to: SIMPLE_CARTESIAN   
 
 
          


#####Parameters

>  <div style='color:#a71d5d; display:inline-block'>CoordinateSpace  &</div> coordinateSpace - the orientation of the sensor. Defaults to: SIMPLE_CARTESIAN 
<br/>
####MicroBitCompass( <div style='color:#a71d5d; display:inline-block'>CoordinateSpace  &</div> coordinateSpace,  <div style='color:#a71d5d; display:inline-block'>uint16_t</div> id)
#####Description
Constructor. Create a software abstraction of an e-compass.  

   
 
 id 
 
 
 the unique  EventModel  id of this component. Defaults to: MICROBIT_ID_COMPASS   
 
 
 
 coordinateSpace 
 
 
 the orientation of the sensor. Defaults to: SIMPLE_CARTESIAN   
 
 
          


#####Parameters

>  <div style='color:#a71d5d; display:inline-block'>CoordinateSpace  &</div> coordinateSpace - the orientation of the sensor. Defaults to: SIMPLE_CARTESIAN 

>  <div style='color:#a71d5d; display:inline-block'>uint16_t</div> id - the unique  EventModel  id of this component. Defaults to: MICROBIT_ID_COMPASS 
<br/>
####MicroBitCompass( <div style='color:#a71d5d; display:inline-block'>MicroBitAccelerometer  &</div> accel,  <div style='color:#a71d5d; display:inline-block'>CoordinateSpace  &</div> coordinateSpace)
#####Description
Constructor. Create a software abstraction of an e-compass.  

   
 
 id 
 
 
 the unique  EventModel  id of this component. Defaults to: MICROBIT_ID_COMPASS   
 
 
 
 accel 
 
 
 the accelerometer to use for tilt compensation   
 
 
 
 coordinateSpace 
 
 
 the orientation of the sensor. Defaults to: SIMPLE_CARTESIAN   
 
 
          


#####Parameters

>  <div style='color:#a71d5d; display:inline-block'>MicroBitAccelerometer  &</div> accel - the accelerometer to use for tilt compensation 

>  <div style='color:#a71d5d; display:inline-block'>CoordinateSpace  &</div> coordinateSpace - the orientation of the sensor. Defaults to: SIMPLE_CARTESIAN 
<br/>
####MicroBitCompass( <div style='color:#a71d5d; display:inline-block'>MicroBitAccelerometer  &</div> accel,  <div style='color:#a71d5d; display:inline-block'>CoordinateSpace  &</div> coordinateSpace,  <div style='color:#a71d5d; display:inline-block'>uint16_t</div> id)
#####Description
Constructor. Create a software abstraction of an e-compass.  

   
 
 id 
 
 
 the unique  EventModel  id of this component. Defaults to: MICROBIT_ID_COMPASS   
 
 
 
 accel 
 
 
 the accelerometer to use for tilt compensation   
 
 
 
 coordinateSpace 
 
 
 the orientation of the sensor. Defaults to: SIMPLE_CARTESIAN   
 
 
          


#####Parameters

>  <div style='color:#a71d5d; display:inline-block'>MicroBitAccelerometer  &</div> accel - the accelerometer to use for tilt compensation 

>  <div style='color:#a71d5d; display:inline-block'>CoordinateSpace  &</div> coordinateSpace - the orientation of the sensor. Defaults to: SIMPLE_CARTESIAN 

>  <div style='color:#a71d5d; display:inline-block'>uint16_t</div> id - the unique  EventModel  id of this component. Defaults to: MICROBIT_ID_COMPASS 
##heading
<br/>
####<div style='color:#a71d5d; display:inline-block'>int</div> <div style='color:#795da3; display:inline-block'>heading</div>()
#####Description
Gets the current heading of the device, relative to magnetic north.  

 If the compass is not calibrated, it will raise the COMPASS_EVT_CALIBRATE event.  

 Users wishing to implement their own calibration algorithms should listen for this event, using MESSAGE_BUS_LISTENER_IMMEDIATE model. This ensures that calibration is complete before the user program continues.  

 


#####Returns
the current heading, in degrees. Or CALIBRATION_IN_PROGRESS if the compass is calibrating.
#####Example
```cpp
 compass.heading(); 
```
##getFieldStrength
<br/>
####<div style='color:#a71d5d; display:inline-block'>int</div> <div style='color:#795da3; display:inline-block'>getFieldStrength</div>()
#####Description
Determines the overall magnetic field strength based on the latest update from the magnetometer.  

 


#####Returns
The magnetic force measured across all axis, in nano teslas.
#####Example
```cpp
 compass.getFieldStrength(); 
```
##calibrate
<br/>
####<div style='color:#a71d5d; display:inline-block'>int</div> <div style='color:#795da3; display:inline-block'>calibrate</div>()
#####Description
Perform a calibration of the compass.  

 This method will be called automatically if a user attempts to read a compass value when the compass is uncalibrated. It can also be called at any time by the user.  

 The method will only return once the compass has been calibrated.  

 


#####Returns
MICROBIT_OK, MICROBIT_I2C_ERROR if the magnetometer could not be accessed, or MICROBIT_CALIBRATION_REQUIRED if the calibration algorithm failed to complete successfully.

!!! note
    THIS MUST BE CALLED TO GAIN RELIABLE VALUES FROM THE COMPASS 

##setCalibration
<br/>
####<div style='color:#a71d5d; display:inline-block'>void</div> <div style='color:#795da3; display:inline-block'>setCalibration</div>( <div style='color:#a71d5d; display:inline-block'>CompassCalibration</div> calibration)
#####Description
Configure the compass to use the calibration data that is supplied to this call.  

 Calibration data is comprised of the perceived zero offset of each axis of the compass.  

 After calibration this should now take into account trimming errors in the magnetometer, and any "hard iron" offsets on the device.  

   
 
 calibration 
 
 
 A  Sample3D  containing the offsets for the x, y and z axis.   
 
 
          


#####Parameters

>  <div style='color:#a71d5d; display:inline-block'>CompassCalibration</div> calibration - A  Sample3D  containing the offsets for the x, y and z axis. 
##getCalibration
<br/>
####<div style='color:#a71d5d; display:inline-block'>CompassCalibration</div> <div style='color:#795da3; display:inline-block'>getCalibration</div>()
#####Description
Provides the calibration data currently in use by the compass.  

 More specifically, the x, y and z zero offsets of the compass.  

 


#####Returns
A  Sample3D  containing the offsets for the x, y and z axis. 
##isCalibrated
<br/>
####<div style='color:#a71d5d; display:inline-block'>int</div> <div style='color:#795da3; display:inline-block'>isCalibrated</div>()
#####Description
Returns 0 or 1. 1 indicates that the compass is calibrated, zero means the compass requires calibration.           


##isCalibrating
<br/>
####<div style='color:#a71d5d; display:inline-block'>int</div> <div style='color:#795da3; display:inline-block'>isCalibrating</div>()
#####Description
Returns 0 or 1. 1 indicates that the compass is calibrating, zero means the compass is not currently calibrating.           


##clearCalibration
<br/>
####<div style='color:#a71d5d; display:inline-block'>void</div> <div style='color:#795da3; display:inline-block'>clearCalibration</div>()
#####Description
Clears the calibration held in persistent storage, and sets the calibrated flag to zero.           


##configure
<br/>
####<div style='color:#a71d5d; display:inline-block'>int</div> <div style='color:#795da3; display:inline-block'>configure</div>()
#####Description
Configures the device for the sample rate defined in this object. The nearest values are chosen to those defined that are supported by the hardware. The instance variables are then updated to reflect reality.  

 


#####Returns
MICROBIT_OK on success, MICROBIT_I2C_ERROR if the compass could not be configured. 
##setAccelerometer
<br/>
####<div style='color:#a71d5d; display:inline-block'>void</div> <div style='color:#795da3; display:inline-block'>setAccelerometer</div>( <div style='color:#a71d5d; display:inline-block'>MicroBitAccelerometer  &</div> accelerometer)
#####Description
Defines the accelerometer to be used for tilt compensation.  

   
 
 acceleromter 
 
 
 Reference to the accelerometer to use.   
 
 
          


#####Parameters

>  <div style='color:#a71d5d; display:inline-block'>MicroBitAccelerometer  &</div> accelerometer
##setPeriod
<br/>
####<div style='color:#a71d5d; display:inline-block'>int</div> <div style='color:#795da3; display:inline-block'>setPeriod</div>( <div style='color:#a71d5d; display:inline-block'>int</div> period)
#####Description
Attempts to set the sample rate of the compass to the specified period value (in ms).  

 


#####Parameters

>  <div style='color:#a71d5d; display:inline-block'>int</div> period - the requested time between samples, in milliseconds. 
#####Returns
MICROBIT_OK on success, MICROBIT_I2C_ERROR is the request fails.

!!! note
    The requested rate may not be possible on the hardware. In this case, the nearest lower rate is chosen.

##getPeriod
<br/>
####<div style='color:#a71d5d; display:inline-block'>int</div> <div style='color:#795da3; display:inline-block'>getPeriod</div>()
#####Description
Reads the currently configured sample rate of the compass.  

 


#####Returns
The time between samples, in milliseconds. 
##requestUpdate
<br/>
####<div style='color:#a71d5d; display:inline-block'>int</div> <div style='color:#795da3; display:inline-block'>requestUpdate</div>()
#####Description
Poll to see if new data is available from the hardware. If so, update it. n.b. it is not necessary to explicitly call this funciton to update data (it normally happens in the background when the scheduler is idle), but a check is performed if the user explicitly requests up to date data.  

 


#####Returns
MICROBIT_OK on success, MICROBIT_I2C_ERROR if the update fails.

!!! note
    This method should be overidden by the hardware driver to implement the requested changes in hardware. 

##update
<br/>
####<div style='color:#a71d5d; display:inline-block'>int</div> <div style='color:#795da3; display:inline-block'>update</div>()
#####Description
Stores data from the compass sensor in our buffer.  

 On first use, this member function will attempt to add this component to the list of fiber components in order to constantly update the values stored by this object.  

 This lazy instantiation means that we do not obtain the overhead from non-chalantly adding this component to fiber components.  

 


#####Returns
MICROBIT_OK on success, MICROBIT_I2C_ERROR if the read request fails. 
##getSample
<br/>
####<div style='color:#a71d5d; display:inline-block'>Sample3D</div> <div style='color:#795da3; display:inline-block'>getSample</div>( <div style='color:#a71d5d; display:inline-block'>CoordinateSystem</div> coordinateSystem)
#####Description
Reads the last compass value stored, and provides it in the coordinate system requested.  

 


#####Parameters

>  <div style='color:#a71d5d; display:inline-block'>CoordinateSystem</div> coordinateSystem
#####Returns
The force measured in each axis, in milli-g. 
<br/>
####<div style='color:#a71d5d; display:inline-block'>Sample3D</div> <div style='color:#795da3; display:inline-block'>getSample</div>()
#####Description



#####Returns
The force measured in each axis, in milli-g. 
##getX
<br/>
####<div style='color:#a71d5d; display:inline-block'>int</div> <div style='color:#795da3; display:inline-block'>getX</div>()
#####Description
reads the value of the x axis from the latest update retrieved from the compass, using the default coordinate system as specified in the constructor.  

 


#####Returns
the force measured in the x axis, in milli-g. 
##getY
<br/>
####<div style='color:#a71d5d; display:inline-block'>int</div> <div style='color:#795da3; display:inline-block'>getY</div>()
#####Description
reads the value of the y axis from the latest update retrieved from the compass, using the default coordinate system as specified in the constructor.  

 


#####Returns
the force measured in the y axis, in milli-g. 
##getZ
<br/>
####<div style='color:#a71d5d; display:inline-block'>int</div> <div style='color:#795da3; display:inline-block'>getZ</div>()
#####Description
reads the value of the z axis from the latest update retrieved from the compass, using the default coordinate system as specified in the constructor.  

 


#####Returns
the force measured in the z axis, in milli-g. 
##updateSample
<br/>
####<div style='color:#a71d5d; display:inline-block'>void</div> <div style='color:#795da3; display:inline-block'>updateSample</div>()
#####Description
 updateSample()  method maintained here as an inline method purely for backward compatibility.           


____
[comment]: <> ({"end":"MicroBitCompass"})
