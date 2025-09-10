import time
from gpiozero import MotionSensor, LED

# Set the GPIO pin where the PIR's data pin is connected
pir_pin = 17  # Using GPIO 17 (Pin 11)
pir = MotionSensor(pir_pin)
led = LED(18)

print("Starting motion detection...")

while True:
    # Wait for motion to be detected
    pir.wait_for_motion()
    print("Motion detected! Turn on LED.")
    led.on()
    time.sleep(10) # 10 second delay

    # Wait for motion to stop
    pir.wait_for_no_motion()
    print("Motion stopped. Turn off LED.")
    led.off()