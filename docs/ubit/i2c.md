#uBit.i2c

##Overview

i2c is a very common, widely used protocol for communicating with other devices
over a wire. i2c uses a very simple addressing scheme to access these other
devices.

Onboard the micro:bit itself there are two components which use i2c bus as a communication
mechanism, the [accelerometer](accelerometer.md) and the [compass](compass.md).

As well as being used internally, the i2c bus is exposed on two edge connector
pins, P19 and P20. This means other accessories that use i2c to communicate
can be used in conjunction with the micro:bit.

##Message Bus ID

> None.

##Message Bus Events

> None.

##API
[comment]: <> ({"className":"MicroBitI2C"})
##Constructor
<br/>
####MicroBitI2C( <div style='color:#008080; display:inline-block'>PinName</div> sda,  <div style='color:#008080; display:inline-block'>PinName</div> scl)
#####Description
Constructor. Create an instance of i2c 
#####Parameters

>  <div style='color:#008080; display:inline-block'>PinName</div> *sda* - the Pin to be used for SDA 

>  <div style='color:#008080; display:inline-block'>PinName</div> *scl* - the Pin to be used for SCL Example:  MicroBitI2C i2c(MICROBIT_PIN_SDA, MICROBIT_PIN_SCL); 
  

!!! note
    this should prevent i2c lockups as well. 

##read
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> read( <div style='color:#008080; display:inline-block'>int</div> address,  <div style='color:#008080; display:inline-block'>char *</div> data,  <div style='color:#008080; display:inline-block'>int</div> length)
#####Description
Performs a complete read transaction. The bottom bit of the address is forced to 1 to indicate a read.
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *address*

>  <div style='color:#008080; display:inline-block'>char *</div> *data*

>  <div style='color:#008080; display:inline-block'>int</div> *length*
#####Returns
MICROBIT_OK on success, MICROBIT_I2C_ERROR if an unresolved read failure is detected. 
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> read( <div style='color:#008080; display:inline-block'>int</div> address,  <div style='color:#008080; display:inline-block'>char *</div> data,  <div style='color:#008080; display:inline-block'>int</div> length,  <div style='color:#008080; display:inline-block'>bool</div> repeated)
#####Description
Performs a complete read transaction. The bottom bit of the address is forced to 1 to indicate a read.
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *address*

>  <div style='color:#008080; display:inline-block'>char *</div> *data*

>  <div style='color:#008080; display:inline-block'>int</div> *length*

>  <div style='color:#008080; display:inline-block'>bool</div> *repeated*
#####Returns
MICROBIT_OK on success, MICROBIT_I2C_ERROR if an unresolved read failure is detected. 
##write
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> write( <div style='color:#008080; display:inline-block'>int</div> address,  <div style='color:#008080; display:inline-block'>const char *</div> data,  <div style='color:#008080; display:inline-block'>int</div> length)
#####Description
Performs a complete write transaction. The bottom bit of the address is forced to 0 to indicate a write.
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *address*

>  <div style='color:#008080; display:inline-block'>const char *</div> *data*

>  <div style='color:#008080; display:inline-block'>int</div> *length*
#####Returns
MICROBIT_OK on success, MICROBIT_I2C_ERROR if an unresolved write failure is detected. 
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> write( <div style='color:#008080; display:inline-block'>int</div> address,  <div style='color:#008080; display:inline-block'>const char *</div> data,  <div style='color:#008080; display:inline-block'>int</div> length,  <div style='color:#008080; display:inline-block'>bool</div> repeated)
#####Description
Performs a complete write transaction. The bottom bit of the address is forced to 0 to indicate a write.
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *address*

>  <div style='color:#008080; display:inline-block'>const char *</div> *data*

>  <div style='color:#008080; display:inline-block'>int</div> *length*

>  <div style='color:#008080; display:inline-block'>bool</div> *repeated*
#####Returns
MICROBIT_OK on success, MICROBIT_I2C_ERROR if an unresolved write failure is detected. 
____
[comment]: <> ({"end":"MicroBitI2C"})
