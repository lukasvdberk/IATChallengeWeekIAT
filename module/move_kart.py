import RPi.GPIO as GPIO
import time
import RPistepper as stp
from threading import Thread

motor_pins_links = [17, 4, 3, 2]
motor_pins_rechts = [9, 10, 22, 27]

def forward():
    global motor_pins_links
    global motor_pins_rechts
    GPIO.setmode(GPIO.BCM)

    print(motor_pins_links)
    for pin in motor_pins_links:
        GPIO.setup(pin, GPIO.OUT)

    for pin in motor_pins_rechts:
        GPIO.setup(pin, GPIO.OUT)

    for i in range(50):
        for pin in motor_pins_rechts:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(0.002)
            GPIO.output(pin, GPIO.LOW)
            time.sleep(0.001)
    for i in range(50):
        for pin in motor_pins_links:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(0.002)
            GPIO.output(pin, GPIO.LOW)
            time.sleep(0.001)
# Voor een bocht
#     for i in range(50):
#         for pin in motor_pins_links:
#             GPIO.output(pin, GPIO.HIGH)
#             time.sleep(0.002)
#             GPIO.output(pin, GPIO.LOW)
#             time.sleep(0.001)

#             _thread.start_new_thread(M1.move(360), "1")
#             _thread.start_new_thread(M2.move(360), "2")
#             M1.release()
#             M2.release()

def backward():
    global motor_pins_links
    global motor_pins_rechts

    motor_pins_links1 = motor_pins_links[::-1]
    motor_pins_rechts1 = motor_pins_rechts[::-1]
    print(motor_pins_links1)
    GPIO.setmode(GPIO.BCM)

    print(motor_pins_links)
    for pin in motor_pins_links1:
        GPIO.setup(pin, GPIO.OUT)

    for pin in motor_pins_rechts1:
        GPIO.setup(pin, GPIO.OUT)

    for i in range(50):
        for pin in motor_pins_rechts1:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(0.002)
            GPIO.output(pin, GPIO.LOW)
            time.sleep(0.001)
    for i in range(50):
        for pin in motor_pins_links1:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(0.002)
            GPIO.output(pin, GPIO.LOW)
            time.sleep(0.001)

def left():
    global motor_pins_rechts
#     try:
    GPIO.setmode(GPIO.BCM)
#
    for pin in motor_pins_rechts:
        GPIO.setup(pin, GPIO.OUT)


    for i in range(500):
        for pin in motor_pins_rechts:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(0.002)
            GPIO.output(pin, GPIO.LOW)
            time.sleep(0.001)
#     except:
#         GPIO.cleanup()
#     finally:
#         GPIO.cleanup()

def right():
    global motor_pins_links
#     try:
    GPIO.setmode(GPIO.BCM)
#
    for pin in motor_pins_links:
        GPIO.setup(pin, GPIO.OUT)


    for i in range(500):
        for pin in motor_pins_links:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(0.002)
            GPIO.output(pin, GPIO.LOW)
            time.sleep(0.001)
#     except:
#         GPIO.cleanup()
#     finally:
#         GPIO.cleanup()
# try:
#     while True:
#         backward()
# except:
#     GPIO.cleanup()
# finally:
#     GPIO.cleanup()
