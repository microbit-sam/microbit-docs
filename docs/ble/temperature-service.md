# Bluetooth Temperature Service

## Introduction

This Bluetooth Low Energy (BLE) service is an optional part of the standard bluetooth profile for the micro:bit. It is a passive service, that can operate transparently in the
background as your main program is running. It provides live temperature data to any attached BLE master device. You do not need to explicity address and API on the service to acheive this.
Please note that the temperature data is inferred from the die temperature of the Nordic nrf51822 CPU. Whilst this sensor has a high precision, it is not calibrated, so will exhibit
a linear shift (although changes in temperature will be accurate). See [MicroBitThermometer](/ubit/thermometer.md) for informaiton on the API to allow calibration.

## Enabling the Service

This service is disabled by default. To enable the service, simply create an instance of this class in your program, at any time after the uBit object has been initialised:

```cpp
    new MicroBitTemperatureService(*uBit.ble, uBit.thermometer);
```

!!! note
    Using BLE services is memory hungry. By default, some of the memory normally used by Nordic's BLE protocol stack (knwon as a SoftDevice), is reclaimed by the micro:bit runtime as general purpose memory for your applications. if you enable more BLE services, then you may need to provide more memory back to Soft Device to ensure proper operation. If after enabling this service your BLE applicaiton cannot access the service reliably, you should consider increasing the value of MICROBIT_SD_GATT_TABLE_SIZE in your inc/MicroBitConfig.h. The more service you add, the larger this will need to be, up to the limit defined in MicroBitConfig.h.

## BLE Service Specification

 Please see the [micro:bit BLE profile specification](../resources/bluetooth/microbit-profile-V1.7-Level-2.pdf).

## Example Applications for Android/IOS/Android

 COMING SOON
