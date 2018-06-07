#from twilio.rest import Client
from twilio import rest #./twilio/rest


# Your Account SID from twilio.com/console
account_sid = "XXXXXXXXXXXXXXXXXXXXXXXXXXX"
# Your Auth Token from twilio.com/console
auth_token  = "XXXXXXXXXXXXXXXXXXXXXXXXXXX"

client = rest.Client(account_sid, auth_token)

message = client.messages.create(
    to="+XXXXXXXXXXXX",     #Number to send
    from_="+XXXXXXXXXXXX",  #Your Twilio number
    body="Hello from Python!")

print(message.sid)
