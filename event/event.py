import RPi.GPIO as GPIO
import time


class pi:
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    buttonPin = 5
    GPIO.setup(buttonPin,GPIO.IN,pull_up_down = GPIO.PUD_UP)
    GPIO.setup(3,GPIO.OUT)
    count=0
    def __init__(self):
        GPIO.add_event_detect(self.buttonPin,GPIO.FALLING,callback=self.pressed,bouncetime=200)
    def pressed(self,e):
        self.count+=1
        if (self.count%4==0):
            GPIO.output(3,GPIO.HIGH)
        else:
            GPIO.output(3,GPIO.LOW)

if __name__ == '__main__':
    p = pi()
    input()