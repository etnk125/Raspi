import RPi.GPIO as GPIO

from .module import pi, toggle

PIN_I = 3
PIN_O = 5


class Main:
    def __init__(self) -> None:
        self.count = 0
        pi.init()
        # pull up
        pi.use_switch(PIN_I, self.sw_handle)
        pi.outp(PIN_O)
        toggle.toggle(PIN_O, False)

    def sw_handle(self, e):
        self.count += 1
        print(self.count % 2)
        toggle.toggle(PIN_O, condition=self.count % 2 == 1)


def main():
    Main()

    input()


if __name__ == '__main__':
    main()
