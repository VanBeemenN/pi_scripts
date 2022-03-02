import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

def blink(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 1)
    sleep(0.5)
    GPIO.output(pin, 0)
    sleep(0.5)

for i in range(0,10):
    blink(23)
    blink(16)
    blink(18)
    blink(24)
    
GPIO.cleanup()