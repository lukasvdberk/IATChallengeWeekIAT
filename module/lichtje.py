def main():
    import RPi.GPIO as GPIO
    from time import sleep

    GPIO.setmode(GPIO.BCM)

    GPIO.setup(24, GPIO.OUT)

    GPIO.setup(23, GPIO.OUT)

    try:
        while True:
            GPIO.output(24, 1)
            GPIO.output(23, 1)

            sleep(1)
            GPIO.output(24, 0)
            GPIO.output(23, 0)

            sleep(1)

    except KeyboardInterrupt:
        GPIO.cleanup()


main()