import RPi.GPIO as GPIO
import time
from picamera import PiCamera
import os
from PIL import Image


def IR_DetectObstacle():
    GPIO.setmode(GPIO.BOARD)
    inPin = 3
    GPIO.setup(inPin, GPIO.IN)

    if (GPIO.input(inPin) == 1):
        print("No obstacles detected")
        return False

    else:
        print("Obstacle detected!")
        return True

    GPIO.cleanup()
    


def IR_WaitForObstacle():
    GPIO.setmode(GPIO.BOARD)
    inPin = 3
    GPIO.setup(inPin, GPIO.IN)

    while (True):
        if (GPIO.input(inPin) == 0):
            print("Obstacle detected!")
            break
        
        time.sleep(0.05)
    
    GPIO.cleanup()

    
    
def CAM_TakePhoto(fileName, rotation = 0, sleepTime = 2):
    filePath = ('/home/pi/RASPIED/Camera_Images/' + str(fileName)+ '.jpg')
    
    if os.path.isfile(filePath) == True:
        os.remove(filePath)
        
    camera = PiCamera()
    camera.resolution = (300, 300)
    camera.rotation = rotation
    camera.start_preview()
    time.sleep(sleepTime)
    camera.capture(filePath)
    camera.stop_preview()
    print("Photo taken")

    return filePath
    

def CAM_DetectColour(fileName):
    filePath = ('/home/pi/RASPIED/Camera_Images/' + str(fileName)+ '.jpg')

    if os.path.isfile(filePath) == False:
        print("Error - file '" + fileName + "' not found!")

    else:
        im = Image.open(filePath)
        pixels = im.load()
        x = im.size[0]
        y = im.size[1]
        totalPixels = x*y

        avgR = 0
        avgG = 0
        avgB = 0

        for i in range (0, x):          # maybe optimise to look at 100-1000 random pixels, rather than all of them
            for j in range (0, y):
                avgR = avgR + pixels[i, j][0]
                avgG = avgG + pixels[i, j][1]
                avgB = avgB + pixels[i, j][2]
                
        avgR = avgR / totalPixels
        avgG = avgG / totalPixels
        avgB = avgB / totalPixels
        
        if (avgR >= 200 and ((avgG + avgB)/2) < 160):
            print("Image '" + fileName + "' colour is red!")
            return "red"

        if (avgG >= 200 and ((avgR + avgB)/2) < 160):
            print("Image '" + fileName + "' colour is green!")
            return "green"

        if (avgB >= 200 and ((avgR + avgG)/2) < 160):
            print("Image '" + fileName + "' colour is blue!")
            return "blue"















    
