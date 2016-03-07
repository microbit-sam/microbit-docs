#uBit.io

##Overview

##Message Bus ID

##Message Bus Events

#API
[comment]: <> ({"className":"MicroBitPin"})
____
##Constructor
<br/>
####MicroBitPin( <div style='color:#008080; display:inline-block'>int</div> id,  <div style='color:#008080; display:inline-block'>PinName</div> name,  <div style='color:#008080; display:inline-block'>PinCapability</div> capability)
<br/>
#####Description
Constructor. Create a Button representation with the given ID.  MicroBitPin

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *id* - the ID of the new Pin object. 

>  <div style='color:#008080; display:inline-block'>PinName</div> *name* - the pin name for this  MicroBitPin  instance to represent 

>  <div style='color:#008080; display:inline-block'>PinCapability</div> *capability* - the capability of this pin.

<br/><br/>
#####Example
```c++
MicroBitPinP0(MICROBIT_ID_IO_P0,MICROBIT_PIN_P0,PIN_CAPABILITY_BOTH);

```

<br/><br/>
____
##setDigitalValue
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> setDigitalValue( <div style='color:#008080; display:inline-block'>int</div> value)
<br/>
#####Description
Configures this IO pin as a digital output (if necessary) and sets the pin to 'value'. 

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *value* - 0 (LO) or 1 (HI) 

<br/><br/>
#####Returns
MICROBIT_OK on success, MICROBIT_INVALID_PARAMETER if value is out of range, or MICROBIT_NOT_SUPPORTED if the given pin does not have digital capability.

<br/><br/>
#####Example
```c++
MicroBitPinP0(MICROBIT_ID_IO_P0,MICROBIT_PIN_P0,PIN_CAPABILITY_BOTH);
P0.setDigitalValue(1);//P0isnowHI

```

<br/><br/>
____
##getDigitalValue
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getDigitalValue()
<br/>
#####Description
Configures this IO pin as a digital input (if necessary) and tests its current value. 

<br/><br/>
#####Returns
1 if this input is high, 0 if input is LO, or MICROBIT_NOT_SUPPORTED if the given pin does not have analog capability.

<br/><br/>
#####Example
```c++
MicroBitPinP0(MICROBIT_ID_IO_P0,MICROBIT_PIN_P0,PIN_CAPABILITY_BOTH);
P0.getDigitalValue();//P0iseither0or1;

```

<br/><br/>
____
##setAnalogValue
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> setAnalogValue( <div style='color:#008080; display:inline-block'>int</div> value)
<br/>
#####Description
Configures this IO pin as an analog/pwm output, and change the output value to the given level. 

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *value* - the level to set on the output pin, in the range 0 - 1024 

<br/><br/>
#####Returns
MICROBIT_OK on success, MICROBIT_INVALID_PARAMETER if value is out of range, or MICROBIT_NOT_SUPPORTED if the given pin does not have analog capability.

<br/><br/>
____
##setServoValue
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> setServoValue( <div style='color:#008080; display:inline-block'>int</div> value)
<br/>
#####Description
Configures this IO pin as an analog/pwm output if it isn't already, configures the period to be 20ms, and sets the duty cycle between 0.05 and 0.1 (i.e. 5% or 10%) based on the value given to this method.

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *value* - the level to set on the output pin, in the range 0 - 180 

<br/><br/>
#####Returns
MICROBIT_OK on success, MICROBIT_INVALID_PARAMETER if value is out of range, or MICROBIT_NOT_SUPPORTED if the given pin does not have analog capability. 

<br/><br/>
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> setServoValue( <div style='color:#008080; display:inline-block'>int</div> value,  <div style='color:#008080; display:inline-block'>int</div> range)
<br/>
#####Description
Configures this IO pin as an analog/pwm output if it isn't already, configures the period to be 20ms, and sets the duty cycle between 0.05 and 0.1 (i.e. 5% or 10%) based on the value given to this method.

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *value* - the level to set on the output pin, in the range 0 - 180 

>  <div style='color:#008080; display:inline-block'>int</div> *range* - which gives the span of possible values the i.e. lower and upper bounds center  range/2 (Defaults to: MICROBIT_PIN_DEFAULT_SERVO_RANGE) 

<br/><br/>
#####Returns
MICROBIT_OK on success, MICROBIT_INVALID_PARAMETER if value is out of range, or MICROBIT_NOT_SUPPORTED if the given pin does not have analog capability. 

<br/><br/>
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> setServoValue( <div style='color:#008080; display:inline-block'>int</div> value,  <div style='color:#008080; display:inline-block'>int</div> range,  <div style='color:#008080; display:inline-block'>int</div> center)
<br/>
#####Description
Configures this IO pin as an analog/pwm output if it isn't already, configures the period to be 20ms, and sets the duty cycle between 0.05 and 0.1 (i.e. 5% or 10%) based on the value given to this method.

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *value* - the level to set on the output pin, in the range 0 - 180 

