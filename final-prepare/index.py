# Natthawee Koengfak 6213125
# https://docs.google.com/spreadsheets/d/1-Hp5QSB9J4o3Ljcb1Mn9XatZvVPePCXGoufBd5jaR5k/edit?usp=sharing
# using time
import time
from datetime import datetime
# using random
import random
# using gg sheet
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# using netpie
import paho.mqtt.client as mqtt  # pip3 install paho-mqtt
import json

# using gpio
import RPi.GPIO as GPIO

# using fsr,adc
# import Adafruit_ADS1x15

# using 7seg
# from luma.led_matrix.device import max7219
# from luma.core.interface.serial import spi, noop
# from luma.core.virtual import viewport, sevensegment

# using lcd
# import lcddriver
# lcd = lcddriver.lcd()

# Initialize Netpie information
NETPIE_HOST = "broker.netpie.io"
CLIENT_ID = "9c389ca8-6e95-4063-916d-52f284b5684d"  # YOUR CLIENT ID
DEVICE_TOKEN = "tYEw2842zc1iWR6zHHMhcrtpeTYaaCN2"  # YOUR TOKEN


def on_connect(client, userdata, flags, rc):
    print("Result from connect : {}".format(mqtt.connack_string(rc)))
    client.subscribe("@shadow/data/updated")


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribe successful")


def on_message(client, userdata, msg):
    load = json.loads(msg.payload)
    print(load['data'])
    if load['data'].get('msg') is not None:
        print(
            load['data']['msg']+datetime.now().strftime(" %H:%M:%S"), 1)

        # Connecting to NETPIE


# gpio init
def gpio_init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

# set i/p


def inp(pin: int):
    GPIO.setup(pin, GPIO.IN)


# set o/p
def outp(pin: int):
    GPIO.setup(pin, GPIO.OUT)


# connect ggs
def connect(SheetName, GSheet_OAUTH_JSON, worksheet_name, scope):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        GSheet_OAUTH_JSON, scope)
    client = gspread.authorize(credentials)
    worksheet = client.open(SheetName).worksheet(worksheet_name)
    return worksheet


# clear and setup  wks
def worksheet_reset(worksheet, row, index=1):
    worksheet.clear()
    worksheet.insert_row(row, index)


def toggle(pin, condition=False):
    GPIO.output(pin, GPIO.HIGH if condition else GPIO.LOW)


def main():

    main_class = Main()
    main_class.run()


class Main:
    # config data
    SheetName = "data logger online"
    GSheet_OAUTH_JSON = "key.json"
    worksheet_name = "final"

    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/drive"]
    row = ["Time", "Value"]

    myData = {"ID": 123, "value": 0, "msg": "", "time": ""}
    GAIN = 1
    PORT = 0
    # using fsr
    # adc = Adafruit_ADS1x15.ADS1115()

    # netpie client
    client = mqtt.Client(protocol=mqtt.MQTTv311,
                         client_id=CLIENT_ID, clean_session=True)
    fahrenheit = False

    def __init__(self):
        # connect to netpie
        self.client.username_pw_set(DEVICE_TOKEN)
        self.client.on_connect = on_connect
        self.client.on_message = on_message
        self.client.connect(NETPIE_HOST, 1883)
        self.client.loop_start()

        # connect worksheet
        self.worksheet = connect(
            self.SheetName, self.GSheet_OAUTH_JSON, self.worksheet_name, self.scope)

        # config worksheet
        worksheet_reset(self.worksheet, self.row)

        # using gpio
        gpio_init()

    def run(self):
        while True:
            # get timestmap
            now = datetime.now()
            timestamp = now.strftime("%H:%M:%S")
            # value = max(self.adc.read_adc(self.PORT, self.GAIN), 0)

            AQI = random.randint(0, 100)
            PM = random.randint(0, 250)

            if AQI > 50 or PM > 50:
                print('send line notify')

            self.myData['value'] = AQI

            self.myData['msg'] = PM
            self.myData['time'] = timestamp

            self.myData['ID'] = "123"
            # self.seg.text = str(value)

            try:
                self.client.publish("@shadow/data/update",
                                    json.dumps({"data": self.myData}), 1)
                self.worksheet.append_row([timestamp, AQI, PM])
                # print(self.myData)
            except Exception as ex:
                print("Google sheet login failed with error:", ex)
            time.sleep(3)


if __name__ == "__main__":
    main()
