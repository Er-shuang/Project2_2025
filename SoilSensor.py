#Author: Yujin Nie
#Data: 16/4/25
#Description: Create a test Python Script
#!/usr/bin/python
import RPi.GPIO as GPIO
import time

#GPIO SETUP
channel=4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
    if GPIO.input(channel):
        print("No Water Detected!")
    else:
        print("Water Detected!")

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300) # let us know when the pin gose HIGH or LOW
GPIO.add_event_callback(channel, callback) # assign function to GPIO PIN, Run function on change

# infinite loop
while True:
    time.sleep(0)
