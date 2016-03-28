#uBit.display

##Overview

`MicroBitDisplay` drives a 5 by 5 matrix of Light Emitting Diodes (LEDs) primarily
used for conveying information.

The display is architected with 3 rows, each with 9 columns. This is illustrated
below:

![light-sensing info graphic](../resources/light-sensing.png)

<center>*Where the format is: **ROW**.**COLUMN***</center>

##Message Bus ID

| Constant | Value |
| ------------- |-------------|
| MICROBIT_ID_DISPLAY | 6 |

##Message Bus Events

| Constant | Value |
| ------------- |-------------|
| MICROBIT_DISPLAY_EVT_ANIMATION_COMPLETE | 1 |
| MICROBIT_DISPLAY_EVT_LIGHT_SENSE | 2 |

## Notify Events

These events use the notification channel `MICROBIT_ID_NOTIFY`, which provides
general purpose synchronisation.

| Constant | Value |
| ------------- |-------------|
| MICROBIT_DISPLAY_EVT_FREE | 1 |

##API
[comment]: <> ({"className":"MicroBitDisplay"})
##Constructor
<br/>
####MicroBitDisplay()
#####Description
Constructor. Create a representation of a display of a given size. The display is initially blank.
#####Example
```cpp
 MicroBitDisplay display(MICROBIT_ID_DISPLAY, microbitMatrixMap), 

```
<br/>
####MicroBitDisplay( <div style='color:#008080; display:inline-block'>uint16_t</div> id)
#####Description
Constructor. Create a representation of a display of a given size. The display is initially blank.
#####Parameters

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *id* - The ID display should use when sending events on the MessageBus. 
#####Example
```cpp
 MicroBitDisplay display(MICROBIT_ID_DISPLAY, microbitMatrixMap), 

```
<br/>
####MicroBitDisplay( <div style='color:#008080; display:inline-block'>uint16_t</div> id,  <div style='color:#008080; display:inline-block'>const  MatrixMap  &</div> map)
#####Description
Constructor. Create a representation of a display of a given size. The display is initially blank.
#####Parameters

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *id* - The ID display should use when sending events on the MessageBus. 

>  <div style='color:#008080; display:inline-block'>const  MatrixMap  &</div> *map* - The mapping information that relates pin inputs/outputs to physical screen coordinates.
#####Example
```cpp
 MicroBitDisplay display(MICROBIT_ID_DISPLAY, microbitMatrixMap), 

```
##stopAnimation
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> stopAnimation()
#####Description
Stops any currently running animation, and any that are waiting to be displayed. 
##printCharAsync
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> printCharAsync( <div style='color:#008080; display:inline-block'>char</div> c)
#####Description
Prints the given character to the display, if it is not in use.
#####Parameters

>  <div style='color:#008080; display:inline-block'>char</div> *c* - The character to display. 
#####Returns
MICROBIT_OK, MICROBIT_BUSY is the screen is in use, or MICROBIT_INVALID_PARAMETER.
#####Example
```cpp
 uBit.display.printAsync('p'); 
 uBit.display.printAsync('p',100); 

```
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> printCharAsync( <div style='color:#008080; display:inline-block'>char</div> c,  <div style='color:#008080; display:inline-block'>int</div> delay)
#####Description
Prints the given character to the display, if it is not in use.
#####Parameters

>  <div style='color:#008080; display:inline-block'>char</div> *c* - The character to display. 

>  <div style='color:#008080; display:inline-block'>int</div> *delay* - Optional parameter - the time for which to show the character. Zero displays the character forever. 
#####Returns
MICROBIT_OK, MICROBIT_BUSY is the screen is in use, or MICROBIT_INVALID_PARAMETER.
#####Example
```cpp
 uBit.display.printAsync('p'); 
 uBit.display.printAsync('p',100); 

```
##printAsync
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> printAsync( <div style='color:#008080; display:inline-block'>ManagedString</div> s)
#####Description
Prints the given string to the display, one character at a time. Uses the given delay between characters. Returns immediately, and executes the animation asynchronously.
#####Parameters

>  <div style='color:#008080; display:inline-block'>ManagedString</div> *s* - The string to display. 
#####Returns
MICROBIT_OK, or MICROBIT_INVALID_PARAMETER.
#####Example
```cpp
 uBit.display.printAsync("abc123",400); 

```
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> printAsync( <div style='color:#008080; display:inline-block'>ManagedString</div> s,  <div style='color:#008080; display:inline-block'>int</div> delay)
#####Description
Prints the given string to the display, one character at a time. Uses the given delay between characters. Returns immediately, and executes the animation asynchronously.
#####Parameters

