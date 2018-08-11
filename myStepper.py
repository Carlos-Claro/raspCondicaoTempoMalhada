#!/usr/bin/python

from time import sleep
import RPi.GPIO as GPIO
import os


class myStepper(object):

    def __init__(self):
        self.IN1=12
        self.IN2=16
        self.IN3=20
        self.IN4=21
        self.time = 0.001

    def on(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.IN1, GPIO.OUT)
        GPIO.setup(self.IN2, GPIO.OUT)
        GPIO.setup(self.IN3, GPIO.OUT)
        GPIO.setup(self.IN4, GPIO.OUT)
        GPIO.output(self.IN1, False)
        GPIO.output(self.IN2, False)
        GPIO.output(self.IN3, False)
        GPIO.output(self.IN4, False)
    
    def teste(self,voltas):
        self.on()
        x = 0
        y = 520*int(voltas)
        while x < y:
            self.Step1()
            self.Step2()
            self.Step3()
            self.Step4()
            self.Step5()
            self.Step6()
            self.Step7()
            self.Step8()
            print x
            x = x+1
        return True

    def go(self,voltas):
        self.on()
        x = 0
        y = 520*int(voltas)
        while x < y:
            self.Step1()
            self.Step2()
            self.Step3()
            self.Step4()
            self.Step5()
            self.Step6()
            self.Step7()
            self.Step8()
            print x
            x = x+1

    def back(self,voltas):
        self.on()
        x = 0
        y = 520*int(voltas)
        while x < y:
            self.Step8()
            self.Step7()
            self.Step6()
            self.Step5()
            self.Step4()
            self.Step3()
            self.Step2()
            self.Step1()
            print x
            x = x+1
    
    def Step1(self):
        GPIO.output(self.IN4, True)
        sleep (self.time)
        GPIO.output(self.IN4, False)

    def Step2(self):
        GPIO.output(self.IN4, True)
        GPIO.output(self.IN3, True)
        sleep (self.time)
        GPIO.output(self.IN4, False)
        GPIO.output(self.IN3, False)

    def Step3(self):
        GPIO.output(self.IN3, True)
        sleep (self.time)
        GPIO.output(self.IN3, False)

    def Step4(self):
        GPIO.output(self.IN2, True)
        GPIO.output(self.IN3, True)
        sleep (self.time)
        GPIO.output(self.IN2, False)
        GPIO.output(self.IN3, False)

    def Step5(self):
        GPIO.output(self.IN2, True)
        sleep (self.time)
        GPIO.output(self.IN2, False)

    def Step6(self):
        GPIO.output(self.IN1, True)
        GPIO.output(self.IN2, True)
        sleep (self.time)
        GPIO.output(self.IN1, False)
        GPIO.output(self.IN2, False)

    def Step7(self):
        GPIO.output(self.IN1, True)
        sleep (self.time)
        GPIO.output(self.IN1, False)

    def Step8(self):
        GPIO.output(self.IN4, True)
        GPIO.output(self.IN1, True)
        sleep (self.time)
        GPIO.output(self.IN4, False)
        GPIO.output(self.IN1, False)


if __name__ == '__main__':
    try:
        a = myStepper()
        a.teste(1)
        #a.go(3)
        #sleep(1)
        #a.back(3)
        #sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
        print("Finally Stepper")













