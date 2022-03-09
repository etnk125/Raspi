
import RPi.GPIO as GPIO
import sys
import time
sys.path.append('./module')
import pi
import toggle

PIN_I = 3
PIN_O = 5

class Main:
    def __init__(self) -> None:
        self.count = 0
        pi.init()
        # pull up
        pi.use_switch(PIN_I,self.sw_handle)
        pi.outp(PIN_O)

    def sw_handle(self,e):
        self.count+=1
        print(self.count%4)
        toggle.toggle(PIN_O,condition = self.count%4==0)
def main():
    Main()
    
    input()

if __name__ == '__main__':
    main()