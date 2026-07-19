from gpiozero import RGBLED
from time import sleep

# Initialize pins based on Broadcom (BCM) numbering
led = RGBLED(red=17, green=27, blue=22, active_high=False)

try:
    while True:
        led.color = (1, 0, 0) # Red
        sleep(1)
        led.color = (0, 1, 0) # Green
        sleep(1)
        led.color = (0, 0, 1) # Blue
        sleep(1)
        led.color = (1, 1, 1) # White
        sleep(1)
        led.color = (1, 1, 0) # Yellow
        sleep(1)
        led.color = (0, 0, 0) # Off
        sleep(1)

except KeyboardInterrupt:
    # Turn off LED and exit gracefully
    led.color = (0, 0, 0)
