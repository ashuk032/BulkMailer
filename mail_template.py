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


def get_html_template() -> str:
    """Return the HTML email template."""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Email from Ashish</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                line-height: 1.6;
                margin: 0;
                padding: 0;
                background-color: #f5f7fa;
            }
            .container {
                max-width: 600px;
                margin: 20px auto;
                background: white;
                border-radius: 12px;
                overflow: hidden;
                box-shadow: 0 4px 25px rgba(0,0,0,0.1);
            }
            .header {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                padding: 40px 30px;
                text-align: center;
            }
            .header h1 {
                margin: 0;
                font-size: 32px;
                font-weight: 300;
                letter-spacing: 1px;
            }
            .rocket {
                font-size: 50px;
                margin-bottom: 15px;
                display: block;
                animation: bounce 2s infinite;
            }
            @keyframes bounce {
                0%, 20%, 50%, 80%, 100% {
                    transform: translateY(0);
                }
                40% {
                    transform: translateY(-10px);
                }
                60% {
                    transform: translateY(-5px);
                }
            }
            .content {
                padding: 50px 40px;
            }
            .greeting {
                font-size: 20px;
                color: #2c3e50;
                margin-bottom: 25px;
                font-weight: 600;
            }
            .message {
                font-size: 16px;
                color: #555;
                margin-bottom: 35px;
                line-height: 1.8;
                text-align: justify;
            }
            .highlight {
                background: linear-gradient(120deg, #a8edea 0%, #fed6e3 100%);
                padding: 20px;
                border-radius: 8px;
                margin: 25px 0;
                border-left: 4px solid #667eea;
            }
            .signature {
                border-top: 2px solid #e9ecef;
                padding-top: 25px;
                font-style: italic;
                color: #6c757d;
                font-size: 16px;
            }
            .footer {
                background: #f8f9fa;
                padding: 25px;
                text-align: center;
                color: #6c757d;
                font-size: 14px;
            }
            .social-links {
                margin-top: 15px;
            }
            .social-links a {
                color: #667eea;
                text-decoration: none;
                margin: 0 10px;
                font-weight: 500;
            }
            .badge {
                display: inline-block;
                background: #28a745;
                color: white;
                padding: 5px 12px;
                border-radius: 15px;
                font-size: 12px;
                font-weight: bold;
                margin-left: 10px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <span class="rocket">🚀</span>
                <h1>Hello from Ashish!</h1>
            </div>
            
            <div class="content">
                <div class="greeting">
                    Hi there! 👋
                    <span class="badge">TEST EMAIL</span>
                </div>
                
                <div class="message">
                    This is a <strong>beautifully crafted HTML email</strong> sent using Python and SMTP. 
                    I've enhanced the original template with modern styling and animations to make 
                    your emails stand out in the inbox!
                </div>
                
                <div class="highlight">
                    <strong>✨ Features of this template:</strong><br>
                    • Responsive design that works on all devices<br>
                    • Modern gradient backgrounds<br>
                    • Smooth animations and hover effects<br>
                    • Professional typography and spacing
                </div>
                
                <div class="message">
                    I hope this email finds you well and that you're having an amazing day! 
                    Feel free to customize this template for your own projects.
                    <br><br>
                    <strong>Keep coding and stay awesome!</strong> 💻✨
                </div>
                
                <div class="signature">
                    Best regards,<br>
                    <strong>- Ashish</strong> 👨‍💻
                </div>
            </div>
            
            <div class="footer">
                <div>Sent with ❤️ using Python & SMTP</div>
                <div class="social-links">
                    <a href="#">LinkedIn</a> | 
                    <a href="#">GitHub</a> | 
                    <a href="#">Portfolio</a>
                </div>
                <div style="margin-top: 10px; font-size: 12px;">
                    © 2024 Ashish. All rights reserved.
                </div>
            </div>
        </div>
    </body>
    </html>
    """


def build_email(to_address: str, subject: str, html_body: str, text_body: str = None) -> MIMEMultipart:
    """Build the MIME email object with HTML content."""
    msg = MIMEMultipart('alternative')
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_address
    msg['Subject'] = subject
    
    # Create plain text version as fallback
    if text_body is None:
        text_body = """Hi there,

This is a test email sent using Python and SMTP.
Stay awesome!

- Ashish
"""
    
    # Attach both plain text and HTML versions
    text_part = MIMEText(text_body, 'plain')
    html_part = MIMEText(html_body, 'html')
    
    msg.attach(text_part)
    msg.attach(html_part)
    
    return msg


def send_email(recipient: str, message: MIMEMultipart) -> bool:
    """Send an email to a single recipient."""
    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(message)
        logging.info(f"HTML email sent successfully to {recipient}")
        return True
    except Exception as e:
        logging.error(f"Failed to send email to {recipient} - {str(e)}")
        return False


def main():
    subject = "Hello from Ashish 🚀"
    
    # Get the HTML template
    html_body = get_html_template()
    
    # Plain text fallback
    text_body = """Hi there,

This is a test email sent using Python and SMTP with HTML template.
Stay awesome!

- Ashish
"""

    recipients = load_recipients('recipients.txt')
    if not recipients:
        logging.warning("No recipients found. Exiting.")
        return

    logging.info(f"Starting to send HTML emails to {len(recipients)} recipient(s)...")
    
    success_count = 0
    for recipient in recipients:
        email_message = build_email(recipient, subject, html_body, text_body)
        if send_email(recipient, email_message):
            success_count += 1
    
    logging.info(f"Email sending completed. {success_count}/{len(recipients)} emails sent successfully.")


if __name__ == "__main__":
    main()