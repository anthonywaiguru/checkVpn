import socket
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Try to connect to the actual host and port, simillar to a telnet to Ip and Port.

def check_connection(host, port, timeout=10):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            print(f"Successfully connected to {host}:{port}")
        return True
    except (OSError, socket.timeout) as e:
        print(f"Failed to connect to {host}:{port} - {e}")
        return False


# Email Credentials (Improve this by using a Secure App Password) instead of YOURPASSWORD
# Change the email addresses below to actual emails.
def send_email():
    from_email = "tech@gmail.com"
    to_emails = ["italerts@roamtech.com", "techops@gmail.com"]  # Insert email addresses into an array
    subject = "Safaricom VPN Alert"
    message = "Please check your connection to 196.201.213.89 Port 6691"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)  # Join the list into a string for the 'To' header
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, "YOURPASSWORD")
    server.sendmail(from_email, to_emails, msg.as_string())  # Use the list here
    server.quit()

while True:
    if not check_connection("196.201.213.89", 6691):
        send_email()
    time.sleep(180)  # Sleep for 3 minutes, instead of a Cronjob, loop every 180 seconds.

