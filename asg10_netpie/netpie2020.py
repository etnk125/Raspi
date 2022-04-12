import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt  # pip3 install paho-mqtt
import json
import random

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


def on_message(client, userdata, msg):
    print(str(msg.payload))
    data = str(msg.payload).split(",")
    print(data)
    for e in data:
        current = e.split(': ')
        if current[0].replace('"', "") == 'led':
            print(e)


            # Connecting to NETPIE
client = mqtt.Client(protocol=mqtt.MQTTv311,
                     client_id=CLIENT_ID, clean_session=True)
client.username_pw_set(DEVICE_TOKEN)
client.on_connect = on_connect
client.on_message = on_message
client.connect(NETPIE_HOST, 1883)
client.loop_start()

value = 0
try:
    while True:

        myData['value'] = random.randint(0, 1000)
        myData['ID'] = "123"

        # send myData (in JSON from) to NETPIE2020 shadow
        client.publish("@shadow/data/update", json.dumps({"data": myData}), 1)
        time.sleep(5)

except KeyboardInterrupt:
    print('Disconnecting successful')
    GPIO.cleanup()
