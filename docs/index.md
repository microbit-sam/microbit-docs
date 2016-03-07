# Welcome to MkDocs

For full documentation visit [mkdocs.org](http://mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs help` - Print this help message.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

#API
[comment]: <> ({"className":"MicroBitImage"})
##leakData
<br/>
####<div style='color:#FF69B4; display:inline-block'>ImageData</div> leakData()
#####Description
Get current ptr, do not decr() it, and set the current instance to empty image. This is to be used by specialized runtimes which pass  ImageData
##getBitmap
<br/>
####<div style='color:#FF69B4; display:inline-block'>uint8_t *</div> getBitmap()
#####Description
Return a 2D array representing the bitmap image. 
##Constructor
<br/>
####MicroBitImage( <div style='color:#008080; display:inline-block'>ImageData  *</div> ptr)
#####Description
Constructor. Create an image from a specially prepared constant array, with no copying. Will call ptr->incr().
#####Parameters

>  <div style='color:#008080; display:inline-block'>ImageData  *</div> *ptr* - The literal - first two bytes should be 0xff, then width, 0, height, 0, and the bitmap. Width and height are 16 bit. The literal has to be 4-byte aligned.
#####Example
```c++
staticconstuint8_theart[]__attribute__((aligned(4)))={0xff,0xff,10,0,5,0,0,1,0,1,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,0,1,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,};//acuteheart
MicroBitImagei((ImageData*)(void*)heart);

```
<br/>
####MicroBitImage()
#####Description
Default Constructor. Creates a new reference to the empty  MicroBitImage
#####Example
```c++
MicroBitImagei();//anemptyimage

```
<br/>
####MicroBitImage( <div style='color:#008080; display:inline-block'>const  MicroBitImage  &</div> image)
#####Description
Copy Constructor. Add ourselves as a reference to an existing  MicroBitImage
#####Parameters

>  <div style='color:#008080; display:inline-block'>const  MicroBitImage  &</div> *image* - The  MicroBitImage  to reference.
#####Example
```c++
MicroBitImagei("0,1,0,1,0\n");
MicroBitImagei2(i);//pointstoi

```
<br/>
####MicroBitImage( <div style='color:#008080; display:inline-block'>const char *</div> s)
#####Description
Constructor. Create a blank bitmap representation of a given size.
#####Parameters

>  <div style='color:#008080; display:inline-block'>const char *</div> *s* - A text based representation of the image given whitespace delimited numeric values.
#####Example
```c++
MicroBitImagei("0,1,0,1,0\n1,0,1,0,1\n0,1,0,1,0\n1,0,1,0,1\n0,1,0,1,0\n");//5x5image

```
<br/>
####MicroBitImage( <div style='color:#008080; display:inline-block'>const int16_t</div> x,  <div style='color:#008080; display:inline-block'>const int16_t</div> y)
#####Description
Constructor. Create a blank bitmap representation of a given size.
#####Parameters

>  <div style='color:#008080; display:inline-block'>const int16_t</div> *x* - the width of the image. 

>  <div style='color:#008080; display:inline-block'>const int16_t</div> *y* - the height of the image.
#####Example
```c++
MicroBitImagei(5,5);//ablank5x5image

```
<br/>
####MicroBitImage( <div style='color:#008080; display:inline-block'>const int16_t</div> x,  <div style='color:#008080; display:inline-block'>const int16_t</div> y,  <div style='color:#008080; display:inline-block'>const uint8_t *</div> bitmap)
#####Description
Constructor. Create a bitmap representation of a given size, based on a given buffer.
#####Parameters

>  <div style='color:#008080; display:inline-block'>const int16_t</div> *x* - the width of the image. 

>  <div style='color:#008080; display:inline-block'>const int16_t</div> *y* - the height of the image. 

>  <div style='color:#008080; display:inline-block'>const uint8_t *</div> *bitmap* - a 2D array representing the image.
#####Example
```c++
constuint8_theart[]={0,1,0,1,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,0,1,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,};//acuteheart
MicroBitImagei(10,5,heart);

```
##~MicroBitImage
<br/>
####~MicroBitImage()
#####Description
Destructor. Removes buffer resources held by the instance. 
##operator=
<br/>
####<div style='color:#FF69B4; display:inline-block'>MicroBitImage</div> operator=( <div style='color:#008080; display:inline-block'>const  MicroBitImage  &</div> i)
#####Description
Copy assign operation.
#####Parameters

>  <div style='color:#008080; display:inline-block'>const  MicroBitImage  &</div> *i*
#####Example
```c++
constuint8_theart[]={0,1,0,1,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,0,1,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,};//acuteheart
MicroBitImagei(10,5,heart);
MicroBitImagei1();
i1=1;//i1nowreferencesi

```
##operator==
<br/>
####<div style='color:#FF69B4; display:inline-block'>bool</div> operator==( <div style='color:#008080; display:inline-block'>const  MicroBitImage  &</div> i)
#####Description
Equality operation.
#####Parameters

>  <div style='color:#008080; display:inline-block'>const  MicroBitImage  &</div> *i* - The  MicroBitImage  to test ourselves against. 
#####Returns
true if this  MicroBitImage  is identical to the one supplied, false otherwise.
#####Example
```c++
MicroBitImagei();
MicroBitImagei1();

if(i==i1)//willbetrue
print("true");

```
##clear
<br/>
####<div style='color:#FF69B4; display:inline-block'>void</div> clear()
#####Description
Clears all pixels in this image
#####Example
```c++
MicroBitImagei("0,1,0,1,0\n1,0,1,0,1\n0,1,0,1,0\n1,0,1,0,1\n0,1,0,1,0\n");//5x5image
i.clear();

```
##setPixelValue
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> setPixelValue( <div style='color:#008080; display:inline-block'>int16_t</div> x,  <div style='color:#008080; display:inline-block'>int16_t</div> y,  <div style='color:#008080; display:inline-block'>uint8_t</div> value)
#####Description
Sets the pixel at the given co-ordinates to a given value. 
#####Parameters

>  <div style='color:#008080; display:inline-block'>int16_t</div> *x* - The co-ordinate of the pixel to change w.r.t. top left origin. 

>  <div style='color:#008080; display:inline-block'>int16_t</div> *y* - The co-ordinate of the pixel to change w.r.t. top left origin. 

>  <div style='color:#008080; display:inline-block'>uint8_t</div> *value* - The new value of the pixel (the brightness level 0-255) 
#####Returns
MICROBIT_OK, or MICROBIT_INVALID_PARAMETER.
#####Example
```c++
MicroBitImagei("0,1,0,1,0\n1,0,1,0,1\n0,1,0,1,0\n1,0,1,0,1\n0,1,0,1,0\n");//5x5image
i.setPixelValue(0,0,255);

```
##getPixelValue
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getPixelValue( <div style='color:#008080; display:inline-block'>int16_t</div> x,  <div style='color:#008080; display:inline-block'>int16_t</div> y)
#####Description
Determines the value of a given pixel.
#####Parameters

>  <div style='color:#008080; display:inline-block'>int16_t</div> *x* - The x co-ordinate of the pixel to read. Must be within the dimensions of the image. 

>  <div style='color:#008080; display:inline-block'>int16_t</div> *y* - The y co-ordinate of the pixel to read. Must be within the dimensions of the image. 
#####Returns
The value assigned to the given pixel location (the brightness level 0-255), or MICROBIT_INVALID_PARAMETER.
#####Example
```c++
MicroBitImagei("0,1,0,1,0\n1,0,1,0,1\n0,1,0,1,0\n1,0,1,0,1\n0,1,0,1,0\n");//5x5image
i.getPixelValue(0,0);//shouldbe0;

```
##printImage
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> printImage( <div style='color:#008080; display:inline-block'>int16_t</div> x,  <div style='color:#008080; display:inline-block'>int16_t</div> y,  <div style='color:#008080; display:inline-block'>const uint8_t *</div> bitmap)
#####Description
Replaces the content of this image with that of a given 2D array representing the image. Origin is in the top left corner of the image.
#####Parameters

>  <div style='color:#008080; display:inline-block'>int16_t</div> *x* - the width of the image. Must be within the dimensions of the image. 

>  <div style='color:#008080; display:inline-block'>int16_t</div> *y* - the width of the image. Must be within the dimensions of the image. 

>  <div style='color:#008080; display:inline-block'>const uint8_t *</div> *bitmap* - a 2D array representing the image. 
#####Returns
MICROBIT_OK on success, or MICROBIT_INVALID_PARAMETER.
#####Example
```c++
constuint8_theart[]={0,1,0,1,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,0,1,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,};//acuteheart
MicroBitImagei();
i.printImage(0,0,heart);

```
##paste
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> paste( <div style='color:#008080; display:inline-block'>const  MicroBitImage  &</div> image,  <div style='color:#008080; display:inline-block'>int16_t</div> x,  <div style='color:#008080; display:inline-block'>int16_t</div> y,  <div style='color:#008080; display:inline-block'>uint8_t</div> alpha)
#####Description
Pastes a given bitmap at the given co-ordinates. Any pixels in the relvant area of this image are replaced.
#####Parameters

>  <div style='color:#008080; display:inline-block'>const  MicroBitImage  &</div> *image* - The  MicroBitImage  to paste. 

>  <div style='color:#008080; display:inline-block'>int16_t</div> *x* - The leftmost X co-ordinate in this image where the given image should be pasted. 

>  <div style='color:#008080; display:inline-block'>int16_t</div> *y* - The uppermost Y co-ordinate in this image where the given image should be pasted. 

>  <div style='color:#008080; display:inline-block'>uint8_t</div> *alpha* - set to 1 if transparency clear pixels in given image should be treated as transparent. Set to 0 otherwise. 
#####Returns
The number of pixels written, or MICROBIT_INVALID_PARAMETER.
#####Example
```c++
constuint8_theart[]={0,1,0,1,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,0,1,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,};//acuteheart
MicroBitImagei(10,5,heart);//ifyoushowthisimage-youwillseeabigheart
i.paste(-5,0,i);//displaysasmallheart:)

```
##print
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> print( <div style='color:#008080; display:inline-block'>char</div> c,  <div style='color:#008080; display:inline-block'>int16_t</div> x,  <div style='color:#008080; display:inline-block'>int16_t</div> y)
#####Description
Prints a character to the display at the given location
#####Parameters

>  <div style='color:#008080; display:inline-block'>char</div> *c* - The character to display. 

>  <div style='color:#008080; display:inline-block'>int16_t</div> *x* - The x co-ordinate of on the image to place the top left of the character 

>  <div style='color:#008080; display:inline-block'>int16_t</div> *y* - The y co-ordinate of on the image to place the top left of the character 
#####Returns
MICROBIT_OK on success, or MICROBIT_INVALID_PARAMETER.
#####Example
```c++
MicroBitImagei(5,5);
i.print('a',0,0);

```
##shiftLeft
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> shiftLeft( <div style='color:#008080; display:inline-block'>int16_t</div> n)
#####Description
Shifts the pixels in this Image a given number of pixels to the Left.
#####Parameters

>  <div style='color:#008080; display:inline-block'>int16_t</div> *n* - The number of pixels to shift. 
#####Returns
MICROBIT_OK on success, or MICROBIT_INVALID_PARAMETER.
#####Example
```c++
constuint8_theart[]={0,1,0,1,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,0,1,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,};//acuteheart
MicroBitImagei(10,5,heart);//ifyoushowthisimage-youwillseeabigheart
i.shiftLeft(5);//displaysasmallheart:)

```
##shiftRight
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> shiftRight( <div style='color:#008080; display:inline-block'>int16_t</div> n)
#####Description
Shifts the pixels in this Image a given number of pixels to the Right.
#####Parameters

>  <div style='color:#008080; display:inline-block'>int16_t</div> *n* - The number of pixels to shift. 
#####Returns
MICROBIT_OK on success, or MICROBIT_INVALID_PARAMETER.
#####Example
```c++
constuint8_theart[]={0,1,0,1,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,0,1,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,};//acuteheart
MicroBitImagei(10,5,heart);
i.shiftLeft(5);//displaysasmallheart:)
i.shiftRight(5);//displaysabigheart:)

```
##shiftUp
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> shiftUp( <div style='color:#008080; display:inline-block'>int16_t</div> n)
#####Description
Shifts the pixels in this Image a given number of pixels to Upward.
#####Parameters

>  <div style='color:#008080; display:inline-block'>int16_t</div> *n* - The number of pixels to shift. 
#####Returns
MICROBIT_OK on success, or MICROBIT_INVALID_PARAMETER.
#####Example
```c++
constuint8_theart[]={0,1,0,1,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,0,1,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,};//acuteheart
MicroBitImagei(10,5,heart);
i.shiftUp(1);

```
##shiftDown
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> shiftDown( <div style='color:#008080; display:inline-block'>int16_t</div> n)
#####Description
Shifts the pixels in this Image a given number of pixels to Downward.
#####Parameters

>  <div style='color:#008080; display:inline-block'>int16_t</div> *n* - The number of pixels to shift. 
#####Returns
MICROBIT_OK on success, or MICROBIT_INVALID_PARAMETER.
#####Example
```c++
constuint8_theart[]={0,1,0,1,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,0,1,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,};//acuteheart
MicroBitImagei(10,5,heart);
i.shiftDown(1);

```
##getWidth
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getWidth()
#####Description
Gets the width of this image.
#####Returns
The width of this image.
#####Example
```c++
constuint8_theart[]={0,1,0,1,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,0,1,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,};//acuteheart
MicroBitImagei(10,5,heart);
i.getWidth();//equals10...

```
##getHeight
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getHeight()
#####Description
Gets the height of this image.
#####Returns
The height of this image.
#####Example
```c++
constuint8_theart[]={0,1,0,1,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,0,1,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,};//acuteheart
MicroBitImagei(10,5,heart);
i.getHeight();//equals5...

```
##getSize
<br/>
####<div style='color:#FF69B4; display:inline-block'>int</div> getSize()
#####Description
Gets number of bytes in the bitmap, ie., width * height.
#####Returns
The size of the bitmap.
#####Example
```c++
constuint8_theart[]={0,1,0,1,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,0,1,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,};//acuteheart
MicroBitImagei(10,5,heart);
i.getSize();//equals50...

```
##toString
<br/>
####<div style='color:#FF69B4; display:inline-block'>ManagedString</div> toString()
#####Description
Converts the bitmap to a csv string.
#####Example
```c++
constuint8_theart[]={0,1,0,1,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,0,1,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,};//acuteheart
MicroBitImagei(10,5,heart);
uBit.serial.printString(i.toString());//"0,1,0,1,0,0,0,0,0,0\n..."

```
##crop
<br/>
####<div style='color:#FF69B4; display:inline-block'>MicroBitImage</div> crop( <div style='color:#008080; display:inline-block'>int</div> startx,  <div style='color:#008080; display:inline-block'>int</div> starty,  <div style='color:#008080; display:inline-block'>int</div> finx,  <div style='color:#008080; display:inline-block'>int</div> finy)
#####Description
Crops the image to the given dimensions
#####Parameters

>  <div style='color:#008080; display:inline-block'>int</div> *startx* - the location to start the crop in the x-axis 

>  <div style='color:#008080; display:inline-block'>int</div> *starty* - the location to start the crop in the y-axis 

>  <div style='color:#008080; display:inline-block'>int</div> *finx*

>  <div style='color:#008080; display:inline-block'>int</div> *finy*
#####Returns
an instance of  MicroBitImage  with your cropped region
#####Example
```c++
constuint8_theart[]={0,1,0,1,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1,0,1,1,1,0,0,1,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,};//acuteheart
MicroBitImagei(10,5,heart);
uBit.serial.printImage(i.crop(0,0,2,2));//"0,1\n1,1\n"

```
##isReadOnly
<br/>
####<div style='color:#FF69B4; display:inline-block'>bool</div> isReadOnly()
#####Description
Check if image is read-only (i.e., residing in flash). 
##clone
<br/>
####<div style='color:#FF69B4; display:inline-block'>MicroBitImage</div> clone()
#####Description
Create a copy of the image bitmap. Used particularly, when  isReadOnly()
#####Returns
an instance of  MicroBitImage  which can be modified independently of the current instance 
____
[comment]: <> ({"end":"MicroBitImage"})
