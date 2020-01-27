# imports are program code that are needed to run your program
import RPi.GPIO as GPIO  # import library for working with Raspberry's GPIO
import time  # needed to use sleep()

buttonPin = 4  # this will be an input pin to which the button is attached

prev_state = 1  # set start state to 1 (button released)

GPIO.setmode(GPIO.BCM)

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

event = 1

while True:
    curr_state = GPIO.input(buttonPin)

    if curr_state != prev_state:
        if curr_state == 1:
            event = "released"
            print(event)
        else:
            event = "pressed"
            print(event)
        prev_state = curr_state

    time.sleep(0.02)

GPIO.cleanup()
