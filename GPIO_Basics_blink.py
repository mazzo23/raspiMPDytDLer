import RPi.io as io
import time

io.setmode(io.BCM)
io.setup(24,io.OUT)

while True:
	io.output(24,1)
	time.sleep(1)
	io.output(24,0)
	time.sleep(1)
