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
import matplotlib.pyplot as plt

class myCondicaoTempo(object):

    def __init__(self):
        self.sets()

    def sets(self):
        self.setTemp()
        self.setChuva()
        return self

    def executa(self):
        self.sets()
        self.setKeys()
        humidade = self.getHumidade()
        if int(humidade) < 100:
            _id = self.adicionar()
            status = self.twittar()
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
            print(_id)
            # print(status)
        else:
            self.main()

    def twittar(self):
        humidade = self.getHumidade()
        temperatura = self.getTemperatura()
        chuva = self.getChuva()
        agora = datetime.datetime.now()
        print(humidade)
        print(temperatura)
        print(chuva)
        keys = self.getKeys()
        api = twitter.Api(consumer_key=keys["consumer_key"],
                      consumer_secret=keys["consumer_secret"],
                      access_token_key=keys["access_token_key"],
                      access_token_secret=keys["access_token_secret"])
        status = api.PostUpdate('Tempo na serra, SJP, Saltinho da malhada, humidade:' + str(humidade) + ', temperatura: ' + str(temperatura) + ', chove no momento? - ' + str(chuva) + '. Fonte: Raspberry pi + Python #raspberry #Iot #python ' + str(agora.strftime('%Y-%m-%d %H:%M')))
        #return status

    def adicionar(self):
        humidade = self.getHumidade()
        m = MyMongo("meteorologia")
        data = {"humidade":humidade,"data_hora":datetime.datetime.now(),"temperatura":self.getTemperatura(), "chuva":self.getChuva()}
        _id = m.add("saltinhoo",data)
        return _id

    def getItens(self):
        temperatures = self.getTemperaturas()
        timestamps = self.getTimes()
        print(len(temperatures))
        print(len(timestamps))
        plt.plot(timestamps, temperatures)
        plt.ylabel('Temperature')
        plt.xlabel('date and time')
        plt.show()#avefig('teste.png',format='png')

    def getTemperaturas(self):
        mongo = MyMongo("meteorologia")
        date = datetime.datetime(2018,7,30,00,00)
        # return mongo.get_itens("saltinhoo",{})
        temperaturas = []
        for item in mongo.get_itens("saltinhoo",{"data_hora":{"$gt":date}}):
            for i in item:
                if i == "temperatura":
                    temperaturas.append(int(item[i]))
        return temperaturas



    def getHumidades(self):
        mongo = MyMongo("meteorologia")
        # return mongo.get_itens("saltinhoo",{})
        humidades = []
        date = datetime.datetime(2018,7,30,00,00)
        for item in mongo.get_itens("saltinhoo",{"data_hora":{"$gt":date}}):
            for i in item:
                if i == "humidade":
                    humidades.append(int(item[i]))
        return humidades

    def getTimes(self):
        mongo = MyMongo("meteorologia")
        # return mongo.get_itens("saltinhoo",{})
        times = []
        date = datetime.datetime(2018,7,30,00,00)
        for item in mongo.get_itens("saltinhoo",{"data_hora":{"$gt":date}}):
            for i in item:
                if (i == "data_hora" ):
                    times.append(item[i].strftime('%Y-%m-%d %H:%M'))
        return times


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
        return int(self.temp.temperatura)

    def getHumidade(self):
        return int(self.temp.humidade)

    def setChuva(self):
        e = myRainSensor(22)
        rain = e.get_dados()
        self.chuva = "sim"
        if int(rain.rain) == 1:
            self.chuva = "nao"
        return self

    def getChuva(self):
        return str(self.chuva)


if __name__ == '__main__':
    try:
        c = myCondicaoTempo()
        c.executa()
        #c.getItens()
    except KeyboardInterrupt:
        pass
    finally:
        print("Finaliza condicao tempo")