>  <div style='color:#008080; display:inline-block'>ManagedString</div> *s* - The string to display. 

>  <div style='color:#008080; display:inline-block'>int</div> *delay* - The time to delay between characters, in milliseconds. Must be > 0. 
#####Returns
MICROBIT_OK, or MICROBIT_INVALID_PARAMETER.
#####Example
```cpp
 uBit.display.printAsync("abc123",400); 

```
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> printAsync( <div style='color:#008080; display:inline-block'>MicroBitImage</div> i,  <div style='color:#008080; display:inline-block'>int</div> x,  <div style='color:#008080; display:inline-block'>int</div> y,  <div style='color:#008080; display:inline-block'>int</div> alpha)
#####Description
Prints the given image to the display, if the display is not in use. Returns immediately, and executes the animation asynchronously.
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitImage</div> *i* - The image to display. 

>  <div style='color:#008080; display:inline-block'>int</div> *x* - The horizontal position on the screen to display the image (default 0) 

>  <div style='color:#008080; display:inline-block'>int</div> *y* - The vertical position on the screen to display the image (default 0) 

>  <div style='color:#008080; display:inline-block'>int</div> *alpha* - Treats the brightness level '0' as transparent (default 0) 
#####Example
```cpp
 MicrobitImage i("1,1,1,1,1\n1,1,1,1,1\n"); 
 uBit.display.print(i,400); 

```
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> printAsync( <div style='color:#008080; display:inline-block'>MicroBitImage</div> i,  <div style='color:#008080; display:inline-block'>int</div> x,  <div style='color:#008080; display:inline-block'>int</div> y,  <div style='color:#008080; display:inline-block'>int</div> alpha,  <div style='color:#008080; display:inline-block'>int</div> delay)
#####Description
Prints the given image to the display, if the display is not in use. Returns immediately, and executes the animation asynchronously.
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitImage</div> *i* - The image to display. 

>  <div style='color:#008080; display:inline-block'>int</div> *x* - The horizontal position on the screen to display the image (default 0) 

>  <div style='color:#008080; display:inline-block'>int</div> *y* - The vertical position on the screen to display the image (default 0) 

>  <div style='color:#008080; display:inline-block'>int</div> *alpha* - Treats the brightness level '0' as transparent (default 0) 

>  <div style='color:#008080; display:inline-block'>int</div> *delay* - The time to delay between characters, in milliseconds. set to 0 to display forever. (default 0).
#####Example
```cpp
 MicrobitImage i("1,1,1,1,1\n1,1,1,1,1\n"); 
 uBit.display.print(i,400); 

```
##printChar
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> printChar( <div style='color:#008080; display:inline-block'>char</div> c)
#####Description
Prints the given character to the display.
#####Parameters

>  <div style='color:#008080; display:inline-block'>char</div> *c* - The character to display. 
#####Returns
MICROBIT_OK, MICROBIT_CANCELLED or MICROBIT_INVALID_PARAMETER.
#####Example
```cpp
 uBit.display.print('p'); 

```
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> printChar( <div style='color:#008080; display:inline-block'>char</div> c,  <div style='color:#008080; display:inline-block'>int</div> delay)
#####Description
Prints the given character to the display.
#####Parameters

>  <div style='color:#008080; display:inline-block'>char</div> *c* - The character to display. 

>  <div style='color:#008080; display:inline-block'>int</div> *delay* - The time to delay between characters, in milliseconds. Must be > 0. 
#####Returns
MICROBIT_OK, MICROBIT_CANCELLED or MICROBIT_INVALID_PARAMETER.
#####Example
```cpp
 uBit.display.print('p'); 

```
##print
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> print( <div style='color:#008080; display:inline-block'>ManagedString</div> s)
#####Description
Prints the given string to the display, one character at a time. Uses the given delay between characters. Blocks the calling thread until all the text has been displayed.
#####Parameters

>  <div style='color:#008080; display:inline-block'>ManagedString</div> *s* - The string to display. 
#####Returns
MICROBIT_OK, MICROBIT_CANCELLED or MICROBIT_INVALID_PARAMETER.
#####Example
```cpp
 uBit.display.print("abc123",400); 

```
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> print( <div style='color:#008080; display:inline-block'>ManagedString</div> s,  <div style='color:#008080; display:inline-block'>int</div> delay)
#####Description
Prints the given string to the display, one character at a time. Uses the given delay between characters. Blocks the calling thread until all the text has been displayed.
#####Parameters

