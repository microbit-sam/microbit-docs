# Advanced micro:bit runtime 

Under the surface, the micro:bit runtime is a highly configurable, modular and component based piece of software.
The 'uBit' object is provided as a collection of the commonly used components, all gathered together in one place
to make it easier for novice users to access the funcitonality of the device. However, there is no obligation to
use the 'uBit' abstraction. More advanced users may prefer to create and use only the parts of the runtime they
need. This provides more control and often frees up more memory resource for the applicaiton program - but does so
at the expense of the user taking more responsibility and complexity in their programs.

## Using Components Directly

Taking advantage of the modular structure of the micro:bit runtime is fairly straightforward. 

 - Firstly, create a program that does **not** create or initialise a uBit object.
 - Include "MicroBit.h" (or if you prefer, just the header files of the components you want to use). Including "MicroBit.h" is however, simpler.
 - Instead, create c++ object instances of the classes that you want to use **as global variables** in your program. Create as many components as you need. You are free to use any of the constructors in this documentation.
 - Call functions on those instances to elicit the behaviour you need, using the name of your object instances instead of 'uBit.*'

For example, if you wanted to create a program that just used the LED matrix display driver, you might write a program like this:

```c++
#include "MicroBit.h"

MicroBitDisplay display;

int main()
{
    while(1)
        display.scroll(":)");
}
```

If you need other components, add them to your program in the same way. If a component has a dependency on another component (e.g. in the example below, the accelerometer is dependent on an I2C bus), then this will be requested as a mandatory parameter in the constructor. See the 'Constructor' section of the API documentation for details and examples. 


```c++
#include "MicroBit.h"

MicroBitI2C i2c = MicroBitI2C(I2C_SDA0, I2C_SCL0); 
MicroBitAccelerometer accelerometer = MicroBitAccelerometer(i2c); 
MicroBitDisplay display;

int main()
{
    while(1)
        display.scroll(accelerometer.getX());
}
```

!!! warning
    micro:bit runtime components should **always** be brought up as global variables. They should **not** be created as local variables - either in your main method or anywhere else. The reason for this is the the runtime is a multi-threaded environment, and any variables created in stack memory (like local variables) may be paged out by the scheduler, and result in instability if they interrupts or are accessed by other threads. So... don't do it! 


## System Components

There are also system components that provide background services. Without the 'uBit' object, these will not be created by default.  Examples include the fiber scheduler, message bus and heap allocator.  You are not required to initialise these components, but you should do so if you want to benefit from the functionality they provide. The following section describe how to do this:

## Initialising the Message Bus
The MessageBus allows events to be created and delivered to applications.  So if a message bus is not created, then all events in the micro:bit runtime will be quietly ignored. To enable this funcitonality, simply create an instance of the MessageBus class. From that point onward in your program, you can raised and listen for events as descibed in the [MicroBitMessageBus](ubit/messagebus.md) documentation.

```c++
#include "MicroBit.h"

MicroBitMessageBus bus;
MicroBitButton buttonA(MICROBIT_PIN_BUTTON_A, MICROBIT_ID_BUTTON_A);
MicroBitDisplay display;

void onPressed(MicroBitEvent e)
{
    display.print("S");    
}

int main()
{
    bus.listen(MICROBIT_ID_BUTTON_A, MICROBIT_BUTTON_EVT_CLICK, onPressed);
    
    while(1)
    {
    }
}
```

## Initialising the Fiber Scheduler
Often when using asychronpus events, it is also useful to run the fiber scheduler. Without a scheduler in operation, all event handler (such as the one above) will be executed with the threading mode MESSAGE_BUS_LISTENER_IMMEDIATE, as
described on the [MicroBitMessageBus](ubit/messagebus.md) page. Also, it is not really possible to transparently enter a power efficient sleep - as illustrated in the busy loop in the above example. Initialising the fiber scheduler can
be simply done as follows. From that moment on, it is then possible to blovk the processor in a power efficient way and to operate threaded event handlers:

Note that function calls to uBit.sleep() must be replaced with the direct, equivalent calls to the scheduler:

```c++
#include "MicroBit.h"

MicroBitMessageBus bus;
MicroBitButton buttonA(MICROBIT_PIN_BUTTON_A, MICROBIT_ID_BUTTON_A);
MicroBitDisplay display;

void onPressed(MicroBitEvent e)
{
    display.print("S");    
}

int main()
{
    scheduler_init(bus);

    bus.listen(MICROBIT_ID_BUTTON_A, MICROBIT_BUTTON_EVT_CLICK, onPressed);
    
    while(1)
        fiber_sleep(1000);
}
```

## Initialising the Heap Allocator
The micro:bit runtime provides an optional, heap memeory allocator. This is primarily to permit the use of **multiple** regions of memory to be used as heap memory space for your variables. The 'uBit' initialisation function will automatically release any memory unused by the BLE stack for general purpose use in this fashion (this typically provides an additiona 1K of SRAM under BLE enabled builds, and another 8K if BLE is disabled). Should you wish to also reclaim memory in this way, you can do so as follows:

```c++
#include "MicroBit.h"

int main()
{
    microbit_create_heap(MICROBIT_SD_GATT_TABLE_START + MICROBIT_SD_GATT_TABLE_SIZE, MICROBIT_SD_LIMIT);
}
```

