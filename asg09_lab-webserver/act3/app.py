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
    print('update time and button change ads val to perc')

    now = datetime.datetime.now()
    timeString = "TIME: " + now.strftime("%H:%M:%S")

    OutputType = State.state()
    OutputValue = 100 if OutputType else 40000
    UpdateTimeOnweb = {
        'type': OutputType,
        'value': OutputValue,
        'Time': timeString
    }
    return jsonify(**UpdateTimeOnweb)


@app.route('/changeState')
def changeState():
    State.toggle()
    return jsonify(state=State.state)


def GPIO_init(GPIO):
    P_OUT = 3
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(P_OUT, GPIO.OUT)


class State:
    state = True

    def toggle(self):
        self.state = not self.state


if __name__ == '__main__':

    GPIO_init(GPIO)
    app.run(debug=True, host='0.0.0.0', port=80)
