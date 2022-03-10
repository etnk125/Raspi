from .module import pi, blink

import RPi.GPIO as GPIO
import time

PIN_I = 3
PIN_O = 5


def sw_handle(e):
    blink.blink(PIN_O, delay=0.3, round=3)


def main():
    pi.init()
    pi.use_switch(PIN_I, sw_handle)
    pi.outp(PIN_O)

    input()


if __name__ == '__main__':
    main()
