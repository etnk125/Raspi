
import os
from flask import Flask, request, make_response, jsonify
# using gg sheet
import gspread
from oauth2client.service_account import ServiceAccountCredentials
# create flask app
app = Flask(__name__)
log = app.logger


def connect(SheetName, GSheet_OAUTH_JSON, worksheet_name, scope):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        GSheet_OAUTH_JSON, scope)
    client = gspread.authorize(credentials)
    worksheet = client.open(SheetName).worksheet(worksheet_name)
    return worksheet


SheetName = "data logger online"
GSheet_OAUTH_JSON = "key.json"
worksheet_name = "final"
scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]
# connect worksheet
worksheet = connect(
    SheetName, GSheet_OAUTH_JSON, worksheet_name, scope)
# connect ggs


@app.route("/", methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    # print(req.get('queryResult').get('parameters').get('time'))

    try:
        action = req.get('queryResult').get('intent').get('displayName')
    except AttributeError:
        return 'json error'
    # action switcher
    
    datas= worksheet.get_all_records()
    time_param = req.get('queryResult').get('parameters').get('time')
    data = datas[-1]
    if time_param is not None:
        for i in datas:
            if i['Time'] == time_param:
                data=i
                break
    res = ""
    if action == 'AQI':
        res = "AQI : "+ str(data[action])
    elif action == 'PM':
        res = "PM2.5 : "+ str(data[action])
    else:
        log.error('Unexpected action.')
   

    print(data)
    print('Action: ' + str(action))
    print('Response: ' + res)
    # print(json.dumps(req, indent=2, sort_keys=True))
    # return response
    return make_response(jsonify({'fulfillmentText': res}))


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=int(
        os.environ.get('PORT', '5000')))
