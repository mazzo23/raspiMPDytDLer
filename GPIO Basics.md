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
* 300 ohm resistor
* LED
* Breadboard
* jumper cables

pic

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

![example LED](https://i.imgur.com/0ZhBEJY.png "example output")

### lets make GPIO read an input:

**you need:**  
* 10k ohm resistor
* button
* jumper cables
* breadbard

pic

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

![example readout](https://i.imgur.com/WChMVI2.png "example readout")  
button connected to pin 4. button not pressed returns 0 - button pressed returns 1

https://imgur.com/a/gdOHATE url almost spells godHATE^^  
https://imgur.com/a/uGHfP1S