>  <div style='color:#008080; display:inline-block'>ManagedString</div> *s* - The string to display. 

>  <div style='color:#008080; display:inline-block'>int</div> *delay* - The time to delay between characters, in milliseconds. Must be > 0. 
#####Returns
MICROBIT_OK, MICROBIT_CANCELLED or MICROBIT_INVALID_PARAMETER.
#####Example
```cpp
 uBit.display.print("abc123",400); 

```
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> print( <div style='color:#008080; display:inline-block'>MicroBitImage</div> i,  <div style='color:#008080; display:inline-block'>int</div> x,  <div style='color:#008080; display:inline-block'>int</div> y,  <div style='color:#008080; display:inline-block'>int</div> alpha)
#####Description
Prints the given image to the display. Blocks the calling thread until all the text has been displayed.
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitImage</div> *i* - The image to display. 

>  <div style='color:#008080; display:inline-block'>int</div> *x*

>  <div style='color:#008080; display:inline-block'>int</div> *y*

>  <div style='color:#008080; display:inline-block'>int</div> *alpha*
#####Returns
MICROBIT_OK, MICROBIT_BUSY if the display is already in use, or MICROBIT_INVALID_PARAMETER.
#####Example
```cpp
 MicrobitImage i("1,1,1,1,1\n1,1,1,1,1\n"); 
 uBit.display.print(i,400); 

```
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> print( <div style='color:#008080; display:inline-block'>MicroBitImage</div> i,  <div style='color:#008080; display:inline-block'>int</div> x,  <div style='color:#008080; display:inline-block'>int</div> y,  <div style='color:#008080; display:inline-block'>int</div> alpha,  <div style='color:#008080; display:inline-block'>int</div> delay)
#####Description
Prints the given image to the display. Blocks the calling thread until all the text has been displayed.
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitImage</div> *i* - The image to display. 

>  <div style='color:#008080; display:inline-block'>int</div> *x*

>  <div style='color:#008080; display:inline-block'>int</div> *y*

>  <div style='color:#008080; display:inline-block'>int</div> *alpha*

>  <div style='color:#008080; display:inline-block'>int</div> *delay* - The time to display the image for, or zero to show the image forever. Must be >= 0. 
#####Returns
MICROBIT_OK, MICROBIT_BUSY if the display is already in use, or MICROBIT_INVALID_PARAMETER.
#####Example
```cpp
 MicrobitImage i("1,1,1,1,1\n1,1,1,1,1\n"); 
 uBit.display.print(i,400); 

```
##scrollAsync
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> scrollAsync( <div style='color:#008080; display:inline-block'>ManagedString</div> s)
#####Description
Scrolls the given string to the display, from right to left. Uses the given delay between characters. Returns immediately, and executes the animation asynchronously.
#####Parameters

>  <div style='color:#008080; display:inline-block'>ManagedString</div> *s* - The string to display. 
#####Returns
MICROBIT_OK, MICROBIT_BUSY if the display is already in use, or MICROBIT_INVALID_PARAMETER.
#####Example
```cpp
 uBit.display.scrollAsync("abc123",100); 

```
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> scrollAsync( <div style='color:#008080; display:inline-block'>ManagedString</div> s,  <div style='color:#008080; display:inline-block'>int</div> delay)
#####Description
Scrolls the given string to the display, from right to left. Uses the given delay between characters. Returns immediately, and executes the animation asynchronously.
#####Parameters

>  <div style='color:#008080; display:inline-block'>ManagedString</div> *s* - The string to display. 

>  <div style='color:#008080; display:inline-block'>int</div> *delay* - The time to delay between each update to the display, in milliseconds. Must be > 0. 
#####Returns
MICROBIT_OK, MICROBIT_BUSY if the display is already in use, or MICROBIT_INVALID_PARAMETER.
#####Example
```cpp
 uBit.display.scrollAsync("abc123",100); 

```
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> scrollAsync( <div style='color:#008080; display:inline-block'>MicroBitImage</div> image)
#####Description
Scrolls the given image across the display, from right to left. Returns immediately, and executes the animation asynchronously.
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitImage</div> *image* - The image to display. 
#####Returns
MICROBIT_OK, MICROBIT_BUSY if the display is already in use, or MICROBIT_INVALID_PARAMETER.
#####Example
```cpp
 MicrobitImage i("1,1,1,1,1\n1,1,1,1,1\n"); 
 uBit.display.scrollAsync(i,100,1); 

```
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> scrollAsync( <div style='color:#008080; display:inline-block'>MicroBitImage</div> image,  <div style='color:#008080; display:inline-block'>int</div> delay)
#####Description
Scrolls the given image across the display, from right to left. Returns immediately, and executes the animation asynchronously.
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitImage</div> *image* - The image to display. 

