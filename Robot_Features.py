import RPi.GPIO as GPIO
import time
from picamera import PiCamera
import os
from PIL import Image
import Feature_Helper as helper




def IR_DetectObstacle():
    GPIO.setmode(GPIO.BOARD)
    inPin = 3
    GPIO.setup(inPin, GPIO.IN)

    if (GPIO.input(inPin) == 1):
        print("No obstacle detected")
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

        for i in range (0, x):         
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



def US_GetDistance():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    TRIGGER = 16
    ECHO    = 18

    GPIO.setup(TRIGGER,GPIO.OUT) 
    GPIO.setup(ECHO,GPIO.IN)     

    GPIO.output(TRIGGER, False)
    time.sleep(1)

    distances = 0
    for i in range (0,3):
        GPIO.output(TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(TRIGGER, False)
        start = time.time()
      
        while GPIO.input(ECHO)==0:
          start = time.time()

        while GPIO.input(ECHO)==1:
          stop = time.time()

        elapsed = stop-start
        distance = (elapsed * 34300)/2

        distances = distances + distance

        time.sleep(0.1)

    distances = distances/3

    GPIO.cleanup()

    return round(distances,2)



def LED_RedOn():
    redPin = 33
    helper.colourOn(redPin)



def LED_RedOff():
    redPin = 33
    helper.colourOff(redPin)
    


def LED_RedFlash():
    redPin = 33
    helper.colourFlash(redPin)


def LED_BlueOn():
    bluePin = 35
    helper.colourOn(bluePin)



def LED_BlueOff():
    bluePin = 35
    helper.colourOff(bluePin)
    


def LED_BlueFlash():
    bluePin = 35
    helper.colourFlash(bluePin)


def LED_YellowOn():
    yellowPin = 37
    helper.colourOn(yellowPin)



def LED_YellowOff():
    yellowPin = 37
    helper.colourOff(yellowPin)
    


def LED_YellowFlash():
    yellowPin = 37
    helper.colourFlash(yellowPin)
    

    
