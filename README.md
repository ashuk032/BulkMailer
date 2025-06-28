# BulkMailer 📬

Send the same email to a list of recipients using Python and Gmail SMTP.

## Features
- Uses secure SMTP over SSL
- Loads credentials from `.env` file
- Reads recipients from `recipients.txt`
- **Sends beautiful, modern HTML emails using `mail_template.py`**

## Setup

### 1. Clone repo & install dependencies
```bash
pip install -r requirements.txt
```
Or, if you only need the HTML mailer:
```bash
pip install python-dotenv
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

## Sending Beautiful HTML Emails

To send a modern, responsive HTML email to all recipients, use the `mail_template.py` script:

```bash
python mail_template.py
```

- Loads recipients from `recipients.txt`
- Sends a beautifully styled HTML email (with a plain text fallback) to each address
- Logs the sending status for each recipient

## Customization

- **Edit the HTML template** in `mail_template.py` inside the `get_html_template()` function.
- **Change the subject** or plain text fallback in the `main()` function.

## Example Email

The default template includes:
- Gradient header
- Animated rocket emoji
- Highlighted features section
- Social links and signature

---

© 2024 Ashish. All rights reserved.
3. **Create a `.env` file** in the project directory with your email credentials:
   ```
   EMAIL_ADDRESS=your_email@gmail.com
   EMAIL_PASSWORD=your_app_password
   ```

   > **Note:** For Gmail, you may need to use an [App Password](https://support.google.com/accounts/answer/185833) if 2FA is enabled.

4. **Create a `recipients.txt` file** with one email address per line.

## Usage

Run the script to send the HTML email to all recipients:
```
python mail_template.py
```

The script will:
- Load recipients from `recipients.txt`
- Send a beautifully styled HTML email (with a plain text fallback) to each address
- Log the sending status for each recipient

## Customization

- **Edit the HTML template** in `mail_template.py` inside the `get_html_template()` function.
- **Change the subject** or plain text fallback in the `main()` function.

## Example Email

The default template includes:
- Gradient header
- Animated rocket emoji
- Highlighted features section
- Social links and signature

---

© 2024 Ashish. All rights reserved.
