import requests
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
from twilio.rest import Client

# Email Configuration
sender_address = 'your_email@gmail.com'
sender_pass = 'your_email_password'
receiver_addresses = [
    "recipient1@gmail.com",
    "recipient2@gmail.com",
    "recipient3@gmail.com"
]

# Discord Configuration
discord_webhook_url = 'https://discord.com/api/v9/channels/YOUR_CHANNEL_ID/messages'
discord_headers = {'authorization': 'YOUR_DISCORD_AUTH_TOKEN'}

# Twilio Configuration
twilio_account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
twilio_auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
twilio_from_number = '+1234567890'
twilio_to_number = '+0987654321'

# Other Configuration
wait_time = 1 * 60
last_announcement = "binance will list tranchess (chess) in the innovation zone"

def send_mail(mail_subject, mail_content):
    global receiver_addresses, sender_address, sender_pass
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = ', '.join(receiver_addresses)
    message['Subject'] = mail_subject
    message.attach(MIMEText(mail_content, 'plain'))

    with smtplib.SMTP('smtp.gmail.com', 587) as session:
        session.starttls()
        session.login(sender_address, sender_pass)
        text = message.as_string()
        session.sendmail(sender_address, receiver_addresses, text)

def discord_send(content):
    requests.post(discord_webhook_url, data={'content': content}, headers=discord_headers)

def make_call():
    client = Client(twilio_account_sid, twilio_auth_token)
    call = client.calls.create(to=twilio_to_number, from_=twilio_from_number, url="https://demo.twilio.com/docs/voice.xml")
    print(f"[!] Call placed {call.sid}")

# Main Loop
running_since = 0
while True:
    try:
        response = requests.get("https://www.binance.com/bapi/composite/v1/public/cms/article/catalog/list/query?catalogId=48&pageNo=1&pageSize=15&rnd=" + str(time.time()))
        latest_announcement = response.json()
        
        if response.status_code != 200:
            print(f"[-] Invalid Status Code {response.status_code}")
            discord_send(f"Binance Listing Bot Invalid Status Code\nStatus Code = {response.status_code}")

        articles = [article['title'].lower() for article in latest_announcement['data']['articles']]
        new_articles = [article for article in articles if article != last_announcement]
        
        if not new_articles:
            print("[-] Last Announcement Not Found")
            discord_send("Binance Listing Bot Last Announcement Not Found.")
        
        new_listings = [article.title() for article in new_articles if 'will list' in article]
        
        if new_listings:
            print(f"[+] Found new listings {time.time()}")
            make_call()
            listing_alert = "\n".join(new_listings)
            discord_send(f"Binance New Listing Alert: {listing_alert}")
        else:
            print(f"[-] Found no new listings {time.time()}")
    except Exception as err:
        print(f"[-] Error: {err}")
        discord_send(f"Binance Listing Bot Error: {err}")
    
    if running_since % 1440 == 0:
        discord_send("Binance Listing Bot Running: No New Listings Found")
    
    running_since += 1
    time.sleep(wait_time)
