#uBit.radio.event

##Overview

It is also possible to transparently send and receive events over the `MicroBitRadio` channel. This can provide very simple and easy to integrate
support for event driven applications. Once configured, an event raised on one micro:bit can be detected on another - in the just the same way as
a local event such as a button click.

To use this functionality, all that is needed is to register the event codes that you would like to be sent over the radio, then write event handlers
for the message bus as with all other events. See the documentation for the [`MicroBitMessageBus`](messageBus.md) for details of how to write
event handlers.

For example, if you wanted to share an event SOMETHING with another micro:bit whenever ButtonA is pressed, you might write code like this on the sending micro:bit:

```cpp
#define MY_APP_ID           4000
#define SOMETHING           1

int main()
{
    uBit.radio.enable();

    // Ensure the radio is listening out to forward our events
    uBit.radio.event.listen(MY_APP_ID, MICROBIT_EVT_ANY);

    while(1)
    {
        if (uBit.buttonA.isPressed())
            MicroBitEvent(MY_APP_ID, SOMETHING);

        uBit.sleep(1000);
    }
}
```

...and on the micro:bits wanting to receive the event:


```cpp
#define MY_APP_ID           4000
#define SOMETHING           1

void onSomething(MicroBitEvent e)
{
    uBit.display.scrollAsync("Something!");
}

int main()
{
    uBit.messageBus.listen(MY_APP_ID, SOMETHING, onSomething);
    uBit.radio.enable();

    while(1)
        uBit.sleep(1000);
}
```

##Message Bus ID

> None.

##Message Bus Events

> None.

#API
[comment]: <> ({"className":"MicroBitRadioEvent"})
[comment]: <> ({"end":"MicroBitRadioEvent"})
