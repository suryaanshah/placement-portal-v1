import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email_validator import validate_email, EmailNotValidError
from app.config import SECRET_KEY

def send_reset_email(to_email: str, reset_link: str):
    try:
        # Validate email
        validate_email(to_email)
    except EmailNotValidError:
        raise ValueError(f"Invalid email address: {to_email}")

    # Email server details
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "your-email@example.com"
    smtp_password = "your-email-password"

    # Compose email
    subject = "Password Reset Request"
    body = f"Click the following link to reset your password: {reset_link}"

    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Send email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, to_email, msg.as_string())

