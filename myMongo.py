from pymongo import MongoClient
import datetime
import pprint

class MyMongo(object):

    def __init__(self,database):
        self.client = MongoClient("localhost",27017)
        self.db = self.client.database

    def add(self,collection,data):
        colection = self.db.collection
        add_id = colection.insert_one(data).inserted_id
        return add_id

    def get_item(self,collection,data):
        p = self.db.collection.find_one(data)
        return p

    def get_itens(self,collection,data):
        p = self.db.collection.find(data)
        return p

if __name__ == '__main__':
    try:
        m = MyMongo("meteorologia")
        data = {"distancia":5.17,"data_hora": datetime.datetime.now()}
        _id = m.add("teste",data)
        print(_id)
        a = m.get_item("teste",{"_id":_id})
        pprint.pprint(a)
        p = m.get_item("teste",{"distancia":{"$gt":5}})
        pprint.pprint(p)
    except KeyboardInterrupt:
        pass
    finally:
        print("Mongo finish")
