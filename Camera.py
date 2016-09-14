from picamera import PiCamera
from PIL import Image
import time
import os

class Camera:

    def __init__(self):
        self.__sleepTime = 2
        self.__filePath = '/home/pi/RASPIED/Camera_Images/'


    def take_photo(self, fileName):
        #Where to save the image to on the raspberry pi
        path = self.__filePath + str(fileName)+ '.jpg'

        #Checks if the file already exists, deletes it if it does
        if os.path.isfile(path) == True:
            os.remove(path)

        
        camera = PiCamera()
        camera.resolution = (300, 300)  #No need for high resolution images, 300x300 will do
        camera.start_preview()  #Open camera shutters
        time.sleep(self.__sleepTime)   #Give camera time to focus
        camera.capture(path)    #Take the photo
        camera.stop_preview()   #Close shutters
        print("Photo taken")    


    def detect_colour(self, fileName):
        path = self.__filePath + str(fileName)+ '.jpg'

        #Checking if file exists
        if os.path.isfile(path) == False:
            print("Error: file '" + fileName + "' not found!")

        else:
            im = Image.open(path)
            pixels = im.load()  #Loading in a 2D array of all pixel RGB values
            x = im.size[0]      
            y = im.size[1]      
            totalPixels = x*y   
            
            avgR = 0
            avgG = 0
            avgB = 0

            #Calculate the average red, green, and blue channel values for the image
            #This would be really inefficient, but is fine for images with resolutions as small as 300x300
            for i in range (0, x):         
                for j in range (0, y):
                    avgR = avgR + pixels[i, j][0]
                    avgG = avgG + pixels[i, j][1]
                    avgB = avgB + pixels[i, j][2]
                    
            avgR = avgR / totalPixels
            avgG = avgG / totalPixels
            avgB = avgB / totalPixels

            
            if (avgR > avgB and avgR > avgG):   #If image is mostly red, classify as red
                return "red"

            elif (avgG > avgR and avgG > avgB):   #If image is mostly green, classify as green
                return "green"

            elif (avgB > avgR and avgB > avgG):   #If image is mostly blue, classify as blue
                return "blue"

            else:
                return "unknown"

            #Maybe not the most accurate colour predictions, but should get the job done
            #Should give fairly reliable predictions in uncertain lighting conditions
            #Will update if incorrect predictions occur frequently
