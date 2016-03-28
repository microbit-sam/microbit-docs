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
##Constructor
<br/>
####MicroBitStorage()
##writeBytes
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> writeBytes( <div style='color:#008080; display:inline-block'>uint8_t *</div> buffer,  <div style='color:#008080; display:inline-block'>uint32_t</div> address,  <div style='color:#008080; display:inline-block'>int</div> length)
#####Parameters

>  <div style='color:#008080; display:inline-block'>uint8_t *</div> *buffer*

>  <div style='color:#008080; display:inline-block'>uint32_t</div> *address*

>  <div style='color:#008080; display:inline-block'>int</div> *length*
##flashPageErase
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> flashPageErase( <div style='color:#008080; display:inline-block'>uint32_t *</div> page_address)
#####Description
Method for erasing a page in flash. 
#####Parameters

>  <div style='color:#008080; display:inline-block'>uint32_t *</div> *page_address* - Address of the first word in the page to be erased. 
##flashWordWrite
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> flashWordWrite( <div style='color:#008080; display:inline-block'>uint32_t *</div> address,  <div style='color:#008080; display:inline-block'>uint32_t</div> value)
#####Description
Method for writing a word of data in flash with a value.
#####Parameters

>  <div style='color:#008080; display:inline-block'>uint32_t *</div> *address* - Address of the word to change. 

>  <div style='color:#008080; display:inline-block'>uint32_t</div> *value* - Value to be written to flash. 
##put
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> put( <div style='color:#008080; display:inline-block'>const char *</div> key,  <div style='color:#008080; display:inline-block'>uint8_t *</div> data)
#####Description
Places a given key, and it's corresponding value into flash at the earliest available point.
#####Parameters

>  <div style='color:#008080; display:inline-block'>const char *</div> *key* - the unique name that should be used as an identifier for the given data. The key is presumed to be null terminated. 

>  <div style='color:#008080; display:inline-block'>uint8_t *</div> *data* - a pointer to the beginning of the data to be persisted.
#####Returns
MICROBIT_OK on success, or MICROBIT_NO_RESOURCES if our storage page is full 
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> put( <div style='color:#008080; display:inline-block'>ManagedString</div> key,  <div style='color:#008080; display:inline-block'>uint8_t *</div> data)
#####Description
Places a given key, and it's corresponding value into flash at the earliest available point.
#####Parameters

>  <div style='color:#008080; display:inline-block'>ManagedString</div> *key* - the unique name that should be used as an identifier for the given data. 

>  <div style='color:#008080; display:inline-block'>uint8_t *</div> *data* - a pointer to the beginning of the data to be persisted. 
##get
<br/>
####<div style='color:#FF69B4; display:inline-block'>KeyValuePair</div> get( <div style='color:#008080; display:inline-block'>const char *</div> key)
#####Description
Retreives a  KeyValuePair
#####Parameters

>  <div style='color:#008080; display:inline-block'>const char *</div> *key* - the unique name used to identify a  KeyValuePair  in flash.
#####Returns
a pointer to a heap allocated  KeyValuePair  struct, this pointer will be NULL if the key was not found in storage.

!!! note
    it is up to the user to free the returned struct. 

<br/>
####<div style='color:#FF69B4; display:inline-block'>KeyValuePair</div> get( <div style='color:#008080; display:inline-block'>ManagedString</div> key)
#####Description
Retreives a  KeyValuePair
#####Parameters

>  <div style='color:#008080; display:inline-block'>ManagedString</div> *key* - the unique name used to identify a  KeyValuePair  in flash.
#####Returns
a pointer to a heap allocated  KeyValuePair  struct, this pointer will be NULL if the key was not found in storage.

!!! note
    it is up to the user to free the returned struct. 

##remove
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> remove( <div style='color:#008080; display:inline-block'>const char *</div> key)
#####Description
Removes a  KeyValuePair
#####Parameters

>  <div style='color:#008080; display:inline-block'>const char *</div> *key* - the unique name used to identify a  KeyValuePair  in flash.
#####Returns
MICROBIT_OK on success, or MICROBIT_NO_DATA if the given key was not found in flash. 
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> remove( <div style='color:#008080; display:inline-block'>ManagedString</div> key)
#####Description
Removes a  KeyValuePair
#####Parameters

>  <div style='color:#008080; display:inline-block'>ManagedString</div> *key* - the unique name used to identify a  KeyValuePair  in flash.
#####Returns
MICROBIT_OK on success, or MICROBIT_NOT_SUPPORTED if the given key was not found in flash. 
##size
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> size()
#####Description
The size of the flash based  KeyValueStore
#####Returns
the number of entries in the key value store 
____
[comment]: <> ({"end":"MicroBitStorage"})
