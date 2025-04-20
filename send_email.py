# Author: Yujin Nie
# Date: 20/4/25
# Description: A email-sending script

import smtplib
from email.message import EmailMessage

# Set the sender email and password and recipient email
from_email_addr="430004615@qq.com"
from_email_pass="gwqongkkwmnvbiaj"
to_email_addr="1343109389@qq.com"

# Create a message object
msg=EmailMessage()

# Set the email body
body="Hello from Raspberry Pi"
msg.set_content(body)

# Set sender and recipient
msg['From']=from_email_addr
msg['To']=to_email_addr

# Se+++t my email subject
msg['Subject']='TEST EMAIL'

# Conneccting to server and sending email
server=smtplib.SMTP('smtp.qq.com', 587)

server.starttls()
# Login to the SMTP server
server.login(from_email_addr, from_email_pass)

# Send the message
server.send_message(msg)

print('Email sent')

# Disconnect from the Server
server.quit()
