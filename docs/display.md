#uBit.display

##Overview

##Message Bus ID

##Message Bus Events

##API
[comment]: <> ({"className":"MicroBitDisplay"})
##Constructor
<br/>
####MicroBitDisplay( <div style='color:#008080; display:inline-block'>uint16_t</div> id,  <div style='color:#008080; display:inline-block'>uint8_t</div> x,  <div style='color:#008080; display:inline-block'>uint8_t</div> y)
#####Description
Constructor. Create a representation of a display of a given size. The display is initially blank.
#####Parameters

>  <div style='color:#008080; display:inline-block'>uint16_t</div> *id*

>  <div style='color:#008080; display:inline-block'>uint8_t</div> *x* - the width of the display in pixels. 

>  <div style='color:#008080; display:inline-block'>uint8_t</div> *y* - the height of the display in pixels.
#####Example
```c++
MicroBitDisplaydisplay(MICROBIT_ID_DISPLAY,5,5),

```
##stopAnimation
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> stopAnimation()
#####Description
Stops any currently running animation, and any that are waiting to be displayed.
##printAsync
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> printAsync( <div style='color:#008080; display:inline-block'>char</div> c)
#####Description
Prints the given character to the display, if it is not in use.
#####Parameters

>  <div style='color:#008080; display:inline-block'>char</div> *c* - The character to display. 
#####Returns
MICROBIT_OK, MICROBIT_BUSY is the screen is in use, or MICROBIT_INVALID_PARAMETER.
#####Example
```c++
uBit.display.printAsync('p');
uBit.display.printAsync('p',100);

```
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> printAsync( <div style='color:#008080; display:inline-block'>char</div> c,  <div style='color:#008080; display:inline-block'>int</div> delay)
#####Description
Prints the given character to the display, if it is not in use.
#####Parameters

>  <div style='color:#008080; display:inline-block'>char</div> *c* - The character to display. 

>  <div style='color:#008080; display:inline-block'>int</div> *delay* - Optional parameter - the time for which to show the character. Zero displays the character forever. 
#####Returns
MICROBIT_OK, MICROBIT_BUSY is the screen is in use, or MICROBIT_INVALID_PARAMETER.
#####Example
```c++
uBit.display.printAsync('p');
uBit.display.printAsync('p',100);

```
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> printAsync( <div style='color:#008080; display:inline-block'>ManagedString</div> s)
#####Description
Prints the given string to the display, one character at a time. Uses the given delay between characters. Returns immediately, and executes the animation asynchronously.
#####Parameters

>  <div style='color:#008080; display:inline-block'>ManagedString</div> *s* - The string to display. 
#####Returns
MICROBIT_OK, or MICROBIT_INVALID_PARAMETER.
#####Example
```c++
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
```c++
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
```c++
MicrobitImagei("1,1,1,1,1\n1,1,1,1,1\n");
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
```c++
MicrobitImagei("1,1,1,1,1\n1,1,1,1,1\n");
uBit.display.print(i,400);

```
##print
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> print( <div style='color:#008080; display:inline-block'>char</div> c)
#####Description
Prints the given character to the display.
#####Parameters

>  <div style='color:#008080; display:inline-block'>char</div> *c* - The character to display. 
#####Returns
MICROBIT_OK, MICROBIT_CANCELLED or MICROBIT_INVALID_PARAMETER.
#####Example
```c++
uBit.display.print('p');

```
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> print( <div style='color:#008080; display:inline-block'>char</div> c,  <div style='color:#008080; display:inline-block'>int</div> delay)
#####Description
Prints the given character to the display.
#####Parameters

>  <div style='color:#008080; display:inline-block'>char</div> *c* - The character to display. 

>  <div style='color:#008080; display:inline-block'>int</div> *delay* - The time to delay between characters, in milliseconds. Must be > 0. 
#####Returns
MICROBIT_OK, MICROBIT_CANCELLED or MICROBIT_INVALID_PARAMETER.
#####Example
```c++
uBit.display.print('p');