>  <div style='color:#008080; display:inline-block'>int</div> *delay* - The time to delay between each update to the display, in milliseconds. Must be > 0. 
#####Returns
MICROBIT_OK, MICROBIT_BUSY if the display is already in use, or MICROBIT_INVALID_PARAMETER.
#####Example
```cpp
 MicrobitImage i("1,1,1,1,1\n1,1,1,1,1\n"); 
 uBit.display.scrollAsync(i,100,1); 

```
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> scrollAsync( <div style='color:#008080; display:inline-block'>MicroBitImage</div> image,  <div style='color:#008080; display:inline-block'>int</div> delay,  <div style='color:#008080; display:inline-block'>int</div> stride)
#####Description
Scrolls the given image across the display, from right to left. Returns immediately, and executes the animation asynchronously.
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitImage</div> *image* - The image to display. 

>  <div style='color:#008080; display:inline-block'>int</div> *delay* - The time to delay between each update to the display, in milliseconds. Must be > 0. 

>  <div style='color:#008080; display:inline-block'>int</div> *stride* - The number of pixels to move in each update. Default value is the screen width. 
#####Returns
MICROBIT_OK, MICROBIT_BUSY if the display is already in use, or MICROBIT_INVALID_PARAMETER.
#####Example
```cpp
 MicrobitImage i("1,1,1,1,1\n1,1,1,1,1\n"); 
 uBit.display.scrollAsync(i,100,1); 

```
##scroll
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> scroll( <div style='color:#008080; display:inline-block'>ManagedString</div> s)
#####Description
Scrolls the given string to the display, from right to left. Uses the given delay between characters. Blocks the calling thread until all the text has been displayed.
#####Parameters

>  <div style='color:#008080; display:inline-block'>ManagedString</div> *s* - The string to display. 
#####Returns
MICROBIT_OK, MICROBIT_CANCELLED or MICROBIT_INVALID_PARAMETER.
#####Example
```cpp
 uBit.display.scroll("abc123",100); 

```
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> scroll( <div style='color:#008080; display:inline-block'>ManagedString</div> s,  <div style='color:#008080; display:inline-block'>int</div> delay)
#####Description
Scrolls the given string to the display, from right to left. Uses the given delay between characters. Blocks the calling thread until all the text has been displayed.
#####Parameters

>  <div style='color:#008080; display:inline-block'>ManagedString</div> *s* - The string to display. 

>  <div style='color:#008080; display:inline-block'>int</div> *delay* - The time to delay between each update to the display, in milliseconds. Must be > 0. 
#####Returns
MICROBIT_OK, MICROBIT_CANCELLED or MICROBIT_INVALID_PARAMETER.
#####Example
```cpp
 uBit.display.scroll("abc123",100); 

```
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> scroll( <div style='color:#008080; display:inline-block'>MicroBitImage</div> image)
#####Description
Scrolls the given image across the display, from right to left. Blocks the calling thread until all the text has been displayed.
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitImage</div> *image* - The image to display. 
#####Returns
MICROBIT_OK, MICROBIT_CANCELLED or MICROBIT_INVALID_PARAMETER.
#####Example
```cpp
 MicrobitImage i("1,1,1,1,1\n1,1,1,1,1\n"); 
 uBit.display.scroll(i,100,1); 

```
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> scroll( <div style='color:#008080; display:inline-block'>MicroBitImage</div> image,  <div style='color:#008080; display:inline-block'>int</div> delay)
#####Description
Scrolls the given image across the display, from right to left. Blocks the calling thread until all the text has been displayed.
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitImage</div> *image* - The image to display. 

>  <div style='color:#008080; display:inline-block'>int</div> *delay* - The time to delay between each update to the display, in milliseconds. Must be > 0. 
#####Returns
MICROBIT_OK, MICROBIT_CANCELLED or MICROBIT_INVALID_PARAMETER.
#####Example
```cpp
 MicrobitImage i("1,1,1,1,1\n1,1,1,1,1\n"); 
 uBit.display.scroll(i,100,1); 

```
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> scroll( <div style='color:#008080; display:inline-block'>MicroBitImage</div> image,  <div style='color:#008080; display:inline-block'>int</div> delay,  <div style='color:#008080; display:inline-block'>int</div> stride)
#####Description
Scrolls the given image across the display, from right to left. Blocks the calling thread until all the text has been displayed.
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitImage</div> *image* - The image to display. 