>  <div style='color:#008080; display:inline-block'>int</div> *range* - which gives the span of possible values the i.e. lower and upper bounds center  range/2 (Defaults to: MICROBIT_PIN_DEFAULT_SERVO_RANGE) 

>  <div style='color:#008080; display:inline-block'>int</div> *center* - the center point from which to calculate the lower and upper bounds (Defaults to: MICROBIT_PIN_DEFAULT_SERVO_CENTER) 

<br/><br/>
#####Returns
MICROBIT_OK on success, MICROBIT_INVALID_PARAMETER if value is out of range, or MICROBIT_NOT_SUPPORTED if the given pin does not have analog capability. 

<br/><br/>
____
##getAnalogValue
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getAnalogValue()
<br/>
#####Description
Configures this IO pin as an analogue input (if necessary and possible). 

<br/><br/>
#####Returns
the current analogue level on the pin, in the range 0 - 1024, or MICROBIT_NOT_SUPPORTED if the given pin does not have analog capability.

<br/><br/>
#####Example
```c++
MicroBitPinP0(MICROBIT_ID_IO_P0,MICROBIT_PIN_P0,PIN_CAPABILITY_BOTH);
P0.getAnalogValue();//P0isavalueintherangeof0-1024

```

<br/><br/>
____
##isInput
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> isInput()
<br/>
#####Description
Determines if this IO pin is currently configured as an input. 

<br/><br/>
#####Returns
1 if pin is an analog or digital input, 0 otherwise. 

<br/><br/>
____
##isOutput
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> isOutput()
<br/>
#####Description
Determines if this IO pin is currently configured as an output. 

<br/><br/>
#####Returns
1 if pin is an analog or digital output, 0 otherwise. 

<br/><br/>
____
##isDigital
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> isDigital()
<br/>
#####Description
Determines if this IO pin is currently configured for digital use. 

<br/><br/>
#####Returns
1 if pin is digital, 0 otherwise. 

<br/><br/>
____
##isAnalog
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> isAnalog()
<br/>
#####Description
Determines if this IO pin is currently configured for analog use. 

<br/><br/>
#####Returns
1 if pin is analog, 0 otherwise. 

<br/><br/>
____
##isTouched
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> isTouched()
<br/>
#####Description
Configures this IO pin as a makey makey style touch sensor (if necessary) and tests its current debounced state. 

<br/><br/>
#####Returns
1 if pin is touched, 0 if not, or MICROBIT_NOT_SUPPORTED if this pin does not support touch capability.

<br/><br/>
#####Example
```c++
MicroBitPinP0(MICROBIT_ID_IO_P0,MICROBIT_PIN_P0,PIN_CAPABILITY_ALL);
if(P0.isTouched())
{
uBit.display.clear();
}

```

<br/><br/>
____
##setServoPulseUs
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> setServoPulseUs( <div style='color:#008080; display:inline-block'>int</div> pulseWidth)
<br/>
#####Description
Configures this IO pin as an analog/pwm output if it isn't already, configures the period to be 20ms, and sets the pulse width, based on the value it is given

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *pulseWidth* - the desired pulse width in microseconds. 

<br/><br/>
#####Returns
MICROBIT_OK on success, MICROBIT_INVALID_PARAMETER if value is out of range, or MICROBIT_NOT_SUPPORTED if the given pin does not have analog capability. 

<br/><br/>
____
##setAnalogPeriod
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> setAnalogPeriod( <div style='color:#008080; display:inline-block'>int</div> period)
<br/>
#####Description
Configures the PWM period of the analog output to the given value.

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *period* - The new period for the analog output in milliseconds. 

<br/><br/>
#####Returns
MICROBIT_OK on success, or MICROBIT_NOT_SUPPORTED if the given pin is not configured as an analog output.

<br/><br/>
____
##setAnalogPeriodUs
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> setAnalogPeriodUs( <div style='color:#008080; display:inline-block'>int</div> period)
<br/>
#####Description
Configures the PWM period of the analog output to the given value.

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *period* - The new period for the analog output in microseconds. 

<br/><br/>
#####Returns
MICROBIT_OK on success, or MICROBIT_NOT_SUPPORTED if the given pin is not configured as an analog output. 

<br/><br/>
____
##getAnalogPeriodUs
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getAnalogPeriodUs()
<br/>
#####Description
Retrieves the PWM period of the analog output.

<br/><br/>
#####Returns
the period on success, or MICROBIT_NOT_SUPPORTED if the given pin is not configured as an analog output. 

<br/><br/>
____
##getAnalogPeriod
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getAnalogPeriod()
<br/>
#####Description
Retrieves the PWM period of the analog output.

<br/><br/>
#####Returns
the period on success, or MICROBIT_NOT_SUPPORTED if the given pin is not configured as an analog output. 

<br/><br/>
____
[comment]: <> ({"end":"MicroBitPin"})