## Compile Time Configuration Options
In addition to the flexibility to initialise only the components that you need, the runtime also provides a central, compile time configuration file called 'MicroBitConfig.h'. You can use this to reconfigure the default behaviour of the runtime. The default setting swill provide a stable woorking environment, but advanced users may want to further tailor the behaviour. Simply edit the 'MicroBitConfig.h' file to change the settings, and then perform a clean rebuild. The following options are configurable at compile time through this mechanism:

| Configuration option | Brief Description |
| ------------- |-------------|
| MICROBIT_HEAP_ALLOCATOR | Enables or disables the MicroBitHeapAllocator for 'uBit' based builds. |
| MICROBIT_HEAP_BLOCK_SIZE | The Block size used by the heap allocator in bytes. |
| MICROBIT_NESTED_HEAP_SIZE | The proportion of SRAM available on the mbed heap to reserve for the micro:bit heap. |
| MICROBIT_HEAP_REUSE_SD | If set to '1', any unused areas of the Soft Device GATT table will be automatically reused as heap memory. |
| MICROBIT_SD_GATT_TABLE_SIZE | The amount of memory (bytes) to dedicate to the SoftDevice GATT table. |
| SYSTEM_TICK_PERIOD_MS | The default scheduling quantum |
| EVENT_LISTENER_DEFAUT_FLAGS | The default threading mode used when a MessageBus listener is created. |
| MESSAGE_BUS_LISTENER_MAX_QUEUE_DEPTH | Maximum event queue depth. If a queue exceeds this depth, further events will be dropped. |
| MICROBIT_SYSTEM_COMPONENTS | The maximum size of interrupt callback list. |
| MICROBIT_IDLE_COMPONENTS | The maximum size of the idle callback list. |
| MICROBIT_BLE_ENABLED | Enable/Disable BLE during normal operation. If disabled, no BLE commuication is possible, but radio funcitonality is made possible, and an additional 8K of SRAM is released|
| MICROBIT_BLE_PAIRING_MODE | Enable/Disable BLE pairing mode with A+B / reset at power up|
| MICROBIT_BLE_PRIVATE_ADDRESSES | Enable/Disable the use of private resolvable addresses. n.b. This is known to be a feature that suffers compatibility issues with many BLE central devices. |
| MICROBIT_BLE_OPEN | Enable/Disable BLE security entirely. Open BLE links are not secure, but are highly useful during the development of BLE services|
| MICROBIT_BLE_SECURITY_LEVEL | Define the default, global BLE security requirements for MicroBit BLE services|
| MICROBIT_BLE_WHITELIST | Enable/Disbale the use of BLE whitelisting.|
| MICROBIT_BLE_ADVERTISING_TIMEOUT | Define the period of time for which the BLE stack will advertise (seconds).|
| MICROBIT_BLE_DEFAULT_TX_POWER | Defines default power level of the BLE radio transmitter.|
| MICROBIT_BLE_DFU_SERVICE | Enable/Disable BLE Service: MicroBitDFU. This allows over the air programming during normal operation.|
| MICROBIT_BLE_EVENT_SERVICE | Enable/Disable BLE Service: MicroBitEventService. This allows routing of events from the micro:bit message bus over BLE.|
| MICROBIT_BLE_DEVICE_INFORMATION_SERVICE | Enable/Disable BLE Service: MicroBitDeviceInformationService. This enables the standard BLE device information service.|
| USE_ACCEL_LSB | Enable 10 bit sampling on the accelerometer. By default, a more efficienct 8 bit sampling if used.|
| MICROBIT_DISPLAY_TYPE | Selects the default matrix configuration for the display driver.|
| MICROBIT_DISPLAY_MINIMUM_BRIGHTNESS | Selects the minimum permissable brightness level for the device.|
| MICROBIT_DISPLAY_MAXIMUM_BRIGHTNESS | Selects the maximum permissable brightness level for the device.|
| MICROBIT_DISPLAY_DEFAULT_BRIGHTNESS | Selects the default brightness level for the device.|
| MICROBIT_DEFAULT_SCROLL_SPEED | Selects the time taken to scroll a single pixel, in milliseconds.|
| MICROBIT_DEFAULT_SCROLL_STRIDE | Selects the number of pixels a scroll will move in each quantum.|
| MICROBIT_DEFAULT_PRINT_SPEED | Selects the time each character will be shown on the display during print operations, in milliseconds.|
| MICROBIT_DEFAULT_SERIAL_MODE | Configures the default serial mode used by serial read and send calls.|
| MICROBIT_PANIC_HEAP_FULL | Enable this to invoke a panic on out of memory conditions.|
| MICROBIT_DBG | Enable this to route debug messages through the USB serial interface.|
| MICROBIT_HEAP_DBG | Enable this to receive detailed diagnostic messages from the heap allocator via the USB serial interface.|
| MICROBIT_DAL_VERSION | Define vdefault version informaiton the the runtime.|


There are also some constants that define the geometry of the micro:bit memory... Only change these if you really know what you are doing!

| Configuration option | Brief Description |
| ------------- |-------------|
| MICROBIT_SRAM_BASE |  The start address of usable RAM memory. |
| MICROBIT_SRAM_END |  The end address of usable RAM memory. |
| MICROBIT_SD_LIMIT |  The end address of RAM memory reserved for Soft Device (Nordic's Bluetooth stack). |
| MICROBIT_SD_GATT_TABLE_START |  The start address of the BLE GATT table in RAM memory. |
| CORTEX_M0_STACK_BASE | The memory address of the top of the system stack. |
| MICROBIT_STACK_SIZE | Amount of memory reserved for the stack (in bytes). |
| MICROBIT_HEAP_END | The end address of the mbed heap space |

