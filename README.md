# sentiment_report

### Overview

Once per day, script runs:

1. Downloads (scrapes?) news and financial data
	- News
	- Price Quotes  ✅
2. Quant. Financial data is analyzed mathematically (optional)
3. All data goes through LLM
4. LLM generates sentiment report
5. Send user a whatsapp message using twilio API w/ report  ✅


### Local Development Guide

1. Clone repo locally

```
git clone git@github.com:srblum/sentiment_report.git
cd sentiment_report
```

2. Create virtual environment (optional)

```
mkvirtualenv sentiment_report
```

3. Install python dependencies

```
pip install -r requirements.txt
```

4. Set up environment variables in `.env` file:

```
TWILIO_ACCOUNT_SID=<twilio_sid>
TWILIO_AUTH_TOKEN=<twilio_auth_token>
TEST_NUMBER='+12345678999'
```

5. Run program

```
python app.py
```
