import time
from datetime import datetime
# import Adafruit_ADS1x15
# import RPi.GPIO as GPIO
import gspread
from oauth2client.service_account import ServiceAccountCredentials

SheetName = "data logger online"
GSheet_OAUTH_JSON = "key.json"
scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    GSheet_OAUTH_JSON, scope)
client = gspread.authorize(credentials)
worksheet = client.open(SheetName).get_worksheet(0)

# clear worksheet
worksheet.clear()

# set worksheet
row = ["Date", "Time"]
index = 1
worksheet.insert_row(row, index)

while True:
    now = datetime.now()
    date = now.strftime("%d/%m/%Y")
    timestamp = now.strftime("%H:%M:%S")
    try:
        worksheet.append_row([date, timestamp])
    except:
        print("Google sheet login failed with error:", Exception)
    time.sleep(2)
