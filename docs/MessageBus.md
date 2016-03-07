#uBit.MessageBus

##Overview

##Message Bus ID

##Message Bus Events

##API
[comment]: <> ({"className":"MicroBitMessageBus"})
____
##Constructor
<br/>
####MicroBitMessageBus()
<br/>
#####Description
Default constructor. Anticipating only one MessageBus per device, as filtering is handled within the class.

<br/><br/>
____
##send
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> send( <div style='color:#008080; display:inline-block'>MicroBitEvent</div> evt)
<br/>
#####Description
Queues the given event to be sent to all registered recipients.

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitEvent</div> *evt*

<br/><br/>
#####Example
```c++
MicroBitEventevt(id,MICROBIT_BUTTON_EVT_DOWN,ticks,false);
evt.fire();
//ORYOUCANDOTHIS...
MicroBitEventevt(id,MICROBIT_BUTTON_EVT_DOWN);

```

<br/><br/>
____
##process
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> process( <div style='color:#008080; display:inline-block'>MicroBitEvent  &</div> evt)
<br/>
#####Description
Internal function, used to deliver the given event to all relevant recipients. Normally, this is called once an event has been removed from the event queue.

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitEvent  &</div> *evt* - The event to send. 

<br/><br/>
#####Returns
1 if all matching listeners were processed, 0 if further processing is required. 

<br/><br/>
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> process( <div style='color:#008080; display:inline-block'>MicroBitEvent  &</div> evt,  <div style='color:#008080; display:inline-block'>bool</div> urgent)
<br/>
#####Description
Internal function, used to deliver the given event to all relevant recipients. Normally, this is called once an event has been removed from the event queue.

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitEvent  &</div> *evt* - The event to send. 

>  <div style='color:#008080; display:inline-block'>bool</div> *urgent* - The type of listeners to process (optional). If set to true, only listeners defined as urgent and non-blocking will be processed otherwise, all other (standard) listeners will be processed. 

<br/><br/>
#####Returns
1 if all matching listeners were processed, 0 if further processing is required. 

<br/><br/>
____
##listen
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> listen( <div style='color:#008080; display:inline-block'>int</div> id,  <div style='color:#008080; display:inline-block'>int</div> value,  <div style='color:#008080; display:inline-block'>void(*)( MicroBitEvent )</div> handler)
<br/>
#####Description
Register a listener function.

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *id* - The source of messages to listen for. Events sent from any other IDs will be filtered. Use MICROBIT_ID_ANY to receive events from all components.

>  <div style='color:#008080; display:inline-block'>int</div> *value* - The value of messages to listen for. Events with any other values will be filtered. Use MICROBIT_EVT_ANY to receive events of any value.

>  <div style='color:#008080; display:inline-block'>void(*)( MicroBitEvent )</div> *handler* - The function to call when an event is received.

<br/><br/>
#####Returns
MICROBIT_OK on success MICROBIT_INVALID_PARAMETER

<br/><br/>
#####Example
```c++
voidonButtonBClick()
{
//dosomething
}
uBit.MessageBus.listen(MICROBIT_ID_BUTTON_B,MICROBIT_BUTTON_EVT_CLICK,onButtonBClick);//callfunctionwheneveraclickeventisdetected.

```

<br/><br/>
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> listen( <div style='color:#008080; display:inline-block'>int</div> id,  <div style='color:#008080; display:inline-block'>int</div> value,  <div style='color:#008080; display:inline-block'>void(*)( MicroBitEvent )</div> handler,  <div style='color:#008080; display:inline-block'>uint16_t</div> flags)
<br/>
#####Description
Register a listener function.

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *id* - The source of messages to listen for. Events sent from any other IDs will be filtered. Use MICROBIT_ID_ANY to receive events from all components.

>  <div style='color:#008080; display:inline-block'>int</div> *value* - The value of messages to listen for. Events with any other values will be filtered. Use MICROBIT_EVT_ANY to receive events of any value.

>  <div style='color:#008080; display:inline-block'>void(*)( MicroBitEvent )</div> *handler* - The function to call when an event is received.

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *flags*

<br/><br/>
#####Returns
MICROBIT_OK on success MICROBIT_INVALID_PARAMETER

<br/><br/>
#####Example
```c++
voidonButtonBClick()
{
//dosomething
}
uBit.MessageBus.listen(MICROBIT_ID_BUTTON_B,MICROBIT_BUTTON_EVT_CLICK,onButtonBClick);//callfunctionwheneveraclickeventisdetected.

```

