from RPi.GPIO import HIGH,LOW,output
from time import sleep 

def toggle(pin,condition=False):
    output(pin,HIGH if condition else LOW) 

    
