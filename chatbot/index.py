# import
from flask import Flask, request, make_response, jsonify
import RPi.GPIO as GPIO
import os
import json
##

# create flask app
app = Flask(__name__)
log = app.logger

# recieve request from webhook

def gpio_init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(7, GPIO.OUT)




@app.route("/", methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
#    print(req.get('queryResult').get('parameters').get('place'))

    try:
        action = req.get('queryResult').get('intent').get('displayName')
    except AttributeError:
        return 'json error'
    # action switcher
    res=""
    if action == 'TurnOnLED':
        res = turn_on(req)
    elif action == 'TurnOffLED':
         res = turn_off(req)
    else:
         log.error('Unexpected action.')
   

    print('Action: ' + str(action))
    print('Response: ' + res)
    # print(json.dumps(req, indent=2, sort_keys=True))
    # return response
    return make_response(jsonify({'fulfillmentText': res}))


def turn_off(req):
    
    GPIO.output(7, GPIO.LOW)
    return 'Finish off'


def turn_on(req):
    GPIO.output(7, GPIO.HIGH)
    return 'Finish on'


# run flask app
if __name__ == '__main__':
    gpio_init()
    app.run(host='0.0.0.0', debug=True, port=int(
        os.environ.get('PORT', '5000')))
