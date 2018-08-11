#!/usr/bin/python3

import Adafruit_DHT
import RPi.GPIO as GPIO
import time


class myDHT11(object):

    def __init__(self,PINO):
        self.pino = PINO
        #self.get_dados()

    def get_dados(self):
        sensor = Adafruit_DHT.DHT11
        GPIO.setmode(GPIO.BCM)
        pino_sensor =self.pino
        humid, temp = Adafruit_DHT.read_retry(sensor, pino_sensor);
        if humid is not None and temp is not None:
            self.humidade = humid
            self.temperatura = temp
            return self
        else:
            print("Erro ao ler DHT11")

    def temperatura(self):
        return self.temperatura

    def humidade(self):
        return self.humidade


if __name__ == '__main__':
    try:
        while(True):
            c = myDHT11(17)
            d = c.get_dados()
            print(d.temperatura)
            print(d.humidade)
            time.sleep(5)
        #humidade = c.humidade()
        #temperatura = c.temperatura()
        #print ("Temperatura = {0:0.1f}  Umidade = {1:0.1f}").format(d.temperatura(), d.humidade())
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
        print("Finally temperatura e humidade")

