import time
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

import RPi.GPIO as GPIO

import Adafruit_ADS1x15

def gpio_init():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

def outp(pin:int):
    GPIO.setup(pin,GPIO.OUT)

def use_switch(pin,handle = None ):
    GPIO.setup(pin,GPIO.IN,pull_up_down = GPIO.PUD_UP)
    GPIO.add_event_detect(pin,GPIO.FALLING,callback = handle,bouncetime=100)

def connect(SheetName,GSheet_OAUTH_JSON,worksheet_name,scope):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        GSheet_OAUTH_JSON, scope)
    client = gspread.authorize(credentials)
    worksheet = client.open(SheetName).worksheet(worksheet_name)
    return worksheet

# clear and setup  wks
def worksheet_reset(worksheet,row,index=1 ):
    worksheet.clear()
    worksheet.insert_row(row, index)

def main():
    main_class = Main()
    main_class.run()

   

class Main:
    # config data
    SheetName = "data logger online"
    GSheet_OAUTH_JSON = "key.json"
    worksheet_name = "minitest"
    scope = ["https://spreadsheets.google.com/feeds",
            "https://www.googleapis.com/auth/drive"]
    GAIN = 1
    PORT = 0
    PIN_SW = 7
    row = [ "Time","FSR","FSR_level (change level every 2000 point)"]
    # using adc
    adc = Adafruit_ADS1x15.ADS1115()
    def __init__(self):
        # connect
        self.worksheet = connect(self.SheetName,self.GSheet_OAUTH_JSON,self.worksheet_name,self.scope)

        # config worksheet
        worksheet_reset(self.worksheet,self.row)

        # using gpio
        gpio_init()

        # using switch
        outp(self.PIN_SW)
        use_switch(self.PIN_SW,self.sw_handle)


    def sw_handle(self,e):
        print('reset')
        worksheet_reset(self.worksheet,self.row)
    def run(self):
        while True:
            # get timestmap
            now = datetime.now()
            timestamp = now.strftime("%H:%M:%S")

            # get fsr value
            value = max(self.adc.read_adc(self.PORT,self.GAIN),0)

            # convert to level
            level = ['low ','mid ','high'][min(2,int(value/2000))]

            try:
                self.worksheet.append_row([timestamp,value,level])
                print(timestamp,value,level)
            except:
                print("Google sheet login failed with error:", Exception)
            time.sleep(2)

if __name__ == "__main__":
    main()