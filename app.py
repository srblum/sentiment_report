import os
import requests
import time
from pprint import pprint
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
alpha_vantage_api_key = os.environ["ALPHA_VANTAGE_API_KEY"]
test_number = os.environ["TEST_NUMBER"]
client = Client(account_sid, auth_token)

# alpha vantage
SYMBOL = "PLTR"
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={SYMBOL}&interval=5min&apikey={alpha_vantage_api_key}'
response = requests.get(url)
data = response.json()
price_items = sorted(data["Time Series (5min)"].items(), key=lambda x: x[0])
start_item = price_items[0]
end_item = price_items[-1]
start_price = float(start_item[1]["1. open"])
end_price = float(end_item[1]["4. close"])
direction = "up" if (end_price - start_price) > 0 else "down"
message = f"Palantir is {direction} today! It started at {start_price} and ended at {end_price}."

# send test message to test number
message = client.messages.create(
  from_='whatsapp:+14155238886',
  body=message,
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