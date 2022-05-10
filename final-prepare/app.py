
import os
from flask import Flask, request, make_response, jsonify

# create flask app
app = Flask(__name__)
log = app.logger


@app.route("/", methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
#    print(req.get('queryResult').get('parameters').get('place'))

    try:
        action = req.get('queryResult').get('intent').get('displayName')
    except AttributeError:
        return 'json error'
    # action switcher
    res = ""
    if action == 'AQI':
        res = "AQI"
    elif action == 'TEMP':
        res = "TEMP"
    else:
        log.error('Unexpected action.')

    print('Action: ' + str(action))
    print('Response: ' + res)
    # print(json.dumps(req, indent=2, sort_keys=True))
    # return response
    return make_response(jsonify({'fulfillmentText': res}))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=int(
        os.environ.get('PORT', '5000')))
