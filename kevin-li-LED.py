import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(True)
GPIO.setup(18,GPIO.OUT)
while True:
    print("LED on")
    GPIO.output(18,GPIO.HIGH)
    time.sleep(2)
    print("LED off")
    GPIO.output(18,GPIO.LOW)
    time.sleep(2)
