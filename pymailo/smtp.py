import smtplib
from dotenv import load_dotenv
import os

load_dotenv()
HOST = os.getenv('SMTP_HOST')
PORT = os.getenv('SMTP_PORT')
EMAIL = os.getenv('SMTP_EMAIL')
PASSWORD = os.getenv('SMTP_PASSWORD')

def send(recipient,subject,body):
    TO = recipient
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = "\r\n".join([
        f"From: No-Reply <{EMAIL}>",
        f"To: {TO}",
        f"Subject: {SUBJECT}",
        f"",
        f"{TEXT}"
    ])

    # send
    try:
        server = smtplib.SMTP(HOST, PORT)
        server.ehlo()
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, TO, message)
        server.close()
        print('Successfully sent the mail')
    except Exception as e:
        print(f"Failed to send mail with message: {e}")