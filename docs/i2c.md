#uBit.i2c

##Overview

##Message Bus ID

##Message Bus Events

##API
[comment]: <> ({"className":"MicroBitI2C"})
____
##Constructor
<br/>
####MicroBitI2C( <div style='color:#008080; display:inline-block'>PinName</div> sda,  <div style='color:#008080; display:inline-block'>PinName</div> scl)
<br/>
#####Description
Constructor. Create an instance of i2c
                

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>PinName</div> *sda* - the Pin to be used for SDA 

>  <div style='color:#008080; display:inline-block'>PinName</div> *scl* - the Pin to be used for SCL Example:
                                 
                                     
                                         MicroBitI2C i2c(MICROBIT_PIN_SDA, MICROBIT_PIN_SCL); 
                                     
                                 
                            

<br/><br/>

!!! note
    this should prevent i2c lockups as well. 
<br/><br/>
____
##read
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> read( <div style='color:#008080; display:inline-block'>int</div> address,  <div style='color:#008080; display:inline-block'>char *</div> data,  <div style='color:#008080; display:inline-block'>int</div> length)
<br/>
#####Description
Performs a complete read transaction. The bottom bit of the address is forced to 1 to indicate a read.

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *address*

>  <div style='color:#008080; display:inline-block'>char *</div> *data*

>  <div style='color:#008080; display:inline-block'>int</div> *length*

<br/><br/>
#####Returns
MICROBIT_OK on success, MICROBIT_I2C_ERROR if an unresolved read failure is detected. 

<br/><br/>
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> read( <div style='color:#008080; display:inline-block'>int</div> address,  <div style='color:#008080; display:inline-block'>char *</div> data,  <div style='color:#008080; display:inline-block'>int</div> length,  <div style='color:#008080; display:inline-block'>bool</div> repeated)
<br/>
#####Description
Performs a complete read transaction. The bottom bit of the address is forced to 1 to indicate a read.

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *address*

>  <div style='color:#008080; display:inline-block'>char *</div> *data*

>  <div style='color:#008080; display:inline-block'>int</div> *length*

>  <div style='color:#008080; display:inline-block'>bool</div> *repeated*

<br/><br/>
#####Returns
MICROBIT_OK on success, MICROBIT_I2C_ERROR if an unresolved read failure is detected. 

<br/><br/>
____
##write
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> write( <div style='color:#008080; display:inline-block'>int</div> address,  <div style='color:#008080; display:inline-block'>const char *</div> data,  <div style='color:#008080; display:inline-block'>int</div> length)
<br/>
#####Description
Performs a complete write transaction. The bottom bit of the address is forced to 0 to indicate a write.

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *address*

>  <div style='color:#008080; display:inline-block'>const char *</div> *data*

>  <div style='color:#008080; display:inline-block'>int</div> *length*

<br/><br/>
#####Returns
MICROBIT_OK on success, MICROBIT_I2C_ERROR if an unresolved write failure is detected. 

<br/><br/>
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> write( <div style='color:#008080; display:inline-block'>int</div> address,  <div style='color:#008080; display:inline-block'>const char *</div> data,  <div style='color:#008080; display:inline-block'>int</div> length,  <div style='color:#008080; display:inline-block'>bool</div> repeated)
<br/>
#####Description
Performs a complete write transaction. The bottom bit of the address is forced to 0 to indicate a write.

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *address*

>  <div style='color:#008080; display:inline-block'>const char *</div> *data*

>  <div style='color:#008080; display:inline-block'>int</div> *length*

>  <div style='color:#008080; display:inline-block'>bool</div> *repeated*

<br/><br/>
#####Returns
MICROBIT_OK on success, MICROBIT_I2C_ERROR if an unresolved write failure is detected. 

<br/><br/>
____
[comment]: <> ({"end":"MicroBitI2C"})
