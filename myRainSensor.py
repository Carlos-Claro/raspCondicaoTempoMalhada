#!/usr/bin/python3

import RPi.GPIO as GPIO
import time


class myRainSensor(object):

    def __init__(self,PINO):
        self.pino = PINO

    def get_dados(self):
        GPIO.setmode(GPIO.BCM)
        pino_sensor =self.pino
        GPIO.setup(pino_sensor,GPIO.IN)
        state = GPIO.input(pino_sensor)
        self.rain = state
        return self

    def rain(self):
        if self.rain == 1:
            return "nao"
        return "sim"


if __name__ == '__main__':
    try:
        while(True):
            c = myRainSensor(22)
            d = c.get_dados()
            print(d.rain)
#            print(d,rain())
            time.sleep(5)
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
        print("Finally ")