>  <div style='color:#008080; display:inline-block'>int</div> *delay* - The time to delay between each update to the display, in milliseconds. Must be > 0. 

>  <div style='color:#008080; display:inline-block'>int</div> *stride* - The number of pixels to move in each update. Default value is the screen width. 
#####Returns
MICROBIT_OK, MICROBIT_CANCELLED or MICROBIT_INVALID_PARAMETER.
#####Example
```cpp
 MicrobitImage i("1,1,1,1,1\n1,1,1,1,1\n"); 
 uBit.display.scroll(i,100,1); 

```
##animateAsync
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> animateAsync( <div style='color:#008080; display:inline-block'>MicroBitImage</div> image,  <div style='color:#008080; display:inline-block'>int</div> delay,  <div style='color:#008080; display:inline-block'>int</div> stride)
#####Description
"Animates" the current image across the display with a given stride, finishing on the last frame of the animation. Returns immediately.
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitImage</div> *image* - The image to display. 

>  <div style='color:#008080; display:inline-block'>int</div> *delay* - The time to delay between each update to the display, in milliseconds. Must be > 0. 

>  <div style='color:#008080; display:inline-block'>int</div> *stride* - The number of pixels to move in each update. Default value is the screen width. 
#####Returns
MICROBIT_OK, MICROBIT_BUSY if the screen is in use, or MICROBIT_INVALID_PARAMETER.
#####Example
```cpp
 const int heart_w = 10; 
 const int heart_h = 5; 
 const uint8_t heart[] = { 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, }; 
 
 MicroBitImage i(heart_w,heart_h,heart); 
 uBit.display.animateAsync(i,100,5); 

```
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> animateAsync( <div style='color:#008080; display:inline-block'>MicroBitImage</div> image,  <div style='color:#008080; display:inline-block'>int</div> delay,  <div style='color:#008080; display:inline-block'>int</div> stride,  <div style='color:#008080; display:inline-block'>int</div> startingPosition)
#####Description
"Animates" the current image across the display with a given stride, finishing on the last frame of the animation. Returns immediately.
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitImage</div> *image* - The image to display. 

>  <div style='color:#008080; display:inline-block'>int</div> *delay* - The time to delay between each update to the display, in milliseconds. Must be > 0. 

>  <div style='color:#008080; display:inline-block'>int</div> *stride* - The number of pixels to move in each update. Default value is the screen width. 

>  <div style='color:#008080; display:inline-block'>int</div> *startingPosition*
#####Returns
MICROBIT_OK, MICROBIT_BUSY if the screen is in use, or MICROBIT_INVALID_PARAMETER.
#####Example
```cpp
 const int heart_w = 10; 
 const int heart_h = 5; 
 const uint8_t heart[] = { 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, }; 
 
 MicroBitImage i(heart_w,heart_h,heart); 
 uBit.display.animateAsync(i,100,5); 

```
##animate
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> animate( <div style='color:#008080; display:inline-block'>MicroBitImage</div> image,  <div style='color:#008080; display:inline-block'>int</div> delay,  <div style='color:#008080; display:inline-block'>int</div> stride)
#####Description
"Animates" the current image across the display with a given stride, finishing on the last frame of the animation. Blocks the calling thread until the animation is complete.
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitImage</div> *image* - The image to display. 

>  <div style='color:#008080; display:inline-block'>int</div> *delay* - The time to delay between each update to the display, in milliseconds. Must be > 0. 

>  <div style='color:#008080; display:inline-block'>int</div> *stride* - The number of pixels to move in each update. Default value is the screen width. 
#####Returns
MICROBIT_OK, MICROBIT_CANCELLED or MICROBIT_INVALID_PARAMETER.
#####Example
```cpp
 const int heart_w = 10; 
 const int heart_h = 5; 
 const uint8_t heart[] = { 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, }; 
 
 MicroBitImage i(heart_w,heart_h,heart); 
 uBit.display.animate(i,100,5); 

```
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> animate( <div style='color:#008080; display:inline-block'>MicroBitImage</div> image,  <div style='color:#008080; display:inline-block'>int</div> delay,  <div style='color:#008080; display:inline-block'>int</div> stride,  <div style='color:#008080; display:inline-block'>int</div> startingPosition)
#####Description
"Animates" the current image across the display with a given stride, finishing on the last frame of the animation. Blocks the calling thread until the animation is complete.
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitImage</div> *image* - The image to display. 

