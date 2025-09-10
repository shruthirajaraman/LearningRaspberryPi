from gpiozero import LED
from time import sleep

# LED pin
led = LED(17)

# Make LED blink
while True:
	led.on() # on
	sleep(0.2)
	led.off() # off
	sleep(0.2)