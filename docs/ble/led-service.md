# Bluetooth LED Service

## Introduction

This Bluetooth Low Energy (BLE) service is an optional part of the standard bluetooth profile for the micro:bit. It is a passive service, that can operate transparently in the
background as your main program is running. It allows any attached Bluetooth master device to read and write the status of the LEDs on the display. This includes reading and writing
nitmap values to the display, and activating simple animations such as scrolling text messages.

live accelerometer data to any attached Bluetooth master device. You do not need to explicity address and API on the service to acheive this.

## Enabling the Service

This service is disabled by default. To enable the service, simply create an instance of this class in your program, at any time after the uBit object has been initialised:

```cpp
    new MicroBitLEDService(*uBit.ble, uBit.display);
```

!!! note
    Using Bluetooth services is memory hungry. By default, some of the memory normally used by Nordic's Bluetooth protocol stack (knwon as a SoftDevice), is reclaimed by the micro:bit runtime as general purpose memory for your applications. if you enable more Bluetooth services, then you may need to provide more memory back to Soft Device to ensure proper operation. If after enabling this service your Bluetooth applicaiton cannot access the service reliably, you should consider increasing the value of MICROBIT_SD_GATT_TABLE_SIZE in your inc/MicroBitConfig.h. The more service you add, the larger this will need to be, up to the limit defined in MicroBitConfig.h.

## Bluetooth Service Specification

 Please see the [micro:bit Bluetooth profile specification](../resources/bluetooth/microbit-profile-V1.7-Level-2.pdf).

## Example Applications for Android/IOS/Android

 COMING SOON
