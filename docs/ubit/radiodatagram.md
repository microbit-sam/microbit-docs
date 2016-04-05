#uBit.radio.datagram

##Overview

This is the most flexible way to use the radio, and lets you easily send and receive up to 32 bytes of data at a time.
This data can be provided as array of bytes, a text string, or PacketBuffer.

You can send a packet at any time using the `uBit.radio.datagram.send` function.

Any other micro:bits in range will detect the transmitted packet, and make the packet available through the
`uBit.radio.datagram.recv` function.

Any micro:bits receiving a datagram packet will also raise a `MICROBIT_RADIO_EVT_DATAGRAM` event to indicate
that some data is ready to be read.

For example, imagine you were creating a simple remote control car with one micro:bit acting as a remote controller, and another connected to some servos on the car.

You might decide that simply sending a `1` means turn left, and a `2` means turn right, so you may write a program like this for the remote control:

```cpp
int main()
{
    uBit.radio.enable();

    while(1)
    {
        if (uBit.buttonA.isPressed())
            uBit.radio.datagram.send("1");

        else if (uBit.buttonB.isPressed())
            uBit.radio.datagram.send("2");

        uBit.sleep(100);
    }
}
```

...and one like this for the remote control car:


```cpp
void onData(MicroBitEvent e)
{
    ManagedString s = uBit.radio.datagram.recv();

    if (s == "1")
        uBit.io.P0.setServoValue(0);

    if (s == "2")
        uBit.io.P0.setServoValue(180);
}

int main()
{
    uBit.messageBus.listen(MICROBIT_ID_RADIO, MICROBIT_RADIO_EVT_DATAGRAM, onData);
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
[comment]: <> ({"className":"MicroBitRadioDatagram"})
[comment]: <> ({"end":"MicroBitRadioDatagram"})
