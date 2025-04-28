import os
import time
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
test_number = os.environ["TEST_NUMBER"]
client = Client(account_sid, auth_token)

# send test message to Sean
message = client.messages.create(
  from_='whatsapp:+14155238886',
  body="the market is terrible today! switch to bonds!",
  to=f"whatsapp:{test_number}"
)
print(message.status)
print(message.error_code)
print(message.sid)

# wait 2 seconds and then check message status
time.sleep(2)
updated_message = client.messages(message.sid).fetch()
print(updated_message.status)
print(updated_message.error_code)
print(updated_message.sid)