```
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> print( <div style='color:#008080; display:inline-block'>ManagedString</div> s)
#####Description
Prints the given string to the display, one character at a time. Uses the given delay between characters. Blocks the calling thread until all the text has been displayed.
#####Parameters

>  <div style='color:#008080; display:inline-block'>ManagedString</div> *s* - The string to display. 
#####Returns
MICROBIT_OK, MICROBIT_CANCELLED or MICROBIT_INVALID_PARAMETER.
#####Example
```c++
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
```c++
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
```c++
MicrobitImagei("1,1,1,1,1\n1,1,1,1,1\n");
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
```c++
MicrobitImagei("1,1,1,1,1\n1,1,1,1,1\n");
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
```c++
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
```c++
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
```c++
MicrobitImagei("1,1,1,1,1\n1,1,1,1,1\n");
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
```c++
MicrobitImagei("1,1,1,1,1\n1,1,1,1,1\n");
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
```c++
MicrobitImagei("1,1,1,1,1\n1,1,1,1,1\n");
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
```c++
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
```c++
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
```c++
MicrobitImagei("1,1,1,1,1\n1,1,1,1,1\n");
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
```c++
MicrobitImagei("1,1,1,1,1\n1,1,1,1,1\n");
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
```c++
MicrobitImagei("1,1,1,1,1\n1,1,1,1,1\n");
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
```c++
constintheart_w=10;
constintheart_h=5;
constuint8_theart[]={0,1,0,1,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,0,1,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,};

MicroBitImagei(heart_w,heart_h,heart);
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
```c++
constintheart_w=10;
constintheart_h=5;
constuint8_theart[]={0,1,0,1,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,0,1,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,};

MicroBitImagei(heart_w,heart_h,heart);
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
```c++
constintheart_w=10;
constintheart_h=5;
constuint8_theart[]={0,1,0,1,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,0,1,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,};

MicroBitImagei(heart_w,heart_h,heart);
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
```c++
constintheart_w=10;
constintheart_h=5;
constuint8_theart[]={0,1,0,1,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,0,1,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,};

MicroBitImagei(heart_w,heart_h,heart);
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
```c++
uBit.display.setBrightness(255);//maxbrightness

```
##setDisplayMode
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> setDisplayMode( <div style='color:#008080; display:inline-block'>DisplayMode</div> mode)
#####Description
Sets the mode of the display. 
#####Parameters

>  <div style='color:#008080; display:inline-block'>DisplayMode</div> *mode* - The mode to swap the display into. (can be either DISPLAY_MODE_GREYSCALE, DISPLAY_MODE_BLACK_AND_WHITE, DISPLAY_MODE_BLACK_AND_WHITE_LIGHT_SENSE)
#####Example
```c++
uBit.display.setDisplayMode(DISPLAY_MODE_GREYSCALE);//perpixelbrightness

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
```c++
uBit.display.getBrightness();//thecurrentbrightness

```
##rotateTo
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> rotateTo( <div style='color:#008080; display:inline-block'>DisplayRotation</div> position)
#####Description
Rotates the display to the given position. Axis aligned values only.
#####Parameters

>  <div style='color:#008080; display:inline-block'>DisplayRotation</div> *position*
#####Example
```c++
uBit.display.rotateTo(MICROBIT_DISPLAY_ROTATION_180);//rotates180degreesfromoriginalorientation

```
##enable
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> enable()
#####Description
Enables the display, should only be called if the display is disabled.
#####Example
```c++
uBit.display.enable();//reenablesthedisplaymechanics

```
##disable
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> disable()
#####Description
Disables the display, should only be called if the display is enabled. Display must be disabled to avoid MUXing of edge connector pins.
#####Example
```c++
uBit.display.disable();//disablesthedisplay

```
##clear
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> clear()
#####Description
Clears the current image on the display. Simplifies the process, you can also use uBit.display.image.clear
#####Example
```c++
uBit.display.clear();//clearsthedisplay

```
##error
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> error( <div style='color:#008080; display:inline-block'>int</div> statusCode)
#####Description
Displays "=(" and an accompanying status code infinitely. 
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *statusCode* - the appropriate status code - 0 means no code will be displayed. Status codes must be in the range 0-255.
#####Example
```c++
uBit.display.error(20);

```
##setErrorTimeout
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> setErrorTimeout( <div style='color:#008080; display:inline-block'>int</div> iterations)
#####Description
Defines the length of time that the device will remain in a error state before resetting. 
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *iterations* - The number of times the error code will be displayed before resetting. Set to zero to remain in error state forever.
#####Example
```c++
uBit.display.setErrorTimeout(4);

```
##setFont
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> setFont( <div style='color:#008080; display:inline-block'>MicroBitFont</div> font)
#####Description
Updates the font property of this object with the new font. 
#####Parameters

>  <div style='color:#008080; display:inline-block'>MicroBitFont</div> *font* - the new font that will be used to render characters.. 
##getFont
<br/>
####<div style='color:#FF69B4; display:inline-block'>MicroBitFont</div> getFont()
#####Description
Retreives the font object used for rendering characters on the display. 
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
    this will return 0 on the first call to this method, a light reading will be available after the display has activated the light sensor for the first time. ##~MicroBitDisplay
<br/>
####~MicroBitDisplay()
#####Description
Destructor for  MicroBitDisplay
____
[comment]: <> ({"end":"MicroBitDisplay"})
