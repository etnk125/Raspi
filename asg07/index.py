# general
import lcddriver
import Adafruit_ADS1x15
from luma.core.virtual import viewport, sevensegment
from luma.core.interface.serial import spi, noop
from luma.led_matrix.device import max7219
import time
from datetime import datetime

# pi
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

# 7seg

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=1)
seg = sevensegment(device)
# seg.text = 'hh1'


# adc
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1

# lcd 16x4
lcd = lcddriver.lcd()


class Main:
    def __init__(self):
        seg.text = 'ee'
        while True:
            inp = max(0, adc.read_adc(0))
            seg.text = str(inp)
            display = ['low ', 'mid ', 'high'][min(2, int(inp/1000))]
            lcd.lcd_display_string(display, 1)
            print(inp, display)
            time.sleep(0.1)


def main():
    Main()
    input()


if __name__ == '__main__':
    main()
