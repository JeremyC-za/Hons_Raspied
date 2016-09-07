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

    Features.CAM_DetectColour("red1")
    Features.CAM_DetectColour("red2")
    Features.CAM_DetectColour("red3")
    Features.CAM_DetectColour("green1")
    Features.CAM_DetectColour("blue1")

    

main()
