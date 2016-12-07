# Eddystone

## Introduction

Bluetooth beacons are used to indicate proximity to a place or object of interest. Beacons use Bluetooth advertising to broadcast a small amount of data, which can be received and acted upon by anyone in range with a suitable device and software, typically a smartphone and application.

There are various beacon message formats, which define the way Bluetooth advertising packets are used as containers for beacon data. iBeacon is Apple's beacon message format. Eddystone comes from Google.

## Eddystone
The [Eddystone specification](https://github.com/google/eddystone) defines four frame types at the time of writing. UID (unique ID), URL (Uniform Resource Locator), TLM (telemetry) and EID (Ephemeral ID). 

UID - this is simply an identifier which is mapped by an application receiving it, to something meaningful like a location

URL - this is exactly what you'd expect. A URL, typically in compressed form, which points to something like a web site

TLM - this frame type contains data about the beacon's operation such as its battery level or temperature.

EID - this is the newest frame type and provides a way of using IDs which is secure such that only the operator of the beacons can make use of the encrypted, temporary IDs in these beacon messages.  
## micro:bit Eddystone beacons
micro:bit is able to use either of the UID or URL frame types. A simple API makes it very straightforward to turn a micro:bit into an Eddystone beacon although there are also some configuration requirements for the build process to take note of as well. 
## Examples

The best way to explain how to use the two frame types is to look at examples. The code shown here comes from two full source code examples you'll find in the microbit-samples repository. 

### URL Frame type

To set up a micro:bit so that it advertises with the Eddystone URL frame type, the **eddystone_url** flag in config.json must be set and the eddystone_uid flag must be unset. Beacons are usually connectionless so there's no need to have pairing and other security capabilities switched on either.

```
{
    "microbit-dal": {
        "bluetooth": {
            "enabled": 1,
            "pairing_mode": 0,
            "private_addressing": 0,
            "whitelist": 0,
            "advertising_timeout": 0,
            "tx_power": 6,
            "dfu_service": 0,
            "event_service": 0,
            "device_info_service": 0,
            "eddystone_url": 1,
            "eddystone_uid": 0
        }
    }
}

```  
#### Starting Advertising
In your source code, you'll need to define the URL you want to be broadcast and then call uBit.bleManager.advertiseEddystoneUrl with the URL as one of the arguments. 

For example, the following shows the use of a URL shortener that allows for a URL of a longer length, to be sent by an Eddistone Beacon.
In this case, http://www.bittysoftware.com/, is shortened to https://goo.gl/TlUTF7. It is important to understand that the maximum length of an URL is 17 but in the micro:bit implementation of the specification, the byte encoding is taken care of. This means that the URL is shortened further from 21 to 14 where the https:// is encoded as one byte. It is left up to the reader to inspect the specification for other byte encoding.

``` cpp
#include "MicroBit.h"

MicroBit uBit;

char URL[] = "https://goo.gl/TlUTF7";
const int8_t CALIBRATED_POWERS[] = {-49, -37, -33, -28, -25, -20, -15, -10};

uint8_t advertising = 0;
uint8_t tx_power_level = 6;

void startAdvertising() {
    uBit.bleManager.advertiseEddystoneUrl(URL, CALIBRATED_POWERS[tx_power_level-1], false);
    uBit.bleManager.setTransmitPower(tx_power_level);
    uBit.display.scroll("ADV");
    advertising = 1;
}

```

The second argument is a value for the calibrated power field of the Eddystone message. It is supposed to indicate the power level that you could expect to find the Bluetooth signal at if you measured it 0 metres from the beacon. Devices receiving this information in a Bluetooth advertising packet can use it, along with the signal strength measured at the receiver, to perform a calculation called a path loss calculation to figure out an estimate of how far away the beacon it is.

The boolean argument, set to false here, indicates whether or not the micro:bit should accept connections. Sometimes you might like to have beacon behaviour but still want it to be possible to connect to the micro:bit so you can access one or more of the GATT services that the micro:bit has. In this situation, your config.json file may need to be adjusted to allow for the GATT and security capabilities you want and you will need to ensure your hex file contains the Bluetooth services you plan to use as well.


#### Stopping Advertising
Stopping advertising is straightforward, as shown in this example:

``` cpp
void stopAdvertising() {
    uBit.bleManager.stopAdvertising();
    uBit.display.scroll("OFF");
    advertising = 0;
}
```

### UID Frame type

To set up a micro:bit so that it advertises with the Eddystone UID frame type, the **eddystone_uid** flag in config.json must be set and the eddystone_url flag must be unset. Beacons are usually connectionless so there's no need to have pairing and other security capabilities switched on either.

```
{
    "microbit-dal": {
        "bluetooth": {
            "enabled": 1,
            "pairing_mode": 0,
            "private_addressing": 0,
            "whitelist": 0,
            "advertising_timeout": 0,
            "tx_power": 6,
            "dfu_service": 0,
            "event_service": 0,
            "device_info_service": 0,
            "eddystone_url": 0,
            "eddystone_uid": 1
        }
    }
}

```  
#### Starting Advertising
In your source code, you'll need to define the UID you want to be broadcast in two parts, named the UID namespace and the UID instance. The [Eddystone UID frame specification](https://github.com/google/eddystone/tree/master/eddystone-uid) gives guidance on how to choose values for your UIDs. In all cases however, the UID namespace must be 10 bytes long and the UID instance must be 6 bytes long.

To start advertising a UID, call advertiseEddystoneUid as shown in this example:

``` cpp
char UID_NAMESPACE[] = {0x0E,0x67,0x47,0x04,0x42,0xD0,0x14,0x06,0xD5,0x83}; // sha-1 hash of "com.bittysoftware" 
char UID_INSTANCE[]  = {0x00 , 0x00, 0x00, 0x00, 0x00, 0x01};
const int8_t CALIBRATED_POWERS[] = {-49, -37, -33, -28, -25, -20, -15, -10};

uint8_t advertising = 0;
uint8_t tx_power_level = 6;

void startAdvertising() {
    uBit.bleManager.advertiseEddystoneUid(UID_NAMESPACE, UID_INSTANCE, CALIBRATED_POWERS[tx_power_level-1], false);
    uBit.bleManager.setTransmitPower(6);
    uBit.display.scroll("ADV");
    advertising = 1;
}
```

Other arguments are as for the URL frame type described above.

#### Stopping Advertising
Stopping advertising is accomplished with the same stopAdvertising() function shown above.

#### Video Demonstrations

##### UIDs

<iframe src="https://www.youtube.com/embed/mZlwxIOYxPE" width="750" height="422" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

##### URLs

<iframe allowfullscreen="" frameborder="0" height="422" mozallowfullscreen="" src="https://www.youtube.com/embed/39gf2s70-Fs" webkitallowfullscreen="" width="750"></iframe>

