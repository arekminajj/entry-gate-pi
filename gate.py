import RPi.GPIO as GPIO
import time

channel = 21

def openclose(pin):
        #GPIO SETUP
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(channel, GPIO.OUT)

        GPIO.output(pin, GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(pin, GPIO.LOW)
        GPIO.cleanup()
