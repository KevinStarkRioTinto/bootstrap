from machine import Pin
import time

pin = Pin("WL_GPIO0", Pin.OUT)

while True:
    pin.toggle()
    time.sleep_ms(1000)
    print("ping")

