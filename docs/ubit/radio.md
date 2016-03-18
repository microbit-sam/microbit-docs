#uBit.radio

##Overview

##Message Bus ID

##Message Bus Events

#API
[comment]: <> ({"className":"MicroBitRadio"})
##Constructor
<br/>
####MicroBitRadio( <div style='color:#008080; display:inline-block'>uint16_t</div> id)
#####Description
Constructor.
#####Parameters

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *id*
##setTransmitPower
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> setTransmitPower( <div style='color:#008080; display:inline-block'>int</div> power)
#####Description
Change the output power level of the transmitter to the given value.
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *power* - a value in the range 0..7, where 0 is the lowest power and 7 is the highest. 
#####Returns
MICROBIT_OK on success, or MICROBIT_INVALID_PARAMETER if the value is out of range. 
##setFrequencyBand
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> setFrequencyBand( <div style='color:#008080; display:inline-block'>int</div> band)
#####Description
Change the transmission and reception band of the radio to the given channel
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *band* - a frequency band in the range 0 - 100. Each step is 1MHz wide, based at 2400MHz. 
#####Returns
MICROBIT_OK on success, or MICROBIT_INVALID_PARAMETER if the value is out of range, or MICROBIT_NOT_SUPPORTED if the BLE stack is running. 
##getRxBuf
<br/>
####<div style='color:#FF69B4; display:inline-block'>FrameBuffer</div> getRxBuf()
#####Description
Retrieve a pointer to the currently allocated recieve buffer. This is the area of memory actively being used by the radio hardware to store incoming data.
#####Returns
a pointer to the current receive buffer
##queueRxBuf
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> queueRxBuf()
#####Description
Attempt to queue a buffer received by the radio hardware, if sufficient space is available.
#####Returns
MICROBIT_OK on success, or MICROBIT_NO_RESOURCES if a replacement receiver buffer could not be allocated (either by policy or memory exhaustion). 
##setRSSI
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> setRSSI( <div style='color:#008080; display:inline-block'>uint8_t</div> rssi)
#####Description
Sets the RSSI for the most recent packet.
#####Parameters

>  <div style='color:#008080; display:inline-block'>uint8_t</div> *rssi* - the new rssi value

!!! note
    should only be called from RADIO_IRQHandler... 

##getRSSI
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getRSSI()
#####Description
Retrieves the current RSSI for the most recent packet. 
##enable
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> enable()
#####Description
Initialises the radio for use as a multipoint sender/receiver 
#####Returns
MICROBIT_OK on success, MICROBIT_NOT_SUPPORTED if SoftDevice is enabled.
##disable
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> disable()
#####Description
Disables the radio for use as a multipoint sender/receiver. 
#####Returns
MICROBIT_OK on success, MICROBIT_NOT_SUPPORTED if SoftDevice is enabled. 
##setGroup
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> setGroup( <div style='color:#008080; display:inline-block'>uint8_t</div> group)
#####Description
Sets the radio to listen to packets sent with the given group id.
#####Parameters

>  <div style='color:#008080; display:inline-block'>uint8_t</div> *group* - The group to join. A micro:bit can only listen to one group ID at any time. 
#####Returns
MICROBIT_OK on success, or MICROBIT_NOT_SUPPORTED if the BLE stack is running. 
##dataReady
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> dataReady()
#####Description
Determines the number of packets ready to be processed. 
#####Returns
The number of packets in the receive buffer. 
##recv
<br/>
####<div style='color:#FF69B4; display:inline-block'>FrameBuffer</div> recv()
#####Description
Retrieves the next packet from the receive buffer. If a data packet is available, then it will be returned immediately to the caller. This call will also dequeue the buffer.
#####Returns
The buffer containing the the packet. If no data is available, NULL is returned. 
##send
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> send( <div style='color:#008080; display:inline-block'>FrameBuffer  *</div> buffer)
#####Description
Transmits the given buffer onto the broadcast radio. The call will wait until the transmission of the packet has completed before returning.
#####Parameters

>  <div style='color:#008080; display:inline-block'>FrameBuffer  *</div> *buffer*
#####Returns
MICROBIT_OK on success, or MICROBIT_NOT_SUPPORTED if the BLE stack is running. 
____
[comment]: <> ({"end":"MicroBitRadio"})
