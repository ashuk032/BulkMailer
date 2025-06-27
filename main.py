import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from typing import List
import logging

# Load environment variables from .env
load_dotenv()

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 465


def load_recipients(file_path: str) -> List[str]:
    """Load recipient email addresses from a file."""
    if not os.path.exists(file_path):
        logging.error(f"Recipients file not found: {file_path}")
        return []

    with open(file_path, 'r') as file:
        recipients = [line.strip() for line in file if line.strip()]
    logging.info(f"Loaded {len(recipients)} recipient(s).")
    return recipients


def build_email(to_address: str, subject: str, body: str) -> MIMEMultipart:
    """Build the MIME email object."""
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    return msg


def send_email(recipient: str, message: MIMEMultipart) -> bool:
    """Send an email to a single recipient."""
    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(message)
        logging.info(f"Email sent to {recipient}")
        return True
    except Exception as e:
        logging.error(f"Failed to send email to {recipient} - {str(e)}")
        return False


def main():
    subject = "Hello from Ashish 🚀"
    body = """Hi there,

This is a test email sent using Python and SMTP.
Stay awesome!

- Ashish
"""

    recipients = load_recipients('recipients.txt')
    if not recipients:
        logging.warning("No recipients found. Exiting.")
        return

    for recipient in recipients:
        email_message = build_email(recipient, subject, body)
        send_email(recipient, email_message)


if __name__ == "__main__":
    main()
