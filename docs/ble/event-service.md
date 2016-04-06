# Bluetooth Event Service

## Introduction

This Bluetooth service is an optional part of the standard Bluetooth profile for the micro:bit. It is a passive service, that can operate transparently in the
background as your main program is running. This service extends the microBitMessageBus over Bluetooth, so that standard MicroBitEvents raised on the device can be transmitted transparently over
Bluetooth and received and processed by connected Bluetooth master device such as a smartphone.  You do not need to explicity address and API on the service to achieve this.

## Enabling the Service

This service is enabled by default.

## Bluetooth Service Specification

 Please see the [micro:bit Bluetooth profile specification](../resources/bluetooth/microbit-profile-V1.7-Level-2.pdf).

## Example Applications for Android/IOS/Android

### General Procedures

micro:bit uses an event bus which relays event objects from system components which generate them to other system components which have registered an interest in events of a given type. This principle and capability has been extended to remote devices connected over Bluetooth. Connected clients can indicate the types of event they are interested in and be informed via Bluetooth notificatons as and when such events occur. Similarly, micro:bit application code can inform a connected client of events which might happen in or be observed by an application running on the connected device (the client application) and be informed when they occur via Bluetooth write operations. 

Event objects consist of an integer (4 octets) type and an integer (4 octets) value.

When either client application or micro:bit code registers an interest in an event type it may register for all events of that type regardless of the associated value or may specify a particular value which must accompany that event type for it to be of interest.

The Microbit Requirements characteristic allows micro:bit code to inform the client application of a list of one or more event types/values it wants to be informed about if they arise. For example if a client application monitors for incoming SMS messages and defines receipt of an SMS message to be event type 1234 then a micro:bit application could inform the client application it wants to be told when an SMS has been received by declaring its interest in event type 1234 in its MicrobitRequirements characteristic.

The Client Requirements characteristic has a similar purpose but is the mechanism the client application uses to tell the micro:bit application what events it is interested in. Should they arise and notifications have been enabled on the MicrobitEvent characteristic, the client application will receive a Bluetooth notification containing the event object. A micro:bit application which monitors temperature and notifies a smartphone application when the temperature falls below a specified limit or rises above another threshold could use events to notify the client application when either of these things happens.

The MicroBit Event characteristic is used to convey events which have happened on the micro:bit to the connected client. Notifications are normally used but the most recent events for which the client registered can be determined by reading the characteristic value at any time.

The Client Event characteirstic is used to convey events which have happened on the client device to the micro:bit. This is achieved through the client application writing one or more events to the characteristic value.

See the profile page and profile reference documentation for data format and UUID details.

### Android

<img src="../../resources/bluetooth/event_demo.png" alt="Event Demo">

#### Android Bluetooth APIs

