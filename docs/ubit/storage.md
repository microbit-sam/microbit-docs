#uBit.storage

##Overview

MicroBitStorage provides a simple way to store data on the micro:bit that persists
through resets. It currently takes the form of a Key Value store which contains
a number of Key Value pairs.

You can `put()`, `get()` and `remove()` Key Value pairs from the store.

Key Value pairs have a fixed length Key of `16 bytes`, and a fixed length value of
`32 bytes`. This class only populates a single block (`1024 bytes`) in its current state,
which means that **21** Key Value pairs can be stored.

Currently, this class is utilised by the [compass](compass.md), [accelerometer](compass.md)
and [bleManager](blemanager.md) to improve the user experience by persisting calibration
and bonding data.

##Message Bus ID

> None.

##Message Bus Events

> None.

##API
[comment]: <> ({"className":"MicroBitStorage"})
[comment]: <> ({"end":"MicroBitStorage"})
