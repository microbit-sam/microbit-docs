#uBit.MessageBus

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
####<div style='color:#FF69B4; display:inline-block'>void</div> send( <div style='color:#008080; display:inline-block'>MicroBitEvent</div> evt)
#####Description
Queues the given event to be sent to all registered recipients.
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitEvent</div> *evt*
#####Example
```c++
MicroBitEventevt(id,MICROBIT_BUTTON_EVT_DOWN,ticks,false);
evt.fire();
//ORYOUCANDOTHIS...
MicroBitEventevt(id,MICROBIT_BUTTON_EVT_DOWN);

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
##listen
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> listen( <div style='color:#008080; display:inline-block'>int</div> id,  <div style='color:#008080; display:inline-block'>int</div> value,  <div style='color:#008080; display:inline-block'>void(*)( MicroBitEvent )</div> handler)
#####Description
Register a listener function.
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *id* - The source of messages to listen for. Events sent from any other IDs will be filtered. Use MICROBIT_ID_ANY to receive events from all components.

>  <div style='color:#008080; display:inline-block'>int</div> *value* - The value of messages to listen for. Events with any other values will be filtered. Use MICROBIT_EVT_ANY to receive events of any value.

>  <div style='color:#008080; display:inline-block'>void(*)( MicroBitEvent )</div> *handler* - The function to call when an event is received.
#####Returns
MICROBIT_OK on success MICROBIT_INVALID_PARAMETER
#####Example
```c++
voidonButtonBClick()
{
//dosomething
}
uBit.MessageBus.listen(MICROBIT_ID_BUTTON_B,MICROBIT_BUTTON_EVT_CLICK,onButtonBClick);//callfunctionwheneveraclickeventisdetected.

```
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> listen( <div style='color:#008080; display:inline-block'>int</div> id,  <div style='color:#008080; display:inline-block'>int</div> value,  <div style='color:#008080; display:inline-block'>void(*)( MicroBitEvent )</div> handler,  <div style='color:#008080; display:inline-block'>uint16_t</div> flags)
#####Description
Register a listener function.
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *id* - The source of messages to listen for. Events sent from any other IDs will be filtered. Use MICROBIT_ID_ANY to receive events from all components.

>  <div style='color:#008080; display:inline-block'>int</div> *value* - The value of messages to listen for. Events with any other values will be filtered. Use MICROBIT_EVT_ANY to receive events of any value.

>  <div style='color:#008080; display:inline-block'>void(*)( MicroBitEvent )</div> *handler* - The function to call when an event is received.

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *flags*
#####Returns
MICROBIT_OK on success MICROBIT_INVALID_PARAMETER
#####Example
```c++
voidonButtonBClick()
{
//dosomething
}
uBit.MessageBus.listen(MICROBIT_ID_BUTTON_B,MICROBIT_BUTTON_EVT_CLICK,onButtonBClick);//callfunctionwheneveraclickeventisdetected.

```
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> listen( <div style='color:#008080; display:inline-block'>int</div> id,  <div style='color:#008080; display:inline-block'>int</div> value,  <div style='color:#008080; display:inline-block'>void(*)( MicroBitEvent , void *)</div> handler,  <div style='color:#008080; display:inline-block'>void *</div> arg)
#####Description
Register a listener function.
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *id* - The source of messages to listen for. Events sent from any other IDs will be filtered. Use MICROBIT_ID_ANY to receive events from all components.

>  <div style='color:#008080; display:inline-block'>int</div> *value* - The value of messages to listen for. Events with any other values will be filtered. Use MICROBIT_EVT_ANY to receive events of any value.

>  <div style='color:#008080; display:inline-block'>void(*)( MicroBitEvent , void *)</div> *handler*

>  <div style='color:#008080; display:inline-block'>void *</div> *arg*
#####Returns
MICROBIT_OK on success MICROBIT_INVALID_PARAMETER
#####Example
```c++
voidonButtonBClick(void*arg)
{
//dosomething
}
uBit.MessageBus.listen(MICROBIT_ID_BUTTON_B,MICROBIT_BUTTON_EVT_CLICK,onButtonBClick);//callfunctionwheneveraclickeventisdetected.

