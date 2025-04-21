# Use comments
# Program Title: Project#2 Agile Raspberry Pi Plant Moisture Sensor with Email Notification
# Program Description: Use moisture and Raspberry Pi to send an email notification when plant needs watering.
# Name: Yujin Nie
# Student ID: 202283890022
# COURSE & Year: Project Semester 3 2025
# Date: 22/4/25

# Used libraries
import RPi.GPIO as GPIO
import time
import smtplib
from email.message import EmailMessage
import datetime

# Global counter 
counter=0

#GPIO SETUP
channel=4

#monitor the soil moisture
def monitor():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(channel, GPIO.IN)
    # get sensor's status
    soil_moisture=GPIO.input(channel)
    # sensor potential 1: Dry
    if GPIO.input(channel):
        print("No Water Detected!")
    # sensor potential 0: Moist
    else:
        print("Water Detected!")
    # clean up GPIO after every monitoring
    GPIO.cleanup()
    return soil_moisture

# Set the sender email and password and recipient email
from_email_addr="430004615@qq.com"
from_email_pass="gwqongkkwmnvbiaj"
to_email_addr="1343109389@qq.com"

# Send email if need water or not need 
def send_email(monitor_data,monitorTime,count):
    # Create a message object
    msg=EmailMessage()

    # Set the email body
    if monitor_data:
        body=f"Monitoring time: {monitorTime}. The {count} monitor: Please water your plant"
    else:
        body=f"Monitoring time: {monitorTime}. The {count} monitor: Water NOT needed"
    msg.set_content(body)

    # write the monitoring statu to a txt file
    with open("record_monitor", "a")as f:
        f.write(f"{body}")

    # Set sender and recipient
    msg['From']=from_email_addr
    msg['To']=to_email_addr

    # Set my email subject
    msg['Subject']='Agile Raspberry Pi Plant Moisture Sensor with Email Notification'

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

# get date and time of monitoring
def monitor_time():
    currentTime=datetime.datetime.now()
    return currentTime.strftime("%d/%m/%y %H:%M:%S")

# run every 3 hours
while True:
    counter+=1 # Add 1 per cycle

    now=monitor_time() # get current time

    soil_moisture=monitor() # get the soil moisture
    send_email(soil_moisture,now,counter) # send email

    time.sleep(3*3600) # sleep for 3 hours
