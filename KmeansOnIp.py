from pymongo import MongoClient;
import pandas as pd
import numpy as np
from PreProcessingFinal import SplitByDotIp
import matplotlib.pyplot as plt


mongoClient = MongoClient();
db = mongoClient.Cyber


trainingData=[]
dataset = db.cowrie.distinct("src_ip",{"eventid":"cowrie.login.success"})

for i in range(0,len(dataset)):
    trainingData.append(SplitByDotIp(dataset[i]))

from sklearn.cluster import KMeans
from scipy.spatial import distance

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(trainingData)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()

kmeans = KMeans(n_clusters = 6, init = 'k-means++', random_state = 42)

y_kmeans = kmeans.fit_predict(trainingData)


def Distance(cluster,data):
    return distance.euclidean(kmeans.cluster_centers_[cluster],data)
        
Finalwcss=[]
for i in range(0,len(y_kmeans)):
    Finalwcss.append(Distance(y_kmeans[i],trainingData[i]));

plt.plot(Finalwcss,"*");
plt.show()    

test = [[2,232,233,104]]
print(Distance(kmeans.predict(test),test[0]))

