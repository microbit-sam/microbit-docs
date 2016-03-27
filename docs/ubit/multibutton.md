#uBit.buttonAB

##Overview

A `MicroBitMultiButton` mirrors the state of two [`MicroBitButton`](button.md)s
using the message bus eventing mechanism. It provides a similar API and emits
the same events as as a [`MicroBitButton`](button.md).


##Message Bus ID
| Constant | Value |
| ------------- |-------------|
| MICROBIT_ID_BUTTON_AB | 26 |

##Message Bus Events

| Constant | Value |
| ------------- |-------------|
| MICROBIT_BUTTON_EVT_DOWN | 1 |
| MICROBIT_BUTTON_EVT_UP | 2 |
| MICROBIT_BUTTON_EVT_CLICK | 3 |
| MICROBIT_BUTTON_EVT_LONG_CLICK | 4 |
| MICROBIT_BUTTON_EVT_HOLD | 5 |
| MICROBIT_BUTTON_EVT_DOUBLE_CLICK | 6 |

##API
[comment]: <> ({"className":"MicroBitMultiButton"})
[comment]: <> ({"end":"MicroBitMultiButton"})
