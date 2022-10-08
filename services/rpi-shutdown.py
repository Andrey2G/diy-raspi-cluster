# !/bin/python
import RPi.GPIO as GPIO
import time
import os

# define pin
shutdown_pin = 21

# Suppress warnings
GPIO.setwarnings(False)
# Use the Broadcom SOC Pin numbering
GPIO.setmode(GPIO.BCM)

# Setup the pin with internal pullups enabled and pin in reading mode.
# we are using a momentary push button without a resistor.
GPIO.setup(shutdown_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def Shutdown(channel):
    print("Shutting Down")
    #waiting 3 seconds to make sure you are definitely want to Shutdown
    time.sleep(3)
    os.system("sudo shutdown -h now")

GPIO.add_event_detect(shutdown_pin, GPIO.FALLING, callback=Shutdown, bouncetime=2000)

# LOOP :)
while 1:
    time.sleep(0.5)