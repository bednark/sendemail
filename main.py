import smtplib, ssl
from getpass import getpass
from email.message import EmailMessage

SENDER = 'sender@example.com'
RECEIVER = 'receiver@example.com'
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
passwd = getpass("Input your password: ")

mail_msg = EmailMessage()
mail_msg["From"] = SENDER
mail_msg["To"] = RECEIVER
mail_msg["Subject"] = "Python test email message"
mail_msg.set_content("Python test email message")

context = ssl.create_default_context()

srv = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
srv.ehlo()
srv.starttls(context=context)
srv.ehlo()
srv.login(SENDER, passwd)
srv.send_message(mail_msg)
srv.quit()

print("Success!")