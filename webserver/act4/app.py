from flask import Flask, render_template, request, redirect, url_for, flash, Markup, jsonify
import datetime
import RPi.GPIO as GPIO


app = Flask(__name__)


@app.route('/')
def index():
    print("start webpage")
    return render_template('index.html')


@app.route('/updateTime')
def updateTime():
    print('update time and button input')
    P_IN = 5
    state = GPIO.input(P_IN)
    Button_Status = "ON" if state else "OFF"
    print(state,Button_Status)
    now = datetime.datetime.now()
    timeString = "TIME: " + now.strftime("%H:%M:%S")
    UpdateTimeOnweb = {
        'ButtonStatus': Button_Status,
        'Time': timeString
    }
    return jsonify(**UpdateTimeOnweb)


def GPIO_init(GPIO):
    P_OUT = 3
    P_IN = 5
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(P_OUT, GPIO.OUT)
    GPIO.setup(P_IN, GPIO.IN)


if __name__ == '__main__':
    GPIO_init(GPIO)
    app.run(debug=True, host='0.0.0.0', port=80)
