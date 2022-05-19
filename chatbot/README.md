# solution for create chatbot
## setup
### line chatbot

1. go to https://developers.line.biz/ 
2. create a provider
3. create a channel
4. select message api
5. goto Messaging API tab 
   1. issue a token
   2. edit auto reply message
      - response mode : bot
      - greeting message : disable
      - auto response : disable
      - webhooks : enable

### dialog flow 

1. goto https://console.dialogflow.com/
2. create new agent

### integration 
1. go to integrations tab in dialog flow
2.  enable line -> use information from Line to fill form
       - chanel ID 
       - channel secret
       - channel access token
3. copy webhooks url from dialog flow
4. goto messaging api ->  webhooks setting -> paste url from step 3 -> verify

## config dialog flow intents

1. create new intent
2. add intent name
3. add training phrase
4. add response message
5. test intent from test tab and line

## deploy own server

1. install [ngrok](https://ngrok.com/)
2. download pi version from above link
   ```cmd
   cd Downloads
   <!-- unzip it -->
    unzip ngrok-stable-linux-arm.zip
    <!-- auth -->
    <!-- see auth token after login ngrok  -->
    ngrok authtoken <token>
    ngrok http 5000

   ```
3. copy forwarding url from ngrok 
4. place in dialog flow fulfillment webhook and enable it
5. **don't forget to enable webhook in  intent you want to use**