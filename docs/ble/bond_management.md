## Bond Management

When Bluetooth devices pair, they can opt to persistently store the resultant keys. If they do, the devices are said to be "bonded". As of release 2.0.0-rc5 of the micro:bit runtime, a micro:bit persists Bluetooth pairing keys in the [micro:bit storage area](../ubit/storage/). In earlier releases, flashing a micro:bit over USB would result in Bluetooth pairing keys being lost and so the device would need to be paired again. This is no longer necessary. There may be occassions, however, where you do want to wipe those pairing keys off the micro:bit and if that is the case, you need to create a micro:bit application in C/C++ which includes the following code fragment, which will clear the pairing data out of storage:

```cpp
// Clear the memory page holding the BLE bond table.
    MicroBitStorage s = MicroBitStorage();
    s.flashPageErase((uint32_t *) BLE_BOND_DATA_PAGE);
```

After building this code and flashing the hex file to your micro:bit, Bluetooth bonds will be deleted. Make sure you also "forget" the pairing on the other device e.g. your smartphone otherwise it will continue to think (incorrectly) that it is paired with your micro:bit. Pair again if necessary.

