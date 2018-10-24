#http://pi4j.com/pins/model-3b-rev1.html
#

from gpiozero import LED
from time import sleep

led = LED(17)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)