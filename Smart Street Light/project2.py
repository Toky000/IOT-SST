import RPi.GPIO as GPIO
import time

LED1 = 11
IR1 = 12

LED2 = 13
IR2 = 15

LED3 = 18
IR3 = 22

GPIO.setmode(GPIO.BOARD)
GPIO.setup(IR1,GPIO.IN)
GPIO.setup(LED1,GPIO.OUT)

GPIO.setup(IR2,GPIO.IN)
GPIO.setup(LED2,GPIO.OUT)

GPIO.setup(IR3,GPIO.IN)
GPIO.setup(LED3,GPIO.OUT)
try:
    while(True):
            input_state1 = GPIO.input(IR1)
            if input_state1 == True:
                GPIO.output(LED1,False)
                time.sleep(2)
            else:
                GPIO.output(LED1,True)
                #time.sleep(0.8)
     
            input_state2 = GPIO.input(IR2)
            if input_state2 == True:
                GPIO.output(LED2,False)
                time.sleep(2)
            else:
                GPIO.output(LED2,True)
##                time.sleep(0.5)
                
            input_state3 = GPIO.input(IR3)
            if input_state3 == True:
                GPIO.output(LED3,False)
                time.sleep(2)
            else:
                GPIO.output(LED3,True)
##                time.sleep(0.5)   
##            
        
except KeyboardInterrupt:
    GPIO.output(LED,True)
   