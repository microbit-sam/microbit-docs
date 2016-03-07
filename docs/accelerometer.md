#uBit.accelerometer

##Overview

##Message Bus ID

##Message Bus Events

##API
[comment]: <> ({"className":"MicroBitAccelerometer"})
____
##Constructor
<br/>
####MicroBitAccelerometer( <div style='color:#008080; display:inline-block'>uint16_t</div> id,  <div style='color:#008080; display:inline-block'>uint16_t</div> address)
<br/>
#####Description
Constructor. Create an accelerometer representation with the given ID. 

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *id* - the ID of the new object. 

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *address* - the default base address of the accelerometer.

<br/><br/>
#####Example
```c++
accelerometer(MICROBIT_ID_ACCELEROMETER,MMA8653_DEFAULT_ADDR)

```

<br/><br/>
____
##configure
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> configure()
<br/>
#####Description
Configures the accelerometer for G range and sample rate defined in this object. The nearest values are chosen to those defined that are supported by the hardware. The instance variables are then updated to reflect reality.

<br/><br/>
#####Returns
MICROBIT_OK on success, MICROBIT_I2C_ERROR if the accelerometer could not be configured.

<br/><br/>
____
##update
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> update()
<br/>
#####Description
Reads the acceleration data from the accelerometer, and stores it in our buffer. This is called by the tick() member function, if the interrupt is set.

<br/><br/>
#####Returns
MICROBIT_OK on success, MICROBIT_I2C_ERROR is the read request fails.

<br/><br/>
____
##setPeriod
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> setPeriod( <div style='color:#008080; display:inline-block'>int</div> period)
<br/>
#####Description
Attempts to set the sample rate of the accelerometer to the specified value (in ms). n.b. the requested rate may not be possible on the hardware. In this case, the nearest lower rate is chosen. 

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *period* - the requested time between samples, in milliseconds. 

<br/><br/>
#####Returns
MICROBIT_OK on success, MICROBIT_I2C_ERROR is the request fails. 

<br/><br/>
____
##getPeriod
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getPeriod()
<br/>
#####Description
Reads the currently configured sample rate of the accelerometer. 

<br/><br/>
#####Returns
The time between samples, in milliseconds. 

<br/><br/>
____
##setRange
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> setRange( <div style='color:#008080; display:inline-block'>int</div> range)
<br/>
#####Description
Attempts to set the sample range of the accelerometer to the specified value (in g). n.b. the requested range may not be possible on the hardware. In this case, the nearest lower rate is chosen. 

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *range* - The requested sample range of samples, in g. 

<br/><br/>
#####Returns
MICROBIT_OK on success, MICROBIT_I2C_ERROR is the request fails. 

<br/><br/>
____
##getRange
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getRange()
<br/>
#####Description
Reads the currently configured sample range of the accelerometer. 

<br/><br/>
#####Returns
The sample range, in g. 

<br/><br/>
____
##whoAmI
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> whoAmI()
<br/>
#####Description
Attempts to determine the 8 bit ID from the accelerometer. 

<br/><br/>
#####Returns
the 8 bit ID returned by the accelerometer, or MICROBIT_I2C_ERROR if the request fails.

<br/><br/>
#####Example
```c++
uBit.accelerometer.whoAmI();

```

<br/><br/>
____
##getX
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getX()
<br/>
#####Description
Reads the X axis value of the latest update from the accelerometer. 

<br/><br/>
#####Returns
The force measured in the X axis, in milli-g.

<br/><br/>
#####Example
```c++
uBit.accelerometer.getX();

```

<br/><br/>
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getX( <div style='color:#008080; display:inline-block'>MicroBitCoordinateSystem</div> system)
<br/>
#####Description
Reads the X axis value of the latest update from the accelerometer. 

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitCoordinateSystem</div> *system* - The coordinate system to use. By default, a simple cartesian system is provided. 

<br/><br/>
#####Returns
The force measured in the X axis, in milli-g.

<br/><br/>
#####Example
```c++
uBit.accelerometer.getX();

```

<br/><br/>
____
##getY
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getY()
<br/>
#####Description
Reads the Y axis value of the latest update from the accelerometer. 

<br/><br/>
#####Returns
The force measured in the Y axis, in milli-g.

<br/><br/>
#####Example
```c++
uBit.accelerometer.getY();

```

<br/><br/>
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getY( <div style='color:#008080; display:inline-block'>MicroBitCoordinateSystem</div> system)
<br/>
#####Description
Reads the Y axis value of the latest update from the accelerometer. 

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitCoordinateSystem</div> *system* - The coordinate system to use. By default, a simple cartesian system is provided. 

<br/><br/>
#####Returns
The force measured in the Y axis, in milli-g.

<br/><br/>
#####Example
```c++
uBit.accelerometer.getY();

```

<br/><br/>
____
##getZ
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getZ()
<br/>
#####Description
Reads the Z axis value of the latest update from the accelerometer. 

<br/><br/>
#####Returns
The force measured in the Z axis, in milli-g.

<br/><br/>
#####Example
```c++
uBit.accelerometer.getZ();

```

<br/><br/>
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getZ( <div style='color:#008080; display:inline-block'>MicroBitCoordinateSystem</div> system)
<br/>
#####Description
Reads the Z axis value of the latest update from the accelerometer. 

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitCoordinateSystem</div> *system* - The coordinate system to use. By default, a simple cartesian system is provided. 

<br/><br/>
#####Returns
The force measured in the Z axis, in milli-g.

<br/><br/>
#####Example
```c++
uBit.accelerometer.getZ();

```

<br/><br/>
____
##getPitch
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getPitch()
<br/>
#####Description
Provides a rotation compensated pitch of the device, based on the latest update from the accelerometer. 

<br/><br/>
#####Returns
The pitch of the device, in degrees.

<br/><br/>
#####Example
```c++
uBit.accelerometer.getPitch();

```

<br/><br/>
____
##getPitchRadians
<br/>
####<div style='color:#FF69B4; display:inline-block'>float</div> getPitchRadians()
<br/>
____
##getRoll
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getRoll()
<br/>
#####Description
Provides a rotation compensated roll of the device, based on the latest update from the accelerometer. 

<br/><br/>
#####Returns
The roll of the device, in degrees.

<br/><br/>
#####Example
```c++
uBit.accelerometer.getRoll();

```

<br/><br/>
____
##getRollRadians
<br/>
####<div style='color:#FF69B4; display:inline-block'>float</div> getRollRadians()
<br/>
____
##getGesture
<br/>
####<div style='color:#FF69B4; display:inline-block'>BasicGesture</div> getGesture()
<br/>
#####Description
Reads the last recorded gesture detected. 

<br/><br/>
#####Returns
The last gesture detected.

<br/><br/>
#####Example
```c++
if(uBit.accelerometer.getGesture()==SHAKE)

```

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
##~MicroBitAccelerometer
<br/>
####~MicroBitAccelerometer()
<br/>
#####Description
Destructor for  MicroBitButton

<br/><br/>
____
[comment]: <> ({"end":"MicroBitAccelerometer"})
