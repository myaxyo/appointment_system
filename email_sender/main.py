import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
from pathlib import Path

current_dir = Path(__file__).resolve().parent
env_path = current_dir.parent / ".private.env"
load_dotenv(env_path)


def email_sender(recepient: str, subject: str, body: str) -> None:
    try:
        smtp_server = "smtp.gmail.com"
        port = 587
        sender_email = os.getenv("EMAIL")
        password = os.getenv("PASSWORD")

        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, password)
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recepient
        message["Subject"] = subject
        message.attach(MIMEText(body, "html"))
        server.send_message(message)
        server.quit()
    except Exception as e:
        print(e)
