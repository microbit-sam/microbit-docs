#uBit.radio

##Overview

##Message Bus ID

##Message Bus Events

#API
[comment]: <> ({"className":"MicroBitRadio"})
____
##Constructor
<br/>
####MicroBitRadio( <div style='color:#008080; display:inline-block'>uint16_t</div> id)
<br/>
#####Description
Constructor.

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *id*

<br/><br/>
____
##setTransmitPower
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> setTransmitPower( <div style='color:#008080; display:inline-block'>int</div> power)
<br/>
#####Description
Change the output power level of the transmitter to the given value.

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *power* - a value in the range 0..7, where 0 is the lowest power and 7 is the highest. 

<br/><br/>
#####Returns
MICROBIT_OK on success, or MICROBIT_INVALID_PARAMETER if the value is out of range. 

<br/><br/>
____
##setFrequencyBand
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> setFrequencyBand( <div style='color:#008080; display:inline-block'>int</div> band)
<br/>
#####Description
Change the transmission and reception band of the radio to the given channel

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *band* - a frequency band in the range 0 - 100. Each step is 1MHz wide, based at 2400MHz. 

<br/><br/>
#####Returns
MICROBIT_OK on success, or MICROBIT_INVALID_PARAMETER if the value is out of range, or MICROBIT_NOT_SUPPORTED if the BLE stack is running. 

<br/><br/>
____
##getRxBuf
<br/>
####<div style='color:#FF69B4; display:inline-block'>FrameBuffer</div> getRxBuf()
<br/>
#####Description
Retrieve a pointer to the currently allocated recieve buffer. This is the area of memory actively being used by the radio hardware to store incoming data.

<br/><br/>
#####Returns
a pointer to the current receive buffer

<br/><br/>
____
##queueRxBuf
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> queueRxBuf()
<br/>
#####Description
Attempt to queue a buffer received by the radio hardware, if sufficient space is available.

<br/><br/>
#####Returns
MICROBIT_OK on success, or MICROBIT_NO_RESOURCES if a replacement receiver buffer could not be allocated (either by policy or memory exhaustion). 

<br/><br/>
____
##setRSSI
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> setRSSI( <div style='color:#008080; display:inline-block'>uint8_t</div> rssi)
<br/>
#####Description
Sets the RSSI for the most recent packet.

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>uint8_t</div> *rssi* - the new rssi value

<br/><br/>

!!! note
    should only be called from RADIO_IRQHandler... 
<br/><br/>
____
##getRSSI
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getRSSI()
<br/>
#####Description
Retrieves the current RSSI for the most recent packet. 

<br/><br/>
____
##enable
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> enable()
<br/>
#####Description
Initialises the radio for use as a multipoint sender/receiver 

<br/><br/>
#####Returns
MICROBIT_OK on success, MICROBIT_NOT_SUPPORTED if SoftDevice is enabled.

<br/><br/>
____
##disable
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> disable()
<br/>
#####Description
Disables the radio for use as a multipoint sender/receiver. 

<br/><br/>
#####Returns
MICROBIT_OK on success, MICROBIT_NOT_SUPPORTED if SoftDevice is enabled. 

<br/><br/>
____
##setGroup
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> setGroup( <div style='color:#008080; display:inline-block'>uint8_t</div> group)
<br/>
#####Description
Sets the radio to listen to packets sent with the given group id.

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>uint8_t</div> *group* - The group to join. A micro:bit can only listen to one group ID at any time. 

<br/><br/>
#####Returns
MICROBIT_OK on success, or MICROBIT_NOT_SUPPORTED if the BLE stack is running. 

<br/><br/>
____
##dataReady
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> dataReady()
<br/>
#####Description
Determines the number of packets ready to be processed. 

<br/><br/>
#####Returns
The number of packets in the receive buffer. 

<br/><br/>
____
##recv
<br/>
####<div style='color:#FF69B4; display:inline-block'>FrameBuffer</div> recv()
<br/>
#####Description
Retrieves the next packet from the receive buffer. If a data packet is available, then it will be returned immediately to the caller. This call will also dequeue the buffer.

<br/><br/>
#####Returns
The buffer containing the the packet. If no data is available, NULL is returned. 

<br/><br/>
____
##send
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> send( <div style='color:#008080; display:inline-block'>FrameBuffer  *</div> buffer)
<br/>
#####Description
Transmits the given buffer onto the broadcast radio. The call will wait until the transmission of the packet has completed before returning.

<br/><br/>
#####Parameters

>  <div style='color:#008080; display:inline-block'>FrameBuffer  *</div> *buffer*

<br/><br/>
#####Returns
MICROBIT_OK on success, or MICROBIT_NOT_SUPPORTED if the BLE stack is running. 

<br/><br/>
____
[comment]: <> ({"end":"MicroBitRadio"})
