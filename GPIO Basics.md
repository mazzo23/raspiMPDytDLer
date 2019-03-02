### if not already up to date:

install/update GPIO (GeneralPurposeInputOutput)  

https://sourceforge.net/p/raspberry-gpio-python/

`sudo apt-get update`  
`sudo apt-get install python-rpi.gpio python3-rpi.gpio`

### get an overview of the pin layout:

`pinout`

## GPIO examples:  

### Basics:  
* [GPIO](https://www.raspberrypi.org/documentation/usage/gpio/)
* [Basic usage](https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/)  
* [Outputs](https://sourceforge.net/p/raspberry-gpio-python/wiki/Outputs/)  
* [Inputs](https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/)

### lets make GPIO control a LED:

**you need:**  
* 300 resistor
* LED
* Breadboard
* jumper cables


**start python the IDE:**

`python`

*enter every line with a return*

```
import RPi.GPIO as IO
IO.setmode(IO.BCM)
IO.setup(18,IO.OUT)
IO.output(18,IO.HIGH)
```
or  
`IO.output(18,1)`  
or  
`IO.output(18,True)`

[example LED](https://imgur.com/a/gdOHATE) url almost spells godHATE^^

### lets make GPIO read an input:

**you need:**  
* 10k resistor
* button
* jumper cables
* breadbard

**start python the IDE:**

`python`  

*enter every line with a return*

```
import RPi.GPIO as IO
IO.setmode(IO.BCM)
IO.setup(4,IO.IN)
```  

**get status of the pin:**

`IO.input(4)`

[![example readout](https://imgur.com/WChMVI2)]
https://imgur.com/a/uGHfP1S
