# -*- coding: utf-8 -*-

# this script has functions to give commands to the slack bot "Big Bot"
#The config file in the same folder has the token for the Big Bot
import time, json, re ,os
from slackclient import SlackClient
from config  import *
import requests

# The following method makes a call to the google maps api . The api returns a json from where we take the formatted address
 
def maps(latitude,longitude):
    
    #The below javascript code when run in browser console will give you thelatitude and longitude of the current position
    # navigator.geolocation.getCurrentPosition(function(p) {
    #   console.log(p);
    # })



    #This variable has to be set as true or false depending on whether latitude and longitude have been gotten from
    # a location sensor
    sensor = 'true'

    base = "http://maps.googleapis.com/maps/api/geocode/json?"
    params = "latlng={lat},{lon}&sensor={sen}".format(
        lat=latitude,
        lon=longitude,
        sen=sensor
    )
    url = "{base}{params}".format(base=base, params=params)
    response = requests.get(url)
    return response.json()['results'][0]['formatted_address']


#The following function uses the above maps function to get the address of a place after getting latitude and longitude from the user
#The function takes a slackclient instance as argument as well as message. If message is address then it activates
#If message is address then the function looks to get latitude and longitude and returns true.
#If message is not address function returns flase

def getAddress(slack,message):
  if message=="address":
    latitude= 0.0
    longitude = 0.0
    #Below 2 variables used to get out of loop when latitude/longitude entered
    got_latitude="false"
    got_longitude="false"
    #12.891990999999999,77.64160729999999, myntra latitude and longitude just for curiosity

    #Below line calls chat.postMessage method of the Slack API to post "Enter latitude " as the bot
    print slack.api_call('chat.postMessage',username='BigBot',as_user=True,channel="#testinbot",text="Enter latitude")

    #following loop loops till the latitude has been entered by the user
    while True:
      #below line initializes a list by all the events read by the slackclient instance(bot)
      new_evts = slack.rtm_read()
      for evt in new_evts:
                print(evt)
                if "type" in evt:
                  # if evt type is a message and the message is not from the bot user id U0GP2A4P2' is of the bot 
                  # and the message is not empty read the message
                  if evt["type"] == "message" and evt["user"] != 'U0GP2A4P2' and "text" in evt:
                      message=evt["text"]
                      #convert the string to a float.
                      latitude = float(message)
                      print slack.api_call('chat.postMessage',username='BigBot',as_user=True,channel="#testinbot",text="latitude entered")
                      got_latitude="true"
                      #latitude entered checked
                      break
      #the below line checks if latitude was entered. If it was then you break from the loop waiting for latitude to be entered
      if got_latitude=="true":
        break

    # similar procedure as above followed for longitude.
    #Below line calls chat.postMessage method of the Slack API to post "Enter longitude " as the bot
    print slack.api_call('chat.postMessage',username='BigBot',as_user=True,channel="#testinbot",text="Enter longitude")

    #following loop loops till the latitude has been entered by the user
    while True:
      #below line initializes a list by all the events read by the slackclient instance(bot)
      new_evts = slack.rtm_read()
      for evt in new_evts:
                print(evt)
                if "type" in evt:
                  # if evt type is a message and the message is not from the bot user id U0GP2A4P2' is of the bot 
                  # and the message is not empty read the message
                  if evt["type"] == "message" and evt["user"] != 'U0GP2A4P2' and "text" in evt:
                      message=evt["text"]
                      longitude = float(message)
                      print slack.api_call('chat.postMessage',username='BigBot',as_user=True,channel="#testinbot",text="longitude entered")
                      got_longitude="true"
                      #longitude entered check
                      break
      #the below line checks if latitude was entered. If it was then you break from the loop waiting for latitude to be entered
      if got_longitude=="true":
        break

    #below line makes a call to maps function with the given latitude and longitude and gives the user the address of 
    # the co-ordinates he/she entered
    print slack.api_call('chat.postMessage',username='BigBot',as_user=True,channel="#testinbot",text=maps(latitude,longitude))
    return True
  return False              


#function to say respond to Good Morning
def sayGoodMorning(message):
  if(message == "Good Morning"):
    print slack.api_call('chat.postMessage',username='BigBot',as_user=True,channel="#testinbot",text="Very Good Morning to you too")
    return True
  return False

#function to respond to "You are smart"
def sayThankYou(message):
  if(message == "You are smart"):
    print slack.api_call('chat.postMessage',username='BigBot',as_user=True,channel="#testinbot",text="Muchas Gracias!")
    return True
  return False


print ("API token is %s"  %  (SLACK_API_TOKEN))

# create a  slackclient instance using the API token got from config file.
slack = SlackClient(SLACK_API_TOKEN)

#check for slack api connection made or not
print slack.api_call("api.test")

# Send a message to #general channel
#slack.rtm_send_message("#testinbot","ready to roll")
print slack.api_call('chat.postMessage',username='BigBot',as_user=True,channel="#testinbot",text="bot ready to roll")

#just a checker for the script
print "post message done"

#rtm_connect method makes a rtm connection with the rtm API of slack
if slack.rtm_connect():
    #following loop keeps reading events detected by bot
    while True:
      # rtm_read keeps reading events detected by bot
      new_evts = slack.rtm_read()
      # loop through all events
      for evt in new_evts:
            print(evt)
            if "type" in evt:
              # if event  is a message and the message is not by the bot read the message
              if evt["type"] == "message" and evt["user"] != 'U0GP2A4P2' and "text" in evt:
                  message=evt["text"]
                  print message
                  #if message has no defined action then post the command as it is
                  if (not(sayGoodMorning(message) or sayThankYou(message) or getAddress(slack,message))):
                    print slack.api_call('chat.postMessage',username='BigBot',as_user=True,channel="#testinbot",text=message)
                  
                  
                  
                 
                    

                  
    # suspend execution of script for 1 second.. arbritartily chosen time currently             
    time.sleep(1)

# if connection failed: print it
else:
  print "\n\n\nconnection failed\n\n"