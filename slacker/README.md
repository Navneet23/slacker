# slacker

Slacker does not have rtm support which is needed to read messages from slack.
So we are using SlackClient API. SlackSocket is another API that has RTM support.
test4.py has the updated code. 

It has been heavily commented.

The Big Bot can read messages and 3 sample commands have been made.

One command responds to Good Morning

One command responds to You are smart

And the third command "address" Prompts the user to give latitude and longitude 
and then connects with the google maps api to get the address of the given co-ordinates