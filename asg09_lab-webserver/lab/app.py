from flask import Flask, render_template, request, redirect, url_for, flash, Markup, jsonify
import datetime
import RPi.GPIO as GPIO
import Adafruit_ADS1x15

state = True

adc = Adafruit_ADS1x15.ADS1115()
app = Flask(__name__)


@app.route('/')
def index():
    print("start webpage")
    return render_template('index.html')


@app.route('/updateTime')
def updateTime():
    print('update time and button change ads val to perc')

    now = datetime.datetime.now()
    timeString = "TIME: " + now.strftime("%H:%M:%S")
    global state
    OutputType = "value" if state else "percent"
    OutputValue = adc_val(state)
    UpdateTimeOnweb = {
        'type': OutputType,
        'value': OutputValue,
        'timeupdate': timeString
    }
    return jsonify(**UpdateTimeOnweb)


@app.route('/changeState')
def changeState():
    global state
    state = not state
    print(state)
    return jsonify(state=state)


def GPIO_init(GPIO):
    global state
    global max_val
    max_val = 1
    state = True
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    # GPIO.setup(P_OUT, GPIO.OUT)
def adc_val(state):
    val = max(adc.read_adc(0),0)
    global max_val 
    max_val = max(val,max_val )
    if(state):
        return val
    return int(val/max_val*100)
    

if __name__ == '__main__':

    GPIO_init(GPIO)
    app.run(debug=True, host='0.0.0.0', port=80)