<br/><br/>
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> listen( <div style='color:#008080; display:inline-block'>int</div> id,  <div style='color:#008080; display:inline-block'>int</div> value,  <div style='color:#008080; display:inline-block'>void(*)( MicroBitEvent , void *)</div> handler,  <div style='color:#008080; display:inline-block'>void *</div> arg)
<br/>
#####Description
Register a listener function.

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *id* - The source of messages to listen for. Events sent from any other IDs will be filtered. Use MICROBIT_ID_ANY to receive events from all components.

>  <div style='color:#008080; display:inline-block'>int</div> *value* - The value of messages to listen for. Events with any other values will be filtered. Use MICROBIT_EVT_ANY to receive events of any value.

>  <div style='color:#008080; display:inline-block'>void(*)( MicroBitEvent , void *)</div> *handler*

>  <div style='color:#008080; display:inline-block'>void *</div> *arg*

<br/><br/>
#####Returns
MICROBIT_OK on success MICROBIT_INVALID_PARAMETER

<br/><br/>
#####Example
```c++
voidonButtonBClick(void*arg)
{
//dosomething
}
uBit.MessageBus.listen(MICROBIT_ID_BUTTON_B,MICROBIT_BUTTON_EVT_CLICK,onButtonBClick);//callfunctionwheneveraclickeventisdetected.

```

<br/><br/>
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> listen( <div style='color:#008080; display:inline-block'>int</div> id,  <div style='color:#008080; display:inline-block'>int</div> value,  <div style='color:#008080; display:inline-block'>void(*)( MicroBitEvent , void *)</div> handler,  <div style='color:#008080; display:inline-block'>void *</div> arg,  <div style='color:#008080; display:inline-block'>uint16_t</div> flags)
<br/>
#####Description
Register a listener function.

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *id* - The source of messages to listen for. Events sent from any other IDs will be filtered. Use MICROBIT_ID_ANY to receive events from all components.

>  <div style='color:#008080; display:inline-block'>int</div> *value* - The value of messages to listen for. Events with any other values will be filtered. Use MICROBIT_EVT_ANY to receive events of any value.

>  <div style='color:#008080; display:inline-block'>void(*)( MicroBitEvent , void *)</div> *handler*

>  <div style='color:#008080; display:inline-block'>void *</div> *arg*

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *flags*

<br/><br/>
#####Returns
MICROBIT_OK on success MICROBIT_INVALID_PARAMETER

<br/><br/>
#####Example
```c++
voidonButtonBClick(void*arg)
{
//dosomething
}
uBit.MessageBus.listen(MICROBIT_ID_BUTTON_B,MICROBIT_BUTTON_EVT_CLICK,onButtonBClick);//callfunctionwheneveraclickeventisdetected.

```

<br/><br/>
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> listen( <div style='color:#008080; display:inline-block'>typename T</div> ,  <div style='color:#008080; display:inline-block'>uint16_t</div> id,  <div style='color:#008080; display:inline-block'>uint16_t</div> value,  <div style='color:#008080; display:inline-block'>T *</div> object,  <div style='color:#008080; display:inline-block'>void(T::*)( MicroBitEvent )</div> handler)
<br/>
#####Description
Register a listener function.

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>typename T</div> **

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *id* - The source of messages to listen for. Events sent from any other IDs will be filtered. Use MICROBIT_ID_ANY to receive events from all components.

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *value* - The value of messages to listen for. Events with any other values will be filtered. Use MICROBIT_EVT_ANY to receive events of any value.

>  <div style='color:#008080; display:inline-block'>T *</div> *object*

>  <div style='color:#008080; display:inline-block'>void(T::*)( MicroBitEvent )</div> *handler*

<br/><br/>
#####Returns
MICROBIT_OK on success MICROBIT_INVALID_PARAMETER

<br/><br/>
#####Example
```c++
voidSomeClass::onButtonBClick()
{
//dosomething
}

SomeClasss=newSomeClass();
uBit.MessageBus.listen(MICROBIT_ID_BUTTON_B,MICROBIT_BUTTON_EVT_CLICK,s,&SomeClass::onButtonBClick);

```

<br/><br/>
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> listen( <div style='color:#008080; display:inline-block'>typename T</div> ,  <div style='color:#008080; display:inline-block'>uint16_t</div> id,  <div style='color:#008080; display:inline-block'>uint16_t</div> value,  <div style='color:#008080; display:inline-block'>T *</div> object,  <div style='color:#008080; display:inline-block'>void(T::*)( MicroBitEvent )</div> handler,  <div style='color:#008080; display:inline-block'>uint16_t</div> flags)
<br/>
#####Description
Register a listener function.

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>typename T</div> **

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *id* - The source of messages to listen for. Events sent from any other IDs will be filtered. Use MICROBIT_ID_ANY to receive events from all components.

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *value* - The value of messages to listen for. Events with any other values will be filtered. Use MICROBIT_EVT_ANY to receive events of any value.

>  <div style='color:#008080; display:inline-block'>T *</div> *object*

