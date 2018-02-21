# Partial Flashing Service

## Introduction

The partial flashing service allows a BLE client to connect to a micro:bit and read and write the information required to partially update the firmware (e.g. the MakeCode section of the flash).

## Bluetooth Service Specification

 Please see the [micro:bit Bluetooth profile specification](https://lancaster-university.github.io/microbit-docs/resources/bluetooth/bluetooth_profile.html).


## Characteristic Commands
The service consists of a single Bluetooth GATT characteristic that responds to a clients WRITE/WRITE WITHOUT RESPONSE request with a BLE Notification. The characteristic supports two commands: one to request Memory Map information, and one to write data to the flash.

### Region Info Command

The Region Info command is used to request information from the Memory Map. The client sends a WRITE or WRITE WITHOUT RESPONSE command with the control byte (byte 0) set to 0x00 (Region Info) and byte 1 set to the region ID:

#### Client Write Request

|    | Byte 0 / Command | Byte 1 / Region # |
|---|---|---|
| Read Soft Device | 0x00 | 0x00 |
| Read DAL | 0x00 | 0x01 |
| Read MakeCode | 0x00 | 0x02 |

#### micro:bit Response

The micro:bit looks up the relevant information and returns it using a BLE NOTIFICATION:

| Byte 0 | Byte 1 | Bytes [2,3,4,5] | Bytes [6,7,8,9] | Bytes [10,11,12,13,14,15,16,17] |
|---|---|---|---|---|
| READ_NOTIFICATION / 0x00 | Region # | Region Start Address | Region End Address | Hash |


### Write Data Command
To send the new firmware and write it to the flash a WRITE_WITHOUT_RESPONSE command is used. These packets begin with the command byte (byte 0) set to 0x01. The packet is structured as follows:

#### Client Write Without Response

| 1 Byte    | 16 Bytes | 2 Bytes | 1 Byte  |
|---|---|---|---|
| COMMAND   | DATA     | OFFSET  | PACKET# |

The micro:bit handles packets in blocks of 4 packets. The offset from the first packet in the block is stored whilst waiting for the remaining 3 packets. Once all 4 packets have been received the block of 4 is written to the flash at the offset specified by the packet and a notification is sent to the client to request the next block of packets.

#### micro:bit Response

**Successful Write:**

| Byte 0 | Byte 1 | 
|---|---|
| WRITE_NOTIFICATION / 0x01 | 0xFF |


**Out Of Order Packet
If the micro:bit detects an out of order packet the packet count is reset to the start of the current block and a notification is sent to inform the client.

| Byte 0 | Byte 1 | 
|---|---|
| WRITE_NOTIFICATION / 0x01 | 0xAA |

**End Of Transmission**

When the start of the embedded source is reached a WRITE request is issues with the value 0xFF. The micro:bit then writes the current block buffer to finish the transmission and overwrite the embedded source magic.

| Byte 0 |
|---|
| END_OF_TX / 0xFF |

### UUIDs
```
const uint8_t  MicroBitPartialFlashServiceUUID[] = {
    0xe9,0x7d,0xd9,0x1d,0x25,0x1d,0x47,0x0a,0xa0,0x62,0xfa,0x19,0x22,0xdf,0xa9,0xa8
};

const uint8_t  MicroBitPartialFlashServiceCharacteristicUUID[] = {
    0xe9,0x7d,0x3b,0x10,0x25,0x1d,0x47,0x0a,0xa0,0x62,0xfa,0x19,0x22,0xdf,0xa9,0xa8
};
```

## Partial Flashing Client

### Example Client for Android
Please see an example implementation [on GitHub](https://github.com/microbit-sam/microbit-android).

### Client Process
A client completing the partial flashing process will first need to read the Memory Map from the micro:bit to obtain the region hashes.

Once the hashes have been obtained from the micro:bit they need to be compared with the hashes found within the new hex file to determine if it is possible to partially flash the micro:bit. Partial flashing requires the micro:bit to be using a matching version of the DAL. The hashes within the file can be found in the 16 bytes following the 'magic number' `708E3B92C615A841C49866C975EE5197` found in the file.

**Defined here:**

```
; start
    .startaddr 0x30000
    .hex 708E3B92C615A841C49866C975EE5197 ; magic number
    .hex 0662709FA0315567 ; hex template hash
    .hex EDE9690A1093AE71 ; program hash
    .short 11   ; num. globals
    .short 0 ; patched with number of words resulting from assembly
    .word 0 ; reserved
    .word 0 ; reserved
    .word 0 ; reserved
```

![Determine Partial Flashing](https://github.com/microbit-foundation/partial-flashing-issue-tracker/blob/master/DeterminePF.png?raw=true)

The client then transfers the hex data from the file starting at the 'magic number' up until the page that contains the [embedded source](https://makecode.com/source-embedding) - also found using a magic number `41140E2FB82FA2BB`.

Once the embedded source is found the client sends an END OF TRANSMISSION BLE write to inform the micro:bit the transfer is over.

![Do Partial Flashing](https://github.com/microbit-foundation/partial-flashing-issue-tracker/blob/master/PFFlow.png?raw=true)

