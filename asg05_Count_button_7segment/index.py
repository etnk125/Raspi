import time
from datetime import datetime
import RPi.GPIO as GPIO

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.virtual import viewport, sevensegment

PIN_I = 3


def init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

def outp(pin:int):
    GPIO.setup(pin,GPIO.OUT)

def inp(pin:int):
    GPIO.setup(pin,GPIO.IN)
    
def use_switch(pin,handle = None ):
    GPIO.setup(pin,GPIO.IN,pull_up_down = GPIO.PUD_UP)
    GPIO.add_event_detect(pin,GPIO.FALLING,callback = handle,bouncetime=200)

class Main:
    def __init__(self) -> None:
        self.count = 0
        init()
        # pull up
        use_switch(PIN_I, self.sw_handle)
        inp(PIN_I)

        self.serial = spi(port=0, device=0, gpio=noop())
        self.device = max7219(self.serial, cascaded=1)
        self.seg = sevensegment(self.device)
        
        self.seg.text = str(self.count)
        

    def sw_handle(self, e):
        self.count += 1
        print(self.count)
        self.seg.text = str(self.count)


def main():
    Main()
    input()

if __name__ == '__main__':
    main()