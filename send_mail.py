import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "xxxxxxxxx@gmail.com"  # Enter your address
receiver_email = "xxxxxxx@gmail.com"  # Enter receiver address
password = "XxXxXx/*-8"
message = """\
Subject: Urgent! You're being hacked

Someone is jamming your car! Hurry up or you'll lose it. ;-)"""

def send_message():
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
           server.login(sender_email, password)
           server.sendmail(sender_email, receiver_email, message)

#send_message()