>  <div style='color:#008080; display:inline-block'>void(T::*)( MicroBitEvent )</div> *handler*

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *flags*

<br/><br/>
#####Returns
MICROBIT_OK on success MICROBIT_INVALID_PARAMETER

<br/><br/>
#####Example
```c++
voidSomeClass::onButtonBClick()
{
//dosomething
}

SomeClasss=newSomeClass();
uBit.MessageBus.listen(MICROBIT_ID_BUTTON_B,MICROBIT_BUTTON_EVT_CLICK,s,&SomeClass::onButtonBClick);

```

<br/><br/>
____
##ignore
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> ignore( <div style='color:#008080; display:inline-block'>int</div> id,  <div style='color:#008080; display:inline-block'>int</div> value,  <div style='color:#008080; display:inline-block'>void(*)( MicroBitEvent )</div> handler)
<br/>
#####Description
Unregister a listener function. Listners are identified by the Event ID, Event VALUE and handler registered using  listen()

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *id* - The Event ID used to register the listener. 

>  <div style='color:#008080; display:inline-block'>int</div> *value* - The Event VALUE used to register the listener. 

>  <div style='color:#008080; display:inline-block'>void(*)( MicroBitEvent )</div> *handler* - The function used to register the listener.

<br/><br/>
#####Returns
MICROBIT_OK on success MICROBIT_INVALID_PARAMETER

<br/><br/>
#####Example
```c++
voidonButtonBClick()
{
//dosomething
}

uBit.MessageBus.ignore(MICROBIT_ID_BUTTON_B,MICROBIT_BUTTON_EVT_CLICK,onButtonBClick);

```

<br/><br/>
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> ignore( <div style='color:#008080; display:inline-block'>int</div> id,  <div style='color:#008080; display:inline-block'>int</div> value,  <div style='color:#008080; display:inline-block'>void(*)( MicroBitEvent , void *)</div> handler)
<br/>
#####Description
Unregister a listener function. Listners are identified by the Event ID, Event VALUE and handler registered using  listen()

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *id* - The Event ID used to register the listener. 

>  <div style='color:#008080; display:inline-block'>int</div> *value* - The Event VALUE used to register the listener. 

>  <div style='color:#008080; display:inline-block'>void(*)( MicroBitEvent , void *)</div> *handler* - The function used to register the listener.

<br/><br/>
#####Returns
MICROBIT_OK on success MICROBIT_INVALID_PARAMETER

<br/><br/>
#####Example
```c++
voidonButtonBClick(void*arg)
{
//dosomething
}

uBit.MessageBus.ignore(MICROBIT_ID_BUTTON_B,MICROBIT_BUTTON_EVT_CLICK,onButtonBClick);

```

<br/><br/>
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> ignore( <div style='color:#008080; display:inline-block'>typename T</div> ,  <div style='color:#008080; display:inline-block'>uint16_t</div> id,  <div style='color:#008080; display:inline-block'>uint16_t</div> value,  <div style='color:#008080; display:inline-block'>T *</div> object,  <div style='color:#008080; display:inline-block'>void(T::*)( MicroBitEvent )</div> handler)
<br/>
#####Description
Unregister a listener function. Listners are identified by the Event ID, Event VALUE and handler registered using  listen()

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>typename T</div> **

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *id* - The Event ID used to register the listener. 

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *value* - The Event VALUE used to register the listener. 

>  <div style='color:#008080; display:inline-block'>T *</div> *object*

>  <div style='color:#008080; display:inline-block'>void(T::*)( MicroBitEvent )</div> *handler* - The function used to register the listener.

<br/><br/>
#####Returns
MICROBIT_OK on success MICROBIT_INVALID_PARAMETER

<br/><br/>
#####Example
```c++
voidSomeClass::onButtonBClick()
{
//dosomething
}

SomeClasss=newSomeClass();
uBit.MessageBus.ignore(MICROBIT_ID_BUTTON_B,MICROBIT_BUTTON_EVT_CLICK,s,&SomeClass::onButtonBClick);

```

<br/><br/>
____
##elementAt
<br/>
####<div style='color:#FF69B4; display:inline-block'>MicroBitListener</div> elementAt( <div style='color:#008080; display:inline-block'>int</div> n)
<br/>
#####Description
Returns the microBitListener with the given position in our list.  MicroBitListener

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *n* - The position in the list to return. 

<br/><br/>
#####Returns
the  MicroBitListener  at postion n in the list, or NULL if the position is invalid. 

<br/><br/>
____
##~MicroBitMessageBus
<br/>
####~MicroBitMessageBus()
<br/>
#####Description
Destructor for  MicroBitMessageBus

<br/><br/>
____
[comment]: <> ({"end":"MicroBitMessageBus"})