Android developers should make themselves familiar with the [Android Bluetooth low energy APIs](http://developer.android.com/guide/topics/connectivity/bluetooth-le.html)

#### microbit-ble-demo-android

The open source microbit-ble-demo-android application contains a number of demonstrations of the micro:bit Bluetooth event service including Temperature Alarm and Squirrel Counter. The main body of code for the temperature alarm demonstration can be found in ui.TemperatureAlarmActivity.java except for the Bluetooth operations themselves which are in bluetooth.BleAdapterService which acts as a kind of higher level Bluetooth API for activities to use without needing to directly concern themselves too closely with the Android APIs themselves. In most cases, operations are asynchronous so that the activity code initiates a Bluetooth operation by calling one of the methods in bluetooth.BleAdapterService (e.g. readCharacteristic(....) ) and later receives a message containing the result of the operation from this object via a Handler object. The message is examined in the Handler code and acted upon.

Key parts of the temperature alarm demonstration in this application are explained next.

#### In bluetooth.BleAdapterService

``` java
public static String EVENTSERVICE_SERVICE_UUID = "E95D93AF251D470AA062FA1922DFA9A8";
public static String MICROBITREQUIREMENTS_CHARACTERISTIC_UUID = "E95DB84C251D470AA062FA1922DFA9A8";
public static String MICROBITEVENT_CHARACTERISTIC_UUID = "E95D9775251D470AA062FA1922DFA9A8";
public static String CLIENTREQUIREMENTS_CHARACTERISTIC_UUID = "E95D23C4251D470AA062FA1922DFA9A8";
public static String CLIENTEVENT_CHARACTERISTIC_UUID = "E95D5404251D470AA062FA1922DFA9A8";
```

#### In ui.TemperatureAlarmActivity

```java
// event variables and values
private byte upper_limit;
private byte lower_limit;

// LE here means Little Endian btw

// micro:bit event codes:
// 9000 = 0x2823 (LE) = temperature alarm. Value=0 means OK, 1 means cold, 2 means hot

// client event codes:
// 9001=0x2923 (LE) = set lower limit, value is the limit value in celsius
// 9002=0x2A23 (LE) = set upper limit, value is the limit value in celsius

private byte [] event_set_lower = { 0x29, 0x23, 0x00, 0x00}; // event 9001
private byte [] event_set_upper = { 0x2A, 0x23, 0x00, 0x00}; // event 9002
```

``` java
// enabling microbit event notifications
bluetooth_le_adapter.setNotificationsState(
                    Utility.normaliseUUID(BleAdapterService.EVENTSERVICE_SERVICE_UUID), 
                    Utility.normaliseUUID(BleAdapterService.MICROBITEVENT_CHARACTERISTIC_UUID), true)                    
```
                       

``` java
// setting the upper and lower temperature limits 
private void setUpperLimit() {
    // set the value part of this event data
    event_set_upper[2] = Settings.getInstance().getUpper_temperature_limit();
    bluetooth_le_adapter.writeCharacteristic(Utility.normaliseUUID(BleAdapterService.EVENTSERVICE_SERVICE_UUID), Utility.normaliseUUID(BleAdapterService.CLIENTEVENT_CHARACTERISTIC_UUID), event_set_upper);
}

private void setLowerLimit() {
    // set the value part of this event data
    event_set_lower[2] = Settings.getInstance().getLower_temperature_limit();
    bluetooth_le_adapter.writeCharacteristic(Utility.normaliseUUID(BleAdapterService.EVENTSERVICE_SERVICE_UUID), Utility.normaliseUUID(BleAdapterService.CLIENTEVENT_CHARACTERISTIC_UUID), event_set_lower);
}
```

```java
// handling a MicrobitEvent notification indicating a temperature alarm of "too hot" or "too cold"
case BleAdapterService.NOTIFICATION_RECEIVED:
    bundle = msg.getData();
    service_uuid = bundle.getString(BleAdapterService.PARCEL_SERVICE_UUID);
    characteristic_uuid = bundle.getString(BleAdapterService.PARCEL_CHARACTERISTIC_UUID);
    b = bundle.getByteArray(BleAdapterService.PARCEL_VALUE);
    if (characteristic_uuid.equalsIgnoreCase((Utility.normaliseUUID(BleAdapterService.MICROBITEVENT_CHARACTERISTIC_UUID)))) {
        byte[] event_bytes = new byte[2];
        byte[] value_bytes = new byte[2];
        System.arraycopy(b, 0, event_bytes, 0, 2);
        System.arraycopy(b, 2, value_bytes, 0, 2);
        short event = Utility.shortFromLittleEndianBytes(event_bytes);
        short value = Utility.shortFromLittleEndianBytes(value_bytes);
        Log.d(Constants.TAG, "Temperature Alarm received: event=" + event + " value=" + value);
        if (event == Constants.MICROBIT_EVENT_TYPE_TEMPERATURE_ALARM) {
            setAlarmImage(alarm_image, value);
            setAlarmMessage(value);
        }
    }
    break;
```


#### Video Demonstration

<iframe src="https://player.vimeo.com/video/153072501" width="750" height="422" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>


