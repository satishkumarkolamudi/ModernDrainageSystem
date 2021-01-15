import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
TRIG=4
ECHO=18
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIG,True)
time.sleep(0.001)
GPIO.output(TRIG,False)

while GPIO.input(ECHO)==False:
    start=time.time()

while GPIO.input(ECHO)==True:
    end=time.time()
sig_time=end-start
distance=sig_time/0.000058
print('Distance: {} cm'.format(distance))

if distance>=5:
    print('SAFE')
elif 5>distance>3:
    print('SAFE LINE CROSED')
elif  distance<=3:
    print('DANGER')

GPIO.cleanup()
