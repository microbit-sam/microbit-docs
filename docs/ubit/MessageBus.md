#uBit.messageBus

##Overview

##Message Bus ID

##Message Bus Events

##API
[comment]: <> ({"className":"MicroBitMessageBus"})
##Constructor
<br/>
####MicroBitMessageBus()
#####Description
Default constructor. Anticipating only one MessageBus per device, as filtering is handled within the class. 
##send
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> send( <div style='color:#008080; display:inline-block'>MicroBitEvent</div> evt)
#####Description
Queues the given event to be sent to all registered recipients.
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitEvent</div> *evt*
#####Example
```cpp
 MicroBitEvent evt(id,MICROBIT_BUTTON_EVT_DOWN,ticks,false); 
 evt.fire(); 
 //OR YOU CAN DO THIS... 
 MicroBitEvent evt(id,MICROBIT_BUTTON_EVT_DOWN); 

```
##process
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> process( <div style='color:#008080; display:inline-block'>MicroBitEvent  &</div> evt)
#####Description
Internal function, used to deliver the given event to all relevant recipients. Normally, this is called once an event has been removed from the event queue.
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitEvent  &</div> *evt* - The event to send. 
#####Returns
1 if all matching listeners were processed, 0 if further processing is required. 
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> process( <div style='color:#008080; display:inline-block'>MicroBitEvent  &</div> evt,  <div style='color:#008080; display:inline-block'>bool</div> urgent)
#####Description
Internal function, used to deliver the given event to all relevant recipients. Normally, this is called once an event has been removed from the event queue.
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitEvent  &</div> *evt* - The event to send. 

>  <div style='color:#008080; display:inline-block'>bool</div> *urgent* - The type of listeners to process (optional). If set to true, only listeners defined as urgent and non-blocking will be processed otherwise, all other (standard) listeners will be processed. 
#####Returns
1 if all matching listeners were processed, 0 if further processing is required. 
##elementAt
<br/>
####<div style='color:#FF69B4; display:inline-block'>MicroBitListener</div> elementAt( <div style='color:#008080; display:inline-block'>int</div> n)
#####Description
Returns the microBitListener with the given position in our list.  MicroBitListener
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *n* - The position in the list to return. 
#####Returns
the  MicroBitListener  at postion n in the list, or NULL if the position is invalid. 
##add
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> add( <div style='color:#008080; display:inline-block'>MicroBitListener  *</div> newListener)
#####Description
Add the given  MicroBitListener MicroBitListener
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitListener  *</div> *newListener*
#####Returns
MICROBIT_OK if the listener is valid, MICROBIT_INVALID_PARAMETER otherwise. 
##remove
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> remove( <div style='color:#008080; display:inline-block'>MicroBitListener  *</div> newListener)
#####Description
Remove the given  MicroBitListener MicroBitListener
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitListener  *</div> *newListener*
#####Returns
MICROBIT_OK if the listener is valid, MICROBIT_INVALID_PARAMETER otherwise. 
____
[comment]: <> ({"end":"MicroBitMessageBus"})
