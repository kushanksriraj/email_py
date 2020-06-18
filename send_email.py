import smtplib
import json

with open('config.json') as f:
    data = json.load(f)

SENDER_EMAIL    = data["your_email"]
SENDER_PASSWORD = data["your_password"]

def send_email(receiver_email, subject, body):
    message = 'Subject: {}\n\n{}'.format(subject, body)
    i = 0
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        i = server.sendmail(SENDER_EMAIL, receiver_email, message)
    return i

if __name__ == '__main__':
    receiver_email = input('Enter the email id : ')
    subject        = input('Enter the subject : ')
    body           = input('Enter the body of email : ')

    send_email(receiver_email, subject, body)
