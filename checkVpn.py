import socket
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Try to connect to the actual host and port, simillar to a telnet to Ip and Port
def check_connection(host, port):
    try:
        socket.create_connection((host, port))
        return True
    except OSError:
        return False

# Email Credentials (Improve this by using a Secure App Password)
def send_email():
    from_email = "tech-admin@roamtech.com"
    to_email = "anthony.waiguru@roamtech.com"
    subject = "VPN Connection Alert"
    message = "Unable to connect to 196.201.213.89 on port 6691"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, "tech-admin2022!")
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

while True:
    if not check_connection("196.201.213.89", 6691):
        send_email()
    time.sleep(180)  # Sleep for 3 minutes, instead of a Cronjob, loop every 180 seconds.

