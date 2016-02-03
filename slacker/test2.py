# -*- coding: utf-8 -*-
import time, json, re ,os
from slackclient import SlackClient
from config  import *

print "API token is %s"  %  (SLACK_API_TOKEN)

slack = SlackClient(SLACK_API_TOKEN)

print slack.api_call("api.test")

# Send a message to #general channel
#slack.rtm_send_message("#testinbot","ready to roll")
print slack.api_call('chat.postMessage',username='BigBot',as_user=True,channel="#testinbot",text="bot ready to roll")
#slack.chat.post_message('#testinbot', 'Hello fellow slackers!', as_user=True)

print "post message done"


if slack.rtm_connect():
    while True:
        new_evts = slack.rtm_read()
    	for evt in new_evts:
      	    print(evt)
            if "type" in evt:
        	    if evt["type"] == "message" and evt["user"] != 'U0GP2A4P2' and "text" in evt:
          		    message=evt["text"]
          		    print message
          		    print slack.api_call('chat.postMessage',username='BigBot',as_user=True,channel="#testinbot",text=message)
          		    time.sleep(2)
    time.sleep(5)


else:
	print "\n\n\nconnection failed\n\n"