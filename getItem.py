import string
from myMongo import MyMongo
import datetime
import pprint

m = MyMongo("meteorologia")
b = m.get_itens('situacao',{})
for c in b:
    pprint.pprint(c)
