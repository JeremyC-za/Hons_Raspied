import RPi.GPIO as GPIO
import time



def IR_DetectObstacle():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(3, GPIO.IN)

    if (GPIO.input(3) == 1):
        print("No obstacles detected")
        return False

    else:
        print("Obstacle detected!")
        return True

    GPIO.cleanup()


def IR_WaitForObstacle():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(3, GPIO.IN)

    while (True):
        if (GPIO.input(3) == 0):
            print("Obstacle detected!")
            break
        
        time.sleep(0.05)
    
    GPIO.cleanup()
    

    