```
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> listen( <div style='color:#008080; display:inline-block'>int</div> id,  <div style='color:#008080; display:inline-block'>int</div> value,  <div style='color:#008080; display:inline-block'>void(*)( MicroBitEvent , void *)</div> handler,  <div style='color:#008080; display:inline-block'>void *</div> arg,  <div style='color:#008080; display:inline-block'>uint16_t</div> flags)
#####Description
Register a listener function.
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *id* - The source of messages to listen for. Events sent from any other IDs will be filtered. Use MICROBIT_ID_ANY to receive events from all components.

>  <div style='color:#008080; display:inline-block'>int</div> *value* - The value of messages to listen for. Events with any other values will be filtered. Use MICROBIT_EVT_ANY to receive events of any value.

>  <div style='color:#008080; display:inline-block'>void(*)( MicroBitEvent , void *)</div> *handler*

>  <div style='color:#008080; display:inline-block'>void *</div> *arg*

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *flags*
#####Returns
MICROBIT_OK on success MICROBIT_INVALID_PARAMETER
#####Example
```c++
voidonButtonBClick(void*arg)
{
//dosomething
}
uBit.MessageBus.listen(MICROBIT_ID_BUTTON_B,MICROBIT_BUTTON_EVT_CLICK,onButtonBClick);//callfunctionwheneveraclickeventisdetected.

```
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> listen( <div style='color:#008080; display:inline-block'>typename T</div> ,  <div style='color:#008080; display:inline-block'>uint16_t</div> id,  <div style='color:#008080; display:inline-block'>uint16_t</div> value,  <div style='color:#008080; display:inline-block'>T *</div> object,  <div style='color:#008080; display:inline-block'>void(T::*)( MicroBitEvent )</div> handler)
#####Description
Register a listener function.
#####Parameters

>  <div style='color:#008080; display:inline-block'>typename T</div> **

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *id* - The source of messages to listen for. Events sent from any other IDs will be filtered. Use MICROBIT_ID_ANY to receive events from all components.

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *value* - The value of messages to listen for. Events with any other values will be filtered. Use MICROBIT_EVT_ANY to receive events of any value.

>  <div style='color:#008080; display:inline-block'>T *</div> *object*

>  <div style='color:#008080; display:inline-block'>void(T::*)( MicroBitEvent )</div> *handler*
#####Returns
MICROBIT_OK on success MICROBIT_INVALID_PARAMETER
#####Example
```c++
voidSomeClass::onButtonBClick()
{
//dosomething
}

SomeClasss=newSomeClass();
uBit.MessageBus.listen(MICROBIT_ID_BUTTON_B,MICROBIT_BUTTON_EVT_CLICK,s,&SomeClass::onButtonBClick);

```
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> listen( <div style='color:#008080; display:inline-block'>typename T</div> ,  <div style='color:#008080; display:inline-block'>uint16_t</div> id,  <div style='color:#008080; display:inline-block'>uint16_t</div> value,  <div style='color:#008080; display:inline-block'>T *</div> object,  <div style='color:#008080; display:inline-block'>void(T::*)( MicroBitEvent )</div> handler,  <div style='color:#008080; display:inline-block'>uint16_t</div> flags)
#####Description
Register a listener function.
#####Parameters

>  <div style='color:#008080; display:inline-block'>typename T</div> **

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *id* - The source of messages to listen for. Events sent from any other IDs will be filtered. Use MICROBIT_ID_ANY to receive events from all components.

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *value* - The value of messages to listen for. Events with any other values will be filtered. Use MICROBIT_EVT_ANY to receive events of any value.

>  <div style='color:#008080; display:inline-block'>T *</div> *object*

>  <div style='color:#008080; display:inline-block'>void(T::*)( MicroBitEvent )</div> *handler*

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *flags*
#####Returns
MICROBIT_OK on success MICROBIT_INVALID_PARAMETER
#####Example
```c++
voidSomeClass::onButtonBClick()
{
//dosomething
}

