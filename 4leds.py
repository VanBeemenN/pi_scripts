import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(12, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(18, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)

while True: # Run forever
 GPIO.output(12, GPIO.HIGH) # Turn on
 GPIO.output(16, GPIO.HIGH)
 GPIO.output(18, GPIO.HIGH)
 GPIO.output(22, GPIO.HIGH)
 sleep(1) # Sleep for 1 second
 GPIO.output(12, GPIO.LOW)
 GPIO.output(16, GPIO.LOW)
 GPIO.output(18, GPIO.LOW)
 GPIO.output(22, GPIO.LOW) # Turn off
 sleep(1) # Sleep for 1 second
 
# cleanup
GPIO.cleanup()
print("program executed")