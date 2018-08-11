#!/usr/bin/python                                                                                             
# -*- coding: utf-8 -*- 
import string
from myMongo import MyMongo
import datetime
import pprint
from myDHT11 import myDHT11
from myRainSensor import myRainSensor
from myCondicaoTempo import myCondicaoTempo


# c = myCondicaoTempo()
# c.getItens()

c = myDHT11(17)
temp = c.get_dados()
e = myRainSensor(22)
rain = e.get_dados()
m = MyMongo("meteorologia")
print(rain.rain)
chuva = "sim"
if int(rain.rain) == 1:
    chuva = "nao"
print(chuva)
print(temp.humidade)
print(temp.temperatura)
data = {"humidade":temp.humidade,"data_hora": datetime.datetime.now(),"temperatura":temp.temperatura,"chuva":chuva}
id = m.add("saltinho",data)
print(id)
a = m.get_item("saltinho",{"_id":id})
pprint.pprint(a)





    # b = m.get_itens('situacao',{})
    # for c in b:
    #     pprint.pprint(c)
