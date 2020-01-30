import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

def vooruit(stappen):

    pins = [9, 10, 17, 4, 22, 27, 3, 2]


    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)
    n = 0
    while n != stappen:
        for pin in pins:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(0.0025)
            GPIO.output(pin, GPIO.LOW)
            time.sleep(0.0001)
        n += 1

def achteruit(stappen):

    pins = [2, 3, 27, 22, 4, 17, 10, 9]
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)
    n = 0
    while n != stappen:
        for pin in pins:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(0.0025)
            GPIO.output(pin, GPIO.LOW)
            time.sleep(0.0001)
        n += 1


if __name__ == "__main__":
    try:
        while True:

            vooruit(100)
            time.sleep(1)
            achteruit(100)

    except:
        GPIO.cleanup()
    finally:
        GPIO.cleanup()
