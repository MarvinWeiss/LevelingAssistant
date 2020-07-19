# Bed Leveling Assistant for Anycubic i3 mega 3d printers with the help of dial indicators

## Introduction
This software can be used as helper tool to level Anycubic i3 mega printers. 

I found inspiration to implement it because of a Video by SunShine on youtube: https://youtu.be/RFkn6gMkz78

it consists of a print in place dial indicator as well as a holder for it do slip onto the printhead.
The STLs can be found here on thingiverse: https://www.thingiverse.com/thing:4524389
To always measure at the same spots I developed this piece of software. 
I'm currently working on a adaption for the holder to fit on Anycubic i3 Mega printers. I will post it here as whell when I'm done.
I use the holder with a generic dial indicator from amazon, nothing fancy and it works like a charm. 



## Installation
To use the software you have to install two python lybraries.
```
pip install pyserial
pip install appjar
```

If you run into module not found errors try 

`python -m pip install --upgrade appJar`

## Usage
To start it just type:
`python  levelingAssistant.py`

After startup select your Printer in the Dropdown menu, it's a list with all the serial ports known to your computer. 
When selected, click Connect. It automatically homes the printer.

Now you have to level the home point with a sheet of paper as usual, just as a reference for the other corners. 
When done select Home Indicator.
Set your indicator to zero. 

Then do the diagonal side, top right, spin the leveling wheel so it matches up with the zero point of the initial bottom left corner. 

Do this with the other corners, too and you should have a perfect leveled bed!


I hope you find this software usefull!

### Have fun Printing! 


