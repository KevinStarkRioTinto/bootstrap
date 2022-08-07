from machine import Pin
from utime import sleep_us,ticks_us, sleep

echo=Pin(17,Pin.IN)  
trig=Pin(16,Pin.OUT)  

led = Pin(25, Pin.OUT)
led.low()

trig.value(0)  
sleep_us(2)  

while True:
    led.high()
    try:  
        trig.high()  
        sleep_us(10)  
        trig.low()  
        while echo.value()==False:  
            st=ticks_us()  
        while echo.value()==True:  
            sto=ticks_us()  
        tt=sto-st  
        dis=(0.031594*tt)/2  
        print(dis)  
    except KeyboardInterrupt:  
        break  
    sleep(1)
    led.low()
    sleep(1)
    