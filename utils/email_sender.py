"""Secure utility for sending emails via SMTP.

Refactored from the legacy script to remove hardcoded plain-text credentials
and utilize secure environment variables or runtime input prompts.
"""

import os
import smtplib
import getpass
from email.mime.text import MIMEText

def send_secure_email(
    to_email: str = None,
    from_email: str = None,
    subject: str = "Python SMTP Testing",
    body: str = "Hello, this is a secure email sent from Python."
):
    """Send an email using SMTP with secure authentication."""
    print("--- Secure Email Sender ---")
    
    # Resolve parameters from arguments or environment variables
    recipient = to_email or os.getenv("SMTP_RECIPIENT") or "recipient@example.com"
    sender = from_email or os.getenv("SMTP_SENDER") or "sender@example.com"
    
    msg = MIMEText(body)
    msg["To"] = recipient
    msg["From"] = sender
    msg["Subject"] = subject
    
    # Securely fetch password
    password = os.getenv("SMTP_PASSWORD")
    if not password:
        print(f"SMTP_PASSWORD environment variable not set. Caching session for {sender}...")
        try:
            password = getpass.getpass(prompt=f"Enter SMTP password for {sender}: ")
        except Exception:
            print("Non-interactive terminal detected. Skipping email delivery simulation.")
            return

    try:
        # Establish secure connection
        print("Connecting to SMTP server (smtp.gmail.com:587)...")
        smtp = smtplib.SMTP(host="smtp.gmail.com", port=587)
        smtp.starttls()
        smtp.login(user=sender, password=password)
        smtp.send_message(msg)
        smtp.quit()
        print(f"Email successfully sent to {recipient}!")
    except Exception as e:
        print("Failed to send email. Error:", e)

if __name__ == "__main__":
    send_secure_email()
