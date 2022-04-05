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
    print("update time")
    now = datetime.datetime.now()
    timeString = "TIME: " + now.strftime("%H:%M:%S")
    return jsonify(timeupdate=timeString)


@app.route('/<pin>/<action>')
def LEDControl(pin, action):
    print('Control LED')


def GPIO_init(GPIO):
    P_OUT = 3
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(P_OUT, GPIO.OUT)


if __name__ == '__main__':
    GPIO_init(GPIO)
    app.run(debug=True, host='0.0.0.0', port=80)
