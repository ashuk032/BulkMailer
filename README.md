# BulkMailer 📬

Send the same email to a list of recipients using Python and Gmail SMTP.

## Features
- Uses secure SMTP over SSL
- Loads credentials from `.env` file
- Reads recipients from `recipients.txt`

## Setup

### 1. Clone repo & install dependencies
```bash
pip install -r requirements.txt
```

### 2. Setup your `.env` file
```env
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password_here
```

💡 Tip: Use [App Passwords](https://myaccount.google.com/apppasswords) if you have 2FA enabled on Gmail.

### 3. Add recipient emails to `recipients.txt`
```txt
email1@example.com
email2@example.com
```

### 4. Run the script
```bash
python main.py
```

## Note
- Use responsibly. Avoid spamming.
- Gmail may limit or block excessive SMTP use.
