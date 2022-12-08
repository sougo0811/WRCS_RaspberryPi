import RPi.GPIO as GPIO
from time import sleep

RELAY_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(RELAY_PIN, GPIO.OUT)

def pump():
  GPIO.output(RELAY_PIN, True)
  sleep(2.00)
  GPIO.output(RELAY_PIN, False)