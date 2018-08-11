import RPi.GPIO as GPIO
import time

class myUltrasonic(object):


    def __init__(self,TRIG,ECHO):
        self.trig = TRIG
        self.echo = ECHO



    def medir(self):
        GPIO.setmode(GPIO.BCM)
        print ("Distance Measurement In Progress")
        GPIO.setup(self.trig,GPIO.OUT)
        GPIO.setup(self.echo,GPIO.IN)
        GPIO.output(self.trig, False)
        print ("Waiting For Sensor To Settle")
        time.sleep(2)
        GPIO.output(self.trig, True)
        time.sleep(0.00001)
        GPIO.output(self.trig, False)
        while GPIO.input(self.echo)==0:
            pulse_start = time.time()
        
        while GPIO.input(self.echo)==1:
            pulse_end = time.time()
        
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        print ("Distance: ",distance,"cm")
        GPIO.cleanup()
        return distance

if __name__ == '__main__':
    try:
        c = myUltrasonic(9,10) 
        print(c.medir())
    except KeyboardInterrupt:
        pass
    finally:
        print("Finally Distancia")
