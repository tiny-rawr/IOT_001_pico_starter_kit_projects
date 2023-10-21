from machine import Pin
import time

led = Pin("LED", Pin.OUT)

try:
    while True:
        led.value(1) # Turn On
        time.sleep(0.5)
        led.value(0) # Turn Off
        time.sleep(0.5)
except:
    pass