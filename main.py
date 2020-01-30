from rijden import rijd
import RPi.GPIO as GPIO
import time
import threading
import requests
from datetime import datetime


class Rijden:
    directions = []
    stop_servo = False

    def links_lichtje(self):
        GPIO.output(24, 1)
        time.sleep(1)
        GPIO.output(24, 0)

    def rechts_lichtje(self):
        GPIO.output(23, 1)
        time.sleep(1)
        GPIO.output(23, 0)

    def achter_lichtje(self):
        GPIO.output(24, 1)
        time.sleep(1)
        GPIO.output(24, 0)
        GPIO.output(23, 1)
        time.sleep(1)
        GPIO.output(23, 0)

    def attack(self):
        direction_attack = False
        p = GPIO.PWM(25, 50)
        p.start(5)

        while not self.stop_servo:
            p.ChangeDutyCycle(7.5)
            time.sleep(1)
            p.ChangeDutyCycle(15)
            time.sleep(1)
            p.ChangeDutyCycle(5)

    def run(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(25, GPIO.OUT)

        # Lichtjes
        GPIO.setup(24, GPIO.OUT)
        GPIO.setup(23, GPIO.OUT)
        GPIO.output(23, 0)
        GPIO.output(24, 0)

        servo_thread = threading.Thread(target=self.attack, )
        servo_thread.start()

        drive = True
        requests.post(url="http://localhost:5000/push_start")

        # Als die 2 keer op hetzelfde punt vast zit dan moet ie anders draaien
        prev_vast_zit_state_left = ""
        prev_vast_zit_state_right = ""

        achter_knop_not_pressed = datetime.now().timestamp()

        while True:
            links_btn = GPIO.input(16)
            links_btn2 = GPIO.input(20)

            rechts_btn = GPIO.input(12)
            rechts_btn2 = GPIO.input(26)

            achter_knop = GPIO.input(21)

            if drive:
                rijd.vooruit(10)
            if self.directions:
                for dir in self.directions:
                    if dir == "left":
                        GPIO.output(24, 1)
                        rijd.links_vooruit(512)
                        GPIO.output(24, 0)

                    elif dir == "right":
                        GPIO.output(23, 1)
                        rijd.rechts_vooruit(512)
                        GPIO.output(23, 0)

                self.directions = []

            if links_btn != 1 or rechts_btn != 1 or links_btn2 != 1 or rechts_btn2 != 1:
                requests.post(url="http://localhost:5000/push_hit")

                for n in range(3):
                    time.sleep(0.2)
                    GPIO.output(24, 1)
                    GPIO.output(23, 1)
                    time.sleep(0.2)
                    GPIO.output(24, 0)
                    GPIO.output(23, 0)


                rijd.achteruit(1000)
                if links_btn != 1 or links_btn2 != 1:

                    if prev_vast_zit_state_left == "left":
                        GPIO.output(24, 1)
                        rijd.links_vooruit(600)
                        prev_vast_zit_state_left = ""
                    else:
                        GPIO.output(23, 1)
                        rijd.rechts_vooruit(600)
                        prev_vast_zit_state_left = "left"

                if rechts_btn != 1 or rechts_btn2 != 1:

                    if prev_vast_zit_state_right == "right":
                        GPIO.output(23, 1)
                        rijd.rechts_vooruit(600)
                        prev_vast_zit_state_right = ""
                    else:
                        GPIO.output(24, 1)
                        prev_vast_zit_state_right = "right"
                        rijd.links_vooruit(600)

                GPIO.output(24, 0)
                GPIO.output(23, 0)

            # TODO change to ==
            curr_timestamp = datetime.now().timestamp()

            if achter_knop == 1 and (curr_timestamp - achter_knop_not_pressed) >= 2:
                requests.post(url="http://localhost:5000/push_death")
                self.stop_servo = True
                GPIO.output(24, 1)
                GPIO.output(23, 1)

                rijd.links_vooruit(20)

                time_not_hit = datetime.now().timestamp()
                while True:
                    rijd.vooruit(10)

                    links_btn = GPIO.input(16)
                    links_btn2 = GPIO.input(20)

                    rechts_btn = GPIO.input(12)
                    rechts_btn2 = GPIO.input(26)

                    curr_timestamp = datetime.now().timestamp()

                    if links_btn == 1 and rechts_btn == 1 and links_btn2 == 1 and rechts_btn2 == 1:
                        time_not_hit = datetime.now().timestamp()
                    if curr_timestamp - time_not_hit >= 3:
                        requests.post(url="http://localhost:5000/push_end")
                        exit()
            if achter_knop != 1:
                achter_knop_not_pressed = datetime.now().timestamp()

if __name__ == "__main__":
    try:
        Rijden().run()
    except KeyboardInterrupt:
        GPIO.cleanup()
    except:
        GPIO.cleanup()
    finally:
        GPIO.cleanup()