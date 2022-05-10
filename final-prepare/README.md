# Final Exam

## ins

- RPI
  - random value every 3 sec
    - aqi 0 - 100
    - pm2.5 0 - 250
  - Save on gg sheet [Time ,AQI ,PM]
- netpie 
  - if both value > 50 trigger to line noti (write on netpie)
  - show latest value on gauge
- chat bot
  - user can req AQI and temp value (separate intents)
    - latest
    - search by time

## solution

- create data logger , make key.json file
  - see data logger asg8
- line noti
  - using line noti gen key from this https://notify-bot.line.me/my/
  - then write on netpie event hook and trigger 
  - event hook
  
    ```่json
    {
      "body": "message={{msg}}",
      "header": {
      "Authorization": "Bearer {{option.linetoken}}",
      "Content-Type": "application/x-www-form-urlencoded"
    },
      "method": "POST",
      "uri": "https://notify-api.line.me/api/notify",
    }
    ```
  -  https://docs.netpie.io/device-config.html#device-trigger-and-event-hook
    ```json
    {
      "enabled": true,
      "trigger": [
        {
          "action": event hook name,
          "event": "SHADOW.UPDATED",
          "condition": see link ,this is ex"$NEW.value > 50 && $NEW.msg> 50 ",
          "msg": "AQI and PM is over 50 -> AQI :  {{$NEW.value}} PM :  {{$NEW.msg}}",
          "option": {
            "linetoken": your line token
          }
        }
      ]
    }
    ```
- chat bot
  - signin dialog flow
  - line dev
  - apply dialog flow line 
  - copy dialog flow webhook to line
- config chatbot
  - create intent
  - ngrok https://dashboard.ngrok.com/
  - ./ngrok http 5000 on extraction file
  - copy forwarding to dialog flow fulfilment tab
