#!/usr/bin/python
# -*- coding: utf-8 -*- 
import string
from myMongo import MyMongo
import datetime
import pprint
import twitter
import json
from myDHT11 import myDHT11
from myRainSensor import myRainSensor

# DHT 17
# Rain 22
# 3.3v

class myCondicaoTempo(object):

    def __init__(self):
        # self.main()

    def main():
        self.setKeys()
        self.setTemp()
        self.setChuva()
        humidade = self.getHumidade()
        if int(humidade) < 100:
            _id = self.adicionar()
            status = self.twittar()
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
            print(_id)
            print(status)
        else:
            self.main()

    def twittar(self):
        humidade = self.getHumidade()
        agora = datetime.datetime.now()
        keys = self.getKeys()
        api = twitter.Api(consumer_key=keys["consumer_key"],
                      consumer_secret=keys["consumer_secret"],
                      access_token_key=keys["access_token_key"],
                      access_token_secret=keys["access_token_secret"])
        status = api.PostUpdate('Tempo na serra, SJP, Saltinho da malhada, humidade:' + self.getHumidade() + ', temperatura: ' + self.getTemperatura() + ', chove no momento? - ' + self.getChuva() + '. Fonte: Raspberry pi + Python #raspberry #Iot #python ' + agora.strftime('%Y-%m-%d %H:%M'))
        return status

    def adicionar(self):
        humidade = self.getHumidade()
        m = MyMongo("meteorologia")
        data = {"humidade":humidade,"data_hora":datetime.datetime.now(),"temperatura":self.getTemperatura(), "chuva":getChuva()}
        _id = m.add("saltinhoo",data)
        return _id


    def setKeys(self):
        with open("/home/pi/Sensores/keys.json","r") as arquivo:
            data = json.load(arquivo)
            self.keys = data
            return self

    def getKeys(self):
        return self.keys

    def setTemp(self):
        c = myDHT11(17)
        self.temp = c.get_dados()
        return self

    def getTemperatura(self):
        return str(int(self.temp.temperatura))

    def getHumidade(self):
        return str(int(self.temp.humidade))

    def setChuva(self):
        e = myRainSensor(22)
        rain = e.get_dados()
        self.chuva = "sim"
        if int(rain.rain) == 1:
            self.chuva = "não"
        return self

    def getChuva(self):
        return self.chuva


f __name__ == '__main__':
    try:
        c = myCondicaoTempo()
        c.main()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
        print("Finaliza condicao tempo")
