import RPi.GPIO as GPIO


def init(pin,freq = 50):
    GPIO.PWM(pin,freq)

def start(dc =50):
