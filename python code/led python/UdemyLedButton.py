import RPi.GPIO as GPIO
import time 

#Pin Defination
pwmPin =18
ledPin =23
butPin =17

#Brigness Control 
duty =75

#setup GPIO
GPOI.setmode(GPIO.BCM)

GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(pwmPin, GPIO.OUT)
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#200 beeing the frequency in Hz
pwm = GPIO.PWM(pwmPin,200)

GPIO.output(ledPin,GPIO.LOW)
pwn.start(duty)

#################### STEUP #####################

try:
    while 1:
    # if butoon not presss  do something 
        if GPIO.input(butPin):
            # Blink Red
              pwm.ChangeDutyCycle(duty)
              #green
              GPIO.output(ledPin , GPIO.LOW)

    # if butoon  presss   
        else:
              #Blink Greeen 
              pwm.ChangeDutyCycle(duty)
              GPIO.output(ledPin , GPIO.HIGH)
              time.sleep(0.5)

              #Blink Greeen red low
              pwm.ChangeDutyCycle(100-duty)
              GPIO.output(ledPin , GPIO.LOW)
              time.sleep(0.5)

except KeyboardInterrupt:
  pwm.stop()
  GPIO.cleanup()
