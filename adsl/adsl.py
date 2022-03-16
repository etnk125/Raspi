import time 
import Adafruit_ADS1x15
from module import pi

adc = Adafruit_ADS1x15.ADS1115()

GAIN = 1

OUT_PIN = 7

pi.init()
pi.outp(OUT_PIN)
pwm = pi.GPIO.PWM(OUT_PIN,50)
max_val=1
pwm.start(1)

while True:
    value = max(adc.read_adc(0,gain=GAIN),0)
    max_val = max(value,max_val)
    pwm.ChangeDutyCycle(100*value/max_val)
    print(value)
    time.sleep(0.2)
pwm.stop()