from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC96ca32e0fa8f265fd9edc72f53e7c7e2"
# Your Auth Token from twilio.com/console
auth_token  = "379374d5e57614a985acfde2f2823842"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+972549747361", 
    from_="+17162295289",
    body="Hello from Python!")

print(message.sid)