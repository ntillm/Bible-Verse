import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Im on a whole nother level im geekin.",
    from_="+18666440718",
    to="+18777804236"
)

print(message.body)