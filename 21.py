# Write a program to cluster a set of points using K-means for IRIS dataset. 
# Consider K=4 clusters. 
# Consider Euclidean distance as the distance measure. Randomly initialize a cluster mean as one of the data points. 
# Iterate at least for 10 iterations. After iterations are over, print the final cluster means for each of the clusters. 


import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('11.csv')
print(data)
print()

w = np.array(data['sepal_length'])
x = np.array(data['sepal_width'])
y = np.array(data['petal_length'])
z = np.array(data['petal_width'])

def euclidian(w1, x1, y1, z1, w2, x2, y2, z2):
    return math.sqrt(pow(w2 - w1, 2) + pow(x2 - x1, 2) + pow(y2 - y1, 2) + pow(z2 - z1, 2))

def getCluster(m1, m2, m3, m4, w, x, y, z):
    differenceM1 = euclidian(m1[0], m1[1], m1[2], m1[3], w, x, y, z)
    differenceM2 = euclidian(m2[0], m2[1], m2[2], m2[3], w, x, y, z)
    differenceM3 = euclidian(m3[0], m3[1], m3[2], m3[3], w, x, y, z)
    differenceM4 = euclidian(m4[0], m4[1], m4[2], m4[3], w, x, y, z)
    if differenceM1 < differenceM2 and differenceM1 < differenceM3 and differenceM1 < differenceM4:
        return 1
    elif differenceM2 < differenceM1 and differenceM2 < differenceM3 and differenceM2 < differenceM4:
        return 2
    elif differenceM3 < differenceM1 and differenceM3 < differenceM2 and differenceM3 < differenceM4:
        return 3
    else:
        return 4


m1 = [5.1, 3.5, 1.4, 0.2]
m2 = [4.9, 3.0, 1.4, 0.2]
m3 = [4.7, 3.2, 1.3, 0.2]
m4 = [5.0, 3.6, 1.4, 0.2]
difference = 0
iteration = 0

while iteration < 10:
    print(f"Iterations: {iteration}\nm1: {m1}, m2: {m2}, m3: {m3}, m4: {m4}")
    cluster1 = []
    cluster2 = []
    cluster3 = []
    cluster4 = []

    for i in range(data.shape[0]):
        cluster = getCluster(m1, m2, m3, m4, w[i], x[i], y[i], z[i])
        point = [w[i], x[i], y[i], z[i]]
        if cluster == 1:
            cluster1.append(point)
        elif cluster == 2:
            cluster2.append(point)
        elif cluster == 3:
            cluster3.append(point)
        else:
            cluster4.append(point)
    
    print(f"Cluster 1: {cluster1}\nCluster 2: {cluster2}\nCluster 3: {cluster3}\nCluster 4: {cluster4}")

    m1_old = m1
    m1 = []
    m1 = np.mean(cluster1, axis=0)
    m2_old = m2
    m2 = []
    m2 = np.mean(cluster2, axis=0)
    m3_old = m3
    m3 = []
    m3 = np.mean(cluster3, axis=0)
    m4_old = m4
    m4 = []
    m4 = np.mean(cluster4, axis=0)

    print(f"m1: {m1}, m2: {m2}, m3: {m3}, m4: {m4}")

    xAvg = 0.0
    xAvg = np.fabs(m1[0] - m1_old[0]) + np.fabs(m2[0] - m2_old[0]) + np.fabs(m3[0] - m3_old[0]) + np.fabs(m4[0] - m4_old[0])
    xAvg /= 4
    yAvg = 0.0
    yAvg = np.fabs(m1[1] - m1_old[1]) + np.fabs(m2[1] - m2_old[1]) + np.fabs(m3[1] - m3_old[1]) + np.fabs(m4[1] - m4_old[1])
    yAvg /= 4

    if xAvg > yAvg:
        difference = xAvg
    else:
        difference = yAvg
    
    print(f"Difference: {difference}")
    iteration += 1

print(f"Cluster 1 centroids: {m1}")
print(f"Cluster 1: {cluster1}")
print(f"Cluster 2 centroids: {m2}")
print(f"Cluster 2: {cluster2}")
print(f"Cluster 3 centroids: {m3}")
print(f"Cluster 3: {cluster3}")
print(f"Cluster 4 centroids: {m4}")
print(f"Cluster 4: {cluster4}")

c1 = np.array(cluster1)
c2 = np.array(cluster2)
c3 = np.array(cluster3)
c4 = np.array(cluster4)

plt.plot(c1[:, 0], c1[:, 1], "o")
plt.plot(c2[:, 0], c2[: , 1], "*")
plt.plot(c3[:, 0], c3[: , 1], "^")
plt.plot(c4[:, 0], c4[: , 1], "|")
plt.show()

