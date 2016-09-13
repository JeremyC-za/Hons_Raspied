import RPi.GPIO as GPIO
import time
from picamera import PiCamera
import os
from PIL import Image


def clearPins():
    GPIO.cleanup()



def colourOn(pinNumber):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    colourPin = pinNumber
    GPIO.setup(colourPin, GPIO.OUT)

    GPIO.output(colourPin, True)
    time.sleep(0.11)


def colourOff(pinNumber):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    colourPin = pinNumber
    GPIO.setup(colourPin, GPIO.OUT)

    GPIO.output(colourPin, False)
    time.sleep(0.11)

def colourFlash(pinNumber):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    colourPin = pinNumber
    GPIO.setup(pinNumber, GPIO.OUT)

    GPIO.output(pinNumber, True)

    time.sleep(1)

    GPIO.output(pinNumber, False)

