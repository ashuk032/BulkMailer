import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

# Email content
subject = "Hello from Ashish 🚀"
body = """Hi there,

This is a test email sent using Python and SMTP.
Stay awesome!

- Ashish
"""

# Read recipient emails from file
with open("recipients.txt", "r") as file:
    recipients = [line.strip() for line in file.readlines() if line.strip()]

# Create message
for recipient in recipients:
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = recipient
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, recipient, msg.as_string())
        print(f"Sent to {recipient} ✅")
    except Exception as e:
        print(f"Failed to send to {recipient} ❌\nReason: {e}")
