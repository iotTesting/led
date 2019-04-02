# Import the libraries we need
import RPi.GPIO as GPIO
#pin defination control the brightness

LED = 21

#define the brightness in terms of percentage 



# Set the GPIO mode defined as per the Manufacturer 
GPIO.setmode(GPIO.BCM) 

# Set the LED GPIO pin as an output
GPIO.setup(LED,GPIO.OUT)
GPIO.setup(pwnPin,GPIO.OUT)


# Turn the GPIO pin on
GPIO.output(LED,GPIO.LOW)


time.sleep(1)

# Turn the GPIO pin off
GPIO.output(LED,FALSE)

GPIO.cleanup()