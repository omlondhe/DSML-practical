# Write a program to do the following: You have given a collection of 8 points. 
# P1=[2, 10] P2=[2, 5] P3=[8, 4] P4=[5, 8] P5=[7,5] P6=[6, 4] P7=[1, 2] P8=[4, 9]. 
# Perform the k-mean clustering with initial centroids as 
# m1=P1 =Cluster#1=C1 and m2=P4=cluster#2=C2, m3=P7 =Cluster#3=C3. 
# Answer the following 
# 1] Which cluster does P6 belong to? 
# 2] What is the population of a cluster around m3? 
# 3] What is the updated value of m1, m2, m3?

import math
import numpy as np
import matplotlib.pyplot as plt

x = np.array([2, 2, 8, 5, 7, 6, 1, 4])
y = np.array([10, 5, 4, 8, 5, 4, 2, 9])
m1 = [2, 10]
m2 = [5, 8]
m3 = [1, 2]

plt.plot(x, y, "o")
plt.show()

def euclidian(x1, y1, x2, y2):
    return math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

def manhattan(x1, y1, x2, y2):
    return math.fabs(x2 - x1) + math.fabs(y2 - y1)

def getCluster(m1, m2, m3, x, y):
    distanceM1 = manhattan(m1[0], m1[1], x, y)
    distanceM2 = manhattan(m2[0], m2[1], x, y)
    distanceM3 = manhattan(m3[0], m3[1], x, y)
    
    if distanceM1 < distanceM2 < distanceM3:
        return 1
    elif distanceM2 < distanceM1 < distanceM3:
        return 2
    else:
        return 3


distance = math.inf
iterations = 0

while True:
    print(f"Iterations: {iterations}\nm1: {m1}, m2: {m2}, m3: {m3}")
    cluster1 = []
    cluster2 = []
    cluster3 = []
 
    for i in range(x.size):
        cluster = getCluster(m1, m2, m3, x[i], y[i])
        point = [x[i], y[i]]
        if cluster == 1:
            cluster1.append(point)
        elif cluster == 2:
            cluster2.append(point)
        else:
            cluster3.append(point)
    
    print(f"Cluster 1: {cluster1}\nCluster 2: {cluster2}\nCluster 3: {cluster3}")
    
    m1_old = m1
    m1 = []
    m1 = np.mean(cluster1, axis=0)
    m2_old = m2
    m2 = []
    m2 = np.mean(cluster2, axis=0)
    m3_old = m3
    m3 = []
    m3 = np.mean(cluster3, axis=0)
    print(f"m1: {m1}, m2: {m2}, m3: {m3}")

    if m1[0] == m1_old[0] and m1[1] == m1_old[1] and m2[0] == m2_old[0] and m2[1] == m2_old[1] and m3[0] == m3_old[0] and m3[1] == m3_old[1]:
        break

    xAvg = 0.0
    xAvg = math.fabs(m1[0] - m1_old[0]) + math.fabs(m2[0] - m2_old[0]) + math.fabs(m3[0] - m3_old[0])
    xAvg /= 3
    yAvg = 0.0
    yAvg = math.fabs(m1[1] - m1_old[1]) + math.fabs(m2[1] - m2_old[1]) + math.fabs(m3[1] - m3_old[1])
    yAvg /= 3

    if xAvg > yAvg:
        difference = xAvg
    else:
        difference = yAvg
    
    print(f"Difference: {difference}")
    iterations += 1

print(f"Cluster 1 centroid: {m1}")
print(f"Cluster 1: {cluster1}")
print(f"Cluster 2 centroid: {m2}")
print(f"Cluster 2: {cluster2}")
print(f"Cluster 3 centroid: {m3}")
print(f"Cluster 3: {cluster3}")

c1 = np.array(cluster1)
c2 = np.array(cluster2)
c3 = np.array(cluster3)

plt.plot(c1[:, 0], c1[:, 1], "o")
plt.plot(c2[:, 0], c2[:, 1], "*")
plt.plot(c3[:, 0], c3[:, 1], "^")
plt.show()

P6 = [6, 4]
print(f"\n\nP6 belongs to {'cluster 1' if cluster1.__contains__(P6) else 'cluster 2'}")
print(f"Population of cluster around m3: {cluster3.__len__()}")
print(f"Updated m1: {m1}, m2: {m2}, m3: {m3}")

