import RPi.io as io
import time

io.setmode(io.BCM)
io.setup(24,io.OUT)

try:
	while True:
		io.output(24,1)
		time.sleep(1)
		io.output(24,0)
		time.sleep(1)

except KeyboardInterrupt:
	print "ontrol + C was pressed, exit with io.cleanup()"

finally:
	io.cleanup()
