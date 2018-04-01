from scapy.all import  *
from packetToJson import *
from pymongo import MongoClient;

mongoClient = MongoClient();


db = mongoClient.Cyber

collection = db.BigData1;


for j in range(1,7):
    a = rdpcap("DARPA/demos"+str(j))
    print("Data Inserted Packet-->"+str(j))
    for i in range(0,len(a),1):
        data = a[0].show()
        x = packetToJson(data)
        y = {}
        y['packet'] = x
        collection.insert_one(y['packet'])
