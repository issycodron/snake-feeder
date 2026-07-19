'''
display.py is responsible for displaying the status of Meeko's feeding schedule.
This includes a trigger feature to show days since/days until next feeding, 
and an urgency score that can be used to control the LED display on the physical device.
'''
from gpiozero import RGBLED, Button
from gpiozero.pins.lgpio import LGPIOFactory
from gpiozero import Device

Device.pin_factory = LGPIOFactory()

led = RGBLED(red=17, green=27, blue=22, active_high=False)

button = Button(4)

def display_status(status):
    """
    This function will be responsible for displaying the status of Meeko's feeding schedule.
    It will show days since last feeding, days until next feeding.
    For now, this will just print to the console, but eventually it will be triggered by a button on the console.
    """
    # make border display for console output

    print("="*40)
    print(status)
    print("="*40)


def display_urgency(urgency_score, days_since):
    """
    This function will take the urgency score calculated in feeder.py and use it to control the LED display on the physical device.
    For example, it could change the color or brightness of the LED based on the urgency score.
    For now, this will just print the urgency score to the console, but eventually it will control the LED display on the physical device.
    """
    print(f"Urgency Score: {urgency_score}")
    if urgency_score >= 1.4:
        led.color = (1, 0, 0)
        print("LED Color: Flashing colours (Very Urgent)")
        print(f"Urgent Warning: Meeko is very hungry! Days since last feeding: {days_since}")
    elif urgency_score >= 1.2:
        led.color = (1, 0, 0)
        print("LED Color: Flashing red (Urgent)")
        print(f"Warning: Meeko is hungry! Days since last feeding: {days_since}")
    elif urgency_score >= 1.0:
        led.color = (1, 0, 0)
        print("LED Color: Red (Feed the beast!)")
    elif urgency_score >= 0.8:
        led.color = (1, 0.4, 0)
        print("LED Color: Orange (Get Ready)")
    elif urgency_score >= 0.6:
        led.color = (1, 1, 0)
        print("LED Color: Yellow (Has he pooped?)")
    else:
        led.color = (0, 1, 0)
        print("LED Color: Green (Not Urgent)")



def prompt_feeding_log():
    """
    Prompts the user to log a feeding by pressing the physical button.
    Times out after 10 seconds if no press detected.
    """
    print("Press the button to log a feed, or wait to skip...")
    button.wait_for_press(timeout=10)
    if button.is_pressed:
        print("Feeding logged.")
        return True
    else:
        print("Logging skipped.")
        return False