SomeClasss=newSomeClass();
uBit.MessageBus.listen(MICROBIT_ID_BUTTON_B,MICROBIT_BUTTON_EVT_CLICK,s,&SomeClass::onButtonBClick);

```
##ignore
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> ignore( <div style='color:#008080; display:inline-block'>int</div> id,  <div style='color:#008080; display:inline-block'>int</div> value,  <div style='color:#008080; display:inline-block'>void(*)( MicroBitEvent )</div> handler)
#####Description
Unregister a listener function. Listners are identified by the Event ID, Event VALUE and handler registered using  listen()
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *id* - The Event ID used to register the listener. 

>  <div style='color:#008080; display:inline-block'>int</div> *value* - The Event VALUE used to register the listener. 

>  <div style='color:#008080; display:inline-block'>void(*)( MicroBitEvent )</div> *handler* - The function used to register the listener.
#####Returns
MICROBIT_OK on success MICROBIT_INVALID_PARAMETER
#####Example
```c++
voidonButtonBClick()
{
//dosomething
}

uBit.MessageBus.ignore(MICROBIT_ID_BUTTON_B,MICROBIT_BUTTON_EVT_CLICK,onButtonBClick);

```
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> ignore( <div style='color:#008080; display:inline-block'>int</div> id,  <div style='color:#008080; display:inline-block'>int</div> value,  <div style='color:#008080; display:inline-block'>void(*)( MicroBitEvent , void *)</div> handler)
#####Description
Unregister a listener function. Listners are identified by the Event ID, Event VALUE and handler registered using  listen()
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *id* - The Event ID used to register the listener. 

>  <div style='color:#008080; display:inline-block'>int</div> *value* - The Event VALUE used to register the listener. 

>  <div style='color:#008080; display:inline-block'>void(*)( MicroBitEvent , void *)</div> *handler* - The function used to register the listener.
#####Returns
MICROBIT_OK on success MICROBIT_INVALID_PARAMETER
#####Example
```c++
voidonButtonBClick(void*arg)
{
//dosomething
}

uBit.MessageBus.ignore(MICROBIT_ID_BUTTON_B,MICROBIT_BUTTON_EVT_CLICK,onButtonBClick);

```
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> ignore( <div style='color:#008080; display:inline-block'>typename T</div> ,  <div style='color:#008080; display:inline-block'>uint16_t</div> id,  <div style='color:#008080; display:inline-block'>uint16_t</div> value,  <div style='color:#008080; display:inline-block'>T *</div> object,  <div style='color:#008080; display:inline-block'>void(T::*)( MicroBitEvent )</div> handler)
#####Description
Unregister a listener function. Listners are identified by the Event ID, Event VALUE and handler registered using  listen()
#####Parameters

>  <div style='color:#008080; display:inline-block'>typename T</div> **

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *id* - The Event ID used to register the listener. 

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *value* - The Event VALUE used to register the listener. 

>  <div style='color:#008080; display:inline-block'>T *</div> *object*

>  <div style='color:#008080; display:inline-block'>void(T::*)( MicroBitEvent )</div> *handler* - The function used to register the listener.
#####Returns
MICROBIT_OK on success MICROBIT_INVALID_PARAMETER
#####Example
```c++
voidSomeClass::onButtonBClick()
{
//dosomething
}

SomeClasss=newSomeClass();
uBit.MessageBus.ignore(MICROBIT_ID_BUTTON_B,MICROBIT_BUTTON_EVT_CLICK,s,&SomeClass::onButtonBClick);

```
##elementAt
<br/>
####<div style='color:#FF69B4; display:inline-block'>MicroBitListener</div> elementAt( <div style='color:#008080; display:inline-block'>int</div> n)
#####Description
Returns the microBitListener with the given position in our list.  MicroBitListener
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *n* - The position in the list to return. 
#####Returns
the  MicroBitListener  at postion n in the list, or NULL if the position is invalid. 
##~MicroBitMessageBus
<br/>
####~MicroBitMessageBus()
#####Description
Destructor for  MicroBitMessageBus
____
[comment]: <> ({"end":"MicroBitMessageBus"})
