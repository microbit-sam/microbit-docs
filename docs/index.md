#Introduction

The micro:bit runtime provides an easy to use environment for programming the BBC micro:bit
in the C/C++ language, written by Lancaster University. It contains device drivers for all the hardware capabilities of the micro:bit,
and also a suite of runtime mechanisms to make programming the micro:bit easier and more flexible. These
range from control of the LED mtrix display to peer-to-peer radio communication and secure
Bluetooth Low Energy services. The micro:bit runtime is proudly built on the [ARM mbed](https://www.mbed.com)
and [Nordic nrf51](http://www.nordicsemi.com) platforms.

In addition to supporting development in C/C++, the runtime is also designed specifically to support
higher level languages provided by our partners that target the micro:bit. It is currently used as a support library for all the
languages on the BBC [www.microbit.co.uk](http://www.microbit.co.uk) website, including Microsoft Block, Microsoft TouchDevelop, Code Kingdoms
JavaScript and Micropython languages.

On these pages you will find guidance on how to start using the runtime in C/C++, summaries of all the
components that make up the system and a full set of API documentation (the functions you can use to control the micro:bit).

Just to show how easy it is to get started, here is how you would write a traditional Hello World program...

```cpp
   uBit.display.scroll("Hello micro:bit!");
```

Not so scary after all, eh?
So, see the getting started and concepts sections to learn more... then go and create!

#Getting Started

Developing with the micro:bit runtime is simple, and there are multiple ways to create programs for your device.

<div class="col-sm-6">
    <h3 id="online-environments">Online development</h3>
    <p>
        A basic quick start guide to getting an example project building in an
        online programming environment. No command line usage required.
    </p>
    <p>
        <a href="todo" class="btn btn-lg btn-outline">
            Online development tools
        </a>
    </p>
</div>
<div class="col-sm-6">
    <h3 id="offline-environments">Offline development</h3>
    <p>
        A full guide to installing offline development tools, and a tutorial on getting
        an example project building.
        <b>Requires setup with usage of the command line.</b>
    </p>
    <p>
        <a href="installing-yotta" class="btn btn-lg btn-outline">
            Offline development tools
        </a>
    </p>
</div>
