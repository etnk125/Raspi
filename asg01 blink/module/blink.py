import RPi.GPIO as GPIO
from time import sleep 

def blink(pin,delay=1,round=1):
    for i in range(round):
        print('blinked',i)
        GPIO.output(pin,GPIO.HIGH)
        sleep(delay)
        GPIO.output(pin,GPIO.LOW)
        sleep(delay)

    
