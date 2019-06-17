import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
GPIO.setup(21, GPIO.OUT)

def LED_ON():
    GPIO.output(21, GPIO.HIGH)

def LED_OFF():
    GPIO.output(21, GPIO.LOW)

while True:
    LED_ON()
    time.sleep(1)
    LED_OFF()
    time.sleep(1)
else:
	LED_OFF()

