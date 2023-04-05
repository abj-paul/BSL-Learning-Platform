import smtplib
from email.mime.text import MIMEText

def send_mail(content, to):
    message = MIMEText(content)
    message['Subject'] = "Test email"
    message['From'] = "dev-acc-2@outlook.com"
    message['To'] = to 

    # Send message
    with smtplib.SMTP('smtp-mail.outlook.com', 587) as smtp:
        smtp.starttls()
        smtp.login('dev-acc-2@outlook.com', 'pbvt4Yta48agDiB')
        smtp.send_message(message)
        