>  <div style='color:#008080; display:inline-block'>int</div> *delay* - The time to delay between each update to the display, in milliseconds. Must be > 0. 

>  <div style='color:#008080; display:inline-block'>int</div> *stride* - The number of pixels to move in each update. Default value is the screen width. 

>  <div style='color:#008080; display:inline-block'>int</div> *startingPosition*
#####Returns
MICROBIT_OK, MICROBIT_CANCELLED or MICROBIT_INVALID_PARAMETER.
#####Example
```cpp
 const int heart_w = 10; 
 const int heart_h = 5; 
 const uint8_t heart[] = { 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, }; 
 
 MicroBitImage i(heart_w,heart_h,heart); 
 uBit.display.animate(i,100,5); 

```
##setBrightness
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> setBrightness( <div style='color:#008080; display:inline-block'>int</div> b)
#####Description
Sets the display brightness to the specified level. 
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *b* - The brightness to set the brightness to, in the range 0..255. 
#####Returns
MICROBIT_OK, or MICROBIT_INVALID_PARAMETER
#####Example
```cpp
 uBit.display.setBrightness(255); //max brightness 

```
##setDisplayMode
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> setDisplayMode( <div style='color:#008080; display:inline-block'>DisplayMode</div> mode)
#####Description
Sets the mode of the display. 
#####Parameters

>  <div style='color:#008080; display:inline-block'>DisplayMode</div> *mode* - The mode to swap the display into. (can be either DISPLAY_MODE_GREYSCALE, DISPLAY_MODE_BLACK_AND_WHITE, DISPLAY_MODE_BLACK_AND_WHITE_LIGHT_SENSE)
#####Example
```cpp
 uBit.display.setDisplayMode(DISPLAY_MODE_GREYSCALE); //per pixel brightness 

```
##getDisplayMode
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getDisplayMode()
#####Description
Gets the mode of the display. 
#####Returns
the current mode of the display 
##getBrightness
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getBrightness()
#####Description
Fetches the current brightness of this display. 
#####Returns
the brightness of this display, in the range 0..255.
#####Example
```cpp
 uBit.display.getBrightness(); //the current brightness 

```
##rotateTo
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> rotateTo( <div style='color:#008080; display:inline-block'>DisplayRotation</div> position)
#####Description
Rotates the display to the given position. Axis aligned values only.
#####Parameters

>  <div style='color:#008080; display:inline-block'>DisplayRotation</div> *position*
#####Example
```cpp
 uBit.display.rotateTo(MICROBIT_DISPLAY_ROTATION_180); //rotates 180 degrees from original orientation 

```
##enable
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> enable()
#####Description
Enables the display, should only be called if the display is disabled.
#####Example
```cpp
 uBit.display.enable(); //reenables the display mechanics 

```
##disable
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> disable()
#####Description
Disables the display, should only be called if the display is enabled. Display must be disabled to avoid MUXing of edge connector pins.
#####Example
```cpp
 uBit.display.disable(); //disables the display 

```
##clear
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> clear()
#####Description
Clears the current image on the display. Simplifies the process, you can also use uBit.display.image.clear
#####Example
```cpp
 uBit.display.clear(); //clears the display 

```
##setFont
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> setFont( <div style='color:#008080; display:inline-block'>MicroBitFont</div> font)
#####Description
Updates the font that will be used for display operations. DEPRECATED: Please use  MicroBitFont::setSystemFont()
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitFont</div> *font* - the new font that will be used to render characters. 
##getFont
<br/>
####<div style='color:#FF69B4; display:inline-block'>MicroBitFont</div> getFont()
#####Description
Retreives the font object used for rendering characters on the display. DEPRECATED: Please use  MicroBitFont::getSystemFont()
##screenShot
<br/>
####<div style='color:#FF69B4; display:inline-block'>MicroBitImage</div> screenShot()
#####Description
Captures the bitmap currently being rendered on the display. 
##readLightLevel
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> readLightLevel()
#####Description
Constructs an instance of a  MicroBitLightSensor

!!! note
    this will return 0 on the first call to this method, a light reading will be available after the display has activated the light sensor for the first time. 

____
[comment]: <> ({"end":"MicroBitDisplay"})
