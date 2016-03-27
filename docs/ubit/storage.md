#uBit.storage

##Overview

`MicroBitStorage` provides a simple way to store data on the micro:bit that persists
through power cycles. It currently takes the form of a key value store which contains
a number of Key Value pairs.

The micro:bit has 256 kB flash memory and 16 kB random access memory (RAM). Flash memory
is *non-volatile*, which essentially means that data is not forgotten when the device
is powered off, this is the technology that many USB sticks use.

The alternative, RAM (known as *volatile* memory), cannot be persisted through power cycling the device as its
operation relies upon maintaining a constant supply of power.

Therefore, `MicroBitStorage` utilises the *non-volatile* nature of flash memory, to
store its data. This class is utilised by the [compass](compass.md), [accelerometer](compass.md)
and [bleManager](blemanager.md) to improve the user experience by persisting calibration
and bonding data.


###Operations

You can `put()`, `get()` and `remove()` key value pairs from the store.

Key Value pairs have a fixed length key of `16 bytes`, and a fixed length value of
`32 bytes`. This class only populates a single block (`1024 bytes`) in its current state,
which means that **21** Key Value pairs can be stored.

##Message Bus ID

> None.

##Message Bus Events

> None.

##API
[comment]: <> ({"className":"MicroBitStorage"})
[comment]: <> ({"end":"MicroBitStorage"})
