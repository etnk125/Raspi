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
    worksheet_name = ['AQI', 'TEMP']

    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/drive"]
    row = ["Time", "Value"]

    myData = {"ID": 123, "temp": 0, "aqi": 0}
    GAIN = 1
    PORT = 0
    # led
    PIN_O = 7
    # using fsr
    # adc = Adafruit_ADS1x15.ADS1115()

    # netpie client
    client = mqtt.Client(protocol=mqtt.MQTTv311,
                         client_id=CLIENT_ID, clean_session=True)

    def __init__(self):
        # connect to netpie
        self.client.username_pw_set(DEVICE_TOKEN)
        self.client.on_connect = on_connect
        self.client.on_message = on_message
        self.client.connect(NETPIE_HOST, 1883)
        self.client.loop_start()

        # connect worksheet
        self.worksheet = {}
        self.worksheet[0] = connect(
            self.SheetName, self.GSheet_OAUTH_JSON, self.worksheet_name[0], self.scope)
        self.worksheet[1] = connect(
            self.SheetName, self.GSheet_OAUTH_JSON, self.worksheet_name[1], self.scope)

        # config worksheet
        for ws in self.worksheet.values():
            worksheet_reset(ws, self.row)

        # using gpio
        gpio_init()

        # using led
        outp(self.PIN_O)
        # toggle(self.PIN_O, self.status)

        # 7seg
        # self.serial = spi(port=0, device=0, gpio=noop())
        # self.device = max7219(self.serial, cascaded=1)
        # self.seg = sevensegment(self.device)

        # using fahrenheit or celsius
        self.fahrenheit = False

    def run(self):
        while True:
            # get timestmap
            now = datetime.now()
            timestamp = now.strftime("%H:%M:%S")
            # value = max(self.adc.read_adc(self.PORT, self.GAIN), 0)

            AQI = random.randint(0, 200)
            TEMP = random.randint(0, 45)

            toggle(self.PIN_O, AQI > 100)

            self.myData['AQI'] = AQI

            self.myData['TEMP'] = self.get_temp(TEMP)
            self.myData['time'] = timestamp
            self.myData['ID'] = "123"
            # self.seg.text = str(value)

            try:
                self.client.publish("@shadow/data/update",
                                    json.dumps({"data": self.myData}), 1)
                self.worksheet[0].append_cell([timestamp, AQI])
                self.worksheet[1].append_cell([timestamp, TEMP])
                print(self.myData)
            except Exception as ex:
                print("Google sheet login failed with error:", ex)
            time.sleep(5)

    def toggle_fahrenheit(self):
        self.fahrenheit = not self.fahrenheit

    def get_temp(self, TEMP=0):
        return TEMP + "Celsius" if self.fahrenheit else (TEMP * 9 / 5 + 32) + "Fahrenheit"


if __name__ == "__main__":
    main()
