# gmail_service.py

import os
import smtplib

from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()


def send_salary_email(employee):

    sender_email = os.getenv("GMAIL_USER")
    app_password = os.getenv("GMAIL_APP_PASSWORD")

    receiver_email = employee["email"]

    if not sender_email or not app_password:
        print("Gmail configuration is missing.")
        return False

    if receiver_email.endswith("@example.com"):
        print("Replace the sample employee email.")
        return False

    message = EmailMessage()

    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Monthly Salary Notification"

    body = f"""
Dear {employee['name']},

Greetings from AI Company HR Department.

Your monthly salary has been approved.

Employee Name: {employee['name']}
Salary Amount: Rs. {employee['salary']}

This is an automated salary notification
from the HR Department.

Regards,
HR Department
AI Company
"""

    message.set_content(body)

    try:

        with smtplib.SMTP_SSL(
            "smtp.gmail.com", 465, timeout=30
        ) as server:

            server.login(sender_email, app_password)

            server.send_message(message)

        print("Email sent to", employee["name"])

        return True

    except Exception as error:

        print("Email sending failed:", error)

        return False