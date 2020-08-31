import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
RELAIS_1_GPIO = 17
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode

#propably time needs to be better matched
def open_close():
    GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # on
    time.sleep(0.3)
    GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # out
    

