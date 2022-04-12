import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt  # pip3 install paho-mqtt
import json
import random

import Adafruit_ADS1x15
adc = Adafruit_ADS1x15.ADS1115()

myData = {"ID": 123, "value": 0}

# Initialize Netpie information
NETPIE_HOST = "broker.netpie.io"
CLIENT_ID = "9c389ca8-6e95-4063-916d-52f284b5684d"  # YOUR CLIENT ID
DEVICE_TOKEN = "tYEw2842zc1iWR6zHHMhcrtpeTYaaCN2"  # YOUR TOKEN

# Function to react with NETPIE


def on_connect(client, userdata, flags, rc):
    print("Result from connect : {}".format(mqtt.connack_string(rc)))
    client.subscribe("@shadow/data/updated")


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribe successful")

def gpio_init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(7, GPIO.OUT)

def adc_val():
    return max(adc.read_adc(0),0)

def on_message(client, userdata, msg):
    load = json.loads(msg.payload)
    print(load['data'])
    if load['data'].get('led') is not None:
        print(load['data']['led'])
        if load['data']['led']=="ON":
            GPIO.output(7, GPIO.HIGH)
        if load['data']['led']=="OFF":
            GPIO.output(7, GPIO.LOW)

            # Connecting to NETPIE
client = mqtt.Client(protocol=mqtt.MQTTv311,
                     client_id=CLIENT_ID, clean_session=True)
client.username_pw_set(DEVICE_TOKEN)
client.on_connect = on_connect
client.on_message = on_message
client.connect(NETPIE_HOST, 1883)
client.loop_start()
gpio_init()
value = 0
try:
    while True:

        myData['value'] = adc_val()
        myData['ID'] = "123"

        # send myData (in JSON from) to NETPIE2020 shadow
        client.publish("@shadow/data/update", json.dumps({"data": myData}), 1)
        time.sleep(3)

except KeyboardInterrupt:
    print('Disconnecting successful')
    GPIO.cleanup()
