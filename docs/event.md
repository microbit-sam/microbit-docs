#MicroBitEvent

##Overview

##Message Bus ID

##Message Bus Events

#API
[comment]: <> ({"className":"MicroBitEvent"})
##Constructor
<br/>
####MicroBitEvent( <div style='color:#008080; display:inline-block'>uint16_t</div> source,  <div style='color:#008080; display:inline-block'>uint16_t</div> value)
#####Description
Constructor.  MicroBit MicroBitEvent MicroBitEvent MicroBitMessageBus MicroBitEvent
#####Parameters

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *source*

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *value* - Component specific code indicating the cause of the event. 
#####Example
```c++
 MicrobitEvent evt(id,MICROBIT_BUTTON_EVT_CLICK); 

```
<br/>
####MicroBitEvent( <div style='color:#008080; display:inline-block'>uint16_t</div> source,  <div style='color:#008080; display:inline-block'>uint16_t</div> value,  <div style='color:#008080; display:inline-block'>MicroBitEventLaunchMode</div> mode)
#####Description
Constructor.  MicroBit MicroBitEvent MicroBitEvent MicroBitMessageBus MicroBitEvent
#####Parameters

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *source*

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *value* - Component specific code indicating the cause of the event. 

>  <div style='color:#008080; display:inline-block'>MicroBitEventLaunchMode</div> *mode* - optional definition of how the event should be processed after construction (if at all):
#####Example
```c++
 MicrobitEvent evt(id,MICROBIT_BUTTON_EVT_CLICK); 

```
<br/>
####MicroBitEvent()
#####Description
Default constructor - initialises all values, and sets timestamp to the current time. 
##fire
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> fire()
#####Description
Fires the represented event onto the message bus using the default configuration.
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> fire( <div style='color:#008080; display:inline-block'>MicroBitEventLaunchMode</div> mode)
#####Description
Fires the represented event onto the message bus. 
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitEventLaunchMode</div> *mode* - Configuration of how the event is processed.
____
[comment]: <> ({"end":"MicroBitEvent"})
