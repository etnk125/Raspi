# Natthawee Koengfak 6213125
# https://docs.google.com/spreadsheets/d/1-Hp5QSB9J4o3Ljcb1Mn9XatZvVPePCXGoufBd5jaR5k/edit?usp=sharing
import time
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

import RPi.GPIO as GPIO

import Adafruit_ADS1x15


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


def main():
    main_class = Main()
    main_class.run()


class Main:
    # config data
    SheetName = "data logger online"
    GSheet_OAUTH_JSON = "key.json"
    worksheet_name = "mini lab"
    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/drive"]
    row = ["Time", "Value"]
    GAIN = 1
    PORT = 0
    # led
    # PIN_O = 3
    adc = Adafruit_ADS1x15.ADS1115()

    def __init__(self):

        # connect
        self.worksheet = connect(
            self.SheetName, self.GSheet_OAUTH_JSON, self.worksheet_name, self.scope)

        # config worksheet
        worksheet_reset(self.worksheet, self.row)

        # using gpio
        gpio_init()

        # using led
        # outp(self.PIN_O)
        # toggle(self.PIN_O, self.status)

    def run(self):
        while True:
            # get timestmap
            now = datetime.now()
            timestamp = now.strftime("%H:%M:%S")
            value = max(self.adc.read_adc(self.PORT, self.GAIN), 0)

            cells = self.worksheet.range('A2:B2')
            cells[0].value = timestamp
            cells[1].value = value

            try:
                self.worksheet.update_cells(cells)
                print(timestamp, value)
            except Exception as ex:
                print("Google sheet login failed with error:", ex)
            time.sleep(2)


if __name__ == "__main__":
    main()
