import RPi.GPIO as GPIO
import time

channel = 21

#GPIO SETUP
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

def openclose(pin):
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(0.3)
        GPIO.output(pin, GPIO.LOW)

openclose(channel)
GPIO.cleanup()
