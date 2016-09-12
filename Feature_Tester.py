import Robot_Features as Features
import time


def main():
#    Features.IR_DetectObstacle()
#       
#    time.sleep(2)
#
#    Features.IR_WaitForObstacle()
#    
#    Features.CAM_TakePhoto("red", 180)    

#    Features.CAM_DetectColour("red1")
 #   Features.CAM_DetectColour("red2")
  #  Features.CAM_DetectColour("red3")
   # Features.CAM_DetectColour("green1")
    #Features.CAM_DetectColour("blue1")

    #Features.US_GetDistance()

#    temp = input("Enter 1 for on, 2 for off: ")

#    if temp == 1:
 #       Features.LED_RedOn()
#
 #   if temp == 2:
 #       Features.LED_RedOff()


    
    LED_Fun()
    

    #Features.clearPins()

    print("Done")

def LED_Fun():
    delay = 0.5
    for i in range (0,4):
        Features.LED_RedOn()
        time.sleep(delay)
        Features.LED_RedOff()
        Features.LED_BlueOn()
        time.sleep(delay)
        Features.LED_BlueOff()
        Features.LED_YellowOn()
        time.sleep(delay)
        Features.LED_YellowOff()
        delay = delay - 0.1

    Features.LED_RedOn()
    Features.LED_BlueOn()
    Features.LED_YellowOn()

    Features.LED_RedOff()
    Features.LED_BlueOff()
    Features.LED_YellowOff()

    Features.LED_RedOn()
    Features.LED_BlueOn()
    Features.LED_YellowOn()

    Features.LED_RedOff()
    Features.LED_BlueOff()
    Features.LED_YellowOff()

    Features.LED_RedOn()
    Features.LED_BlueOn()
    Features.LED_YellowOn()

    time.sleep(1.0)

    Features.LED_YellowOff()
    Features.LED_BlueOff()
    Features.LED_RedOff()

main()
