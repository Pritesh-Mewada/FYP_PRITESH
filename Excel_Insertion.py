from pymongo import MongoClient;
import xlsxwriter
import pandas as pd
import numpy as np


mongoClient = MongoClient();


db = mongoClient.Jay

dataset = db.cowrie.find({"eventid":"cowrie.client.version"});




# Create a workbook and add a worksheet.
# workbook = xlsxwriter.Workbook('cowrieLoginSuccess.xlsx')
# worksheet = workbook.add_worksheet()

row =0
col=0

total=[]

for i in range(0,db.cowrie.find({"eventid":"cowrie.client.version"}).count()):
    dictobject = dict(dataset[i])
    object = list(dictobject.keys())
    print(i)
    datarow=[]
    for c in range(0,len(object)):
        datarow.append(str(dictobject[object[c]]))
    row = row+1
    total.append(datarow)

fd = pd.DataFrame(total)
fd.to_csv("CowrieClientVersion.csv")
