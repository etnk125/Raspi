import RPi.GPIO as GPIO
import time

def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

def outp(pin):
    GPIO.setup(pin,GPIO.OUT)

def inp(pin):
    GPIO.setup(pin,GPIO.IN)
    
def use_switch(pin,handle = None ):
    GPIO.setup(pin,GPIO.IN,pull_up_down = GPIO.PUD_UP)
    GPIO.add_event_detect(pin,GPIO.FALLING,callback = handle,bouncetime=200)

def test():
    print('test')