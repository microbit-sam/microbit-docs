#Buttons

##Overview

The micro:bit has two forward facing buttons either side of the display, `buttonA`
and `buttonB`. These are intuitively exposed on the [`MicroBit`](../ubit.md) object as `uBit.buttonA`
and `uBit.buttonB`. A third button, `uBit.buttonAB` is used to detect the combined
input of `buttonA` and `buttonB`, and is an instance of the class [`MicroBitMultiButton`](multibutton.md).

Hardware buttons are notoriously renowned for generating multiple open/close transitions
for what a user perceives as a single press, which can make depending on the raw input
of a button unreliable. To combat this, a technique called 'debouncing' is used, which
periodically polls the state of the button, when a transition from open to close
(and vice versa) is detected. Through periodically polling the button, we get a
more accurate representation of the state of a button.

`MicroBitButton`s and [`MicroBitMultiButton`](multibutton.md)s are debounced in
software and provide a number of events that can be used to detect different
variations of presses.

The `MicroBitButton` debouncing mechanism is used to provide resistive touch sensing on [`MicroBitPin`](io.md)s
and could also be used on external 'button-like' input if required.

##Message Bus ID
| Constant | Value |
| ------------- |-------------|
| MICROBIT_ID_BUTTON_A | 1 |
| MICROBIT_ID_BUTTON_B | 2 |

##Message Bus Events

| Constant | Value |
| ------------- |-------------|
| MICROBIT_BUTTON_EVT_DOWN | 1 |
| MICROBIT_BUTTON_EVT_UP | 2 |
| MICROBIT_BUTTON_EVT_CLICK | 3 |
| MICROBIT_BUTTON_EVT_LONG_CLICK | 4 |
| MICROBIT_BUTTON_EVT_HOLD | 5 |
| MICROBIT_BUTTON_EVT_DOUBLE_CLICK | 6 |

##API
[comment]: <> ({"className":"MicroBitButton"})
##Constructor
<br/>
####MicroBitButton( <div style='color:#008080; display:inline-block'>PinName</div> name,  <div style='color:#008080; display:inline-block'>uint16_t</div> id)
#####Description
Constructor. Create a pin representation with the given ID.  MicroBitButton
#####Parameters

>  <div style='color:#008080; display:inline-block'>PinName</div> *name* - the physical pin on the processor that this butotn is connected to. 

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *id* - the ID of the new  MicroBitButton  object. 
#####Example
```cpp
 buttonA(MICROBIT_ID_BUTTON_A,MICROBIT_PIN_BUTTON_A); //a number between 0 and 200 inclusive 

```
<br/>
####MicroBitButton( <div style='color:#008080; display:inline-block'>PinName</div> name,  <div style='color:#008080; display:inline-block'>uint16_t</div> id,  <div style='color:#008080; display:inline-block'>MicroBitButtonEventConfiguration</div> eventConfiguration)
#####Description
Constructor. Create a pin representation with the given ID.  MicroBitButton
#####Parameters

>  <div style='color:#008080; display:inline-block'>PinName</div> *name* - the physical pin on the processor that this butotn is connected to. 

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *id* - the ID of the new  MicroBitButton  object. 

>  <div style='color:#008080; display:inline-block'>MicroBitButtonEventConfiguration</div> *eventConfiguration*
#####Example
```cpp
 buttonA(MICROBIT_ID_BUTTON_A,MICROBIT_PIN_BUTTON_A); //a number between 0 and 200 inclusive 

```
<br/>
####MicroBitButton( <div style='color:#008080; display:inline-block'>PinName</div> name,  <div style='color:#008080; display:inline-block'>uint16_t</div> id,  <div style='color:#008080; display:inline-block'>MicroBitButtonEventConfiguration</div> eventConfiguration,  <div style='color:#008080; display:inline-block'>PinMode</div> mode)
#####Description
Constructor. Create a pin representation with the given ID.  MicroBitButton
#####Parameters

>  <div style='color:#008080; display:inline-block'>PinName</div> *name* - the physical pin on the processor that this butotn is connected to. 

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *id* - the ID of the new  MicroBitButton  object. 

>  <div style='color:#008080; display:inline-block'>MicroBitButtonEventConfiguration</div> *eventConfiguration*

>  <div style='color:#008080; display:inline-block'>PinMode</div> *mode* - the configuration of internal pullups/pulldowns, as define in the mbed PinMode class. PullNone by default.
#####Example
```cpp
 buttonA(MICROBIT_ID_BUTTON_A,MICROBIT_PIN_BUTTON_A); //a number between 0 and 200 inclusive 

```
##isPressed
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> isPressed()
#####Description
Tests if this Button is currently pressed. 
#####Returns
1 if this button is pressed, 0 otherwise.
#####Example
```cpp
 if(uBit.buttonA.isPressed()) 
 print("Pressed!"); 

```
##setEventConfiguration
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> setEventConfiguration( <div style='color:#008080; display:inline-block'>MicroBitButtonEventConfiguration</div> config)
#####Description
Changes the event configuraiton of this button to the given value. All subsequent events generated by this button will then be informed by this configuraiton.
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitButtonEventConfiguration</div> *config* - The new configuration for this button. Legal values are MICROBIT_BUTTON_ALL_EVENTS or MICROBIT_BUTTON_SIMPLE_EVENTS.
#####Example
```cpp
 // Configure a button to generate all possible events. 
 uBit.buttonA.setEventConfiguration(MICROBIT_BUTTON_ALL_EVENTS); 
 
 // Configure a button to suppress MICROBIT_BUTTON_EVT_CLICK and MICROBIT_BUTTON_EVT_LONG_CLICK events. 
 uBit.buttonA.setEventConfiguration(MICROBIT_BUTTON_SIMPLE_EVENTS); 

```
____
[comment]: <> ({"end":"MicroBitButton"})
