import time 
import Adafruit_ADS1x15
import RPi.GPIO as GPIO

adc = Adafruit_ADS1x15.ADS1115()

GAIN = 1

OUT_PIN = 7

def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

def outp(pin:int):
    GPIO.setup(pin,GPIO.OUT)

class Main:
    def __init__(self) -> None:
        init()
        outp(OUT_PIN)
        self.pwm = GPIO.PWM(OUT_PIN,50)
        max_val=1
        self.pwm.start(1) 

        while True:
            value = max(adc.read_adc(0,gain=GAIN),0)
            max_val = max(value,max_val)
            self.pwm.ChangeDutyCycle(100*value/max_val)
            print(value,max_val)
            time.sleep(0.2)

def main():
   Main()

   


if __name__ == "__main__":
    main()