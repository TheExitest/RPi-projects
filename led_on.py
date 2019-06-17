import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
GPIO.setup(21, GPIO.OUT)

def LED_ON():
    GPIO.output(21, GPIO.HIGH)

def LED_OFF():
    GPIO.output(21, GPIO.LOW)

while true:
    LED_ON()
    time.sleep(1)
    LED_OFF()
    time.sleep(1)
