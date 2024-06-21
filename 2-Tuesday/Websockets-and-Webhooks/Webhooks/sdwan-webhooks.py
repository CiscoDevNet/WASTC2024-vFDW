from flask import Flask, request, jsonify
from webexteamssdk import WebexTeamsAPI
import json
import os
import datetime
import pytz

bearer_token = os.environ.get("bearer_token")
room_id = os.environ.get("room_id")

app = Flask(__name__)

@app.route('/',methods=['POST'])
def alarms():
   try:
      PDT = pytz.timezone('Australia/Melbourne')
      data = json.loads(request.data)
      print(data)
      message =  '''Team, Alarm event : **''' + data['rule_name_display'] + '''** is received from vManage and here are the complete details <br><br>'''

      temp_time = datetime.datetime.utcfromtimestamp(data['entry_time']/1000.)
      temp_time = pytz.UTC.localize(temp_time)
      message = message + '**Alarm Date & Time:** ' + temp_time.astimezone(PDT).strftime('%c') + ' PDT'
      temp = data['values_short_display']
      for item in temp:
          for key, value in item.items():
              message = message + '<br> **' + key + ':** ' + value

      message = message + '<br> **' + 'Details:' + '** ' + "https://test.sdwanlab.com/#/app/monitor/alarms/details/" + data['uuid']
      
      api = WebexTeamsAPI(access_token=bearer_token)
      res=api.messages.create(roomId=room_id, markdown=message)
      print(res)
    
   except Exception as exc:
      print(exc)
      return jsonify(str(exc)), 500
   
   return jsonify("Message sent to Webex Teams"), 200

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5001, debug=True)