import socket
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def check_connection(host, port, timeout=8):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            print(f"Successfully connected to {host}:{port}")
        return True
    except (OSError, socket.timeout) as e:
        print(f"Failed to connect to {host}:{port} - {e}")
        return False

def send_email():
    from_email = "your_email@gmail.com"
    to_email = "recipient_email@gmail.com"
    subject = "Connection Alert"
    message = "Unable to connect to 196.201.213.89 on port 6691"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, "your_password")
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

while True:
    if not check_connection("196.201.213.89", 6691):
        send_email()
    time.sleep(180)  # Sleep for 3 minutes
