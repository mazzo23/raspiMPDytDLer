import RPi.GPIO as io
import time
import os

io.setmode(io.BCM)

# GPIO setup
io.setup(4,io.IN)
io.setup(17,io.IN)
io.setup(18,io.IN)
io.setup(27,io.IN)
io.setup(22,io.IN)
io.setup(23,io.IN)
io.setup(24,io.OUT)

x = True

try:
    while True:
        #vars are easier to read
        toggle = io.input(4)    	#play/pause; if stopped, starts playing
        prev = io.input(17)     	#previous title
        seek_f = io.input(18)   	#seek forward (+5% of whole song)
        seek_b = io.input(27)   	#seek backward (-5% of the song)
        next = io.input(22)     	#next title
        stop = io.input(23)     	#stop playback
        LED_on = io.output(24,1)	#green LED on
        LED_off = io.output(24,0)	#green LED off

	if x == True:
	    LED_on
	    time.sleep(0.5)
	    LED_off
	    time.sleep(0.5)
	if x == False:
	    LED_off


        if toggle == 1:
            os.system('mpc toggle')
            time.sleep(0.3)
            x = not x
        if prev == 1:
            os.system('mpc prev')
            time.sleep(0.3)
        if seek_f == 1:
            os.system('mpc seek +5%')
            time.sleep(0.3)
        if seek_b == 1:
            os.system('mpc seek -5%')
            time.sleep(0.3)
        if next == 1:
            os.system('mpc next')
            time.sleep(0.3)
        if stop == 1:
            os.system('mpc stop')
            time.sleep(0.3)

except KeyboardInterrupt:
    print "ontrol + C was pressed, exit with cleanup()"

finally:
    io.cleanup()
