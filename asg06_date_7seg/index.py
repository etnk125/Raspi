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

class Main:
    def __init__(self) -> None:
        init()

        self.serial = spi(port=0, device=0, gpio=noop())
        self.device = max7219(self.serial, cascaded=1)
        self.seg = sevensegment(self.device)
        
        self.clock()

    def clock(self):
        while True:
            now = datetime.now()
            self.seg.text = now.strftime("  %H.%M.%S")
            time.sleep(1)
        

def main():
    Main()

if __name__ == '__main__':
    main()