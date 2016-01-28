from slacker import Slacker
from config  import *

print "API token is %s"  %  (SLACK_API_TOKEN)

slack = Slacker(SLACK_API_TOKEN)

# Send a message to #general channel
slack.chat.post_message('#testchannel', 'Hello fellow slackers!', as_user=True)

# Get users list
response = slack.users.list()
users = response.body['members']

# Upload a file
slack.files.upload('hello.txt')

# Gat user details
user_info = slack.user.info("@anand")

print user_info


