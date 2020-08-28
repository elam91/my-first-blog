from twilio.rest import Client
import cgi
import os

form = cgi.FieldStorage()
message = form.getvalue('message') + "From" + form.getvalue('fname')
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+972549747361", 
    from_="+17162295289",
    body= message

print(message.sid)