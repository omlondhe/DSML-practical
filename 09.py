# Write a program to do the following: 
# You have given a collection of 8 points. 
# P1=[0.1,0.6] P2=[0.15,0.71] P3=[0.08,0.9] P4=[0.16, 0.85]
# P5=[0.2,0.3] P6=[0.25,0.5] P7=[0.24,0.1] P8=[0.3,0.2]. 
# Perform the k-mean clustering with initial centroids as m1=P1=Cluster#1=C1 and
# m2=P8=cluster#2=C2. 
# Answer the following 
# 1] Which cluster does P6 belong to? 
# 2] What is the population of a cluster around m2? 
# 3] What is the updated value of m1 and m2?

import numpy as np
import matplotlib.pyplot as plt
import math

x = np.array([0.1, 0.15, 0.08, 0.16, 0.2, 0.25, 0.24, 0.3])
y = np.array([0.6, 0.71, 0.9, 0.85, 0.3, 0.5, 0.1, 0.2])

# showing initial point positions
plt.plot(x, y, "o")
plt.show()

def euclidian(x1, y1, x2, y2):
    return math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

def manhattan(x1, y1, x2, y2):
    return math.fabs(x2 - x1) + math.fabs(y2 - y1)

def getCluster(m1, m2, x, y):
    distanceM1 = manhattan(m1[0], m1[1], x, y)
    distanceM2 = manhattan(m2[0], m2[1], x, y)
    return 1 if distanceM1 < distanceM2 else 2

# initial centroids
m1 = [0.1, 0.6]
m2 = [0.3, 0.2]

difference = math.inf
iterations = 0

while True:
    print(f"Iteration: {iterations}\nm1 = {m1}, m2 = {m2}")
    cluster1 = []
    cluster2 = []

    # assign all points to nearest cluster
    for i in range(x.size):
        cluster = getCluster(m1, m2, x[i], y[i])
        point = [x[i], y[i]]
        if cluster == 1:
            cluster1.append(point)
        else:
            cluster2.append(point)
    
    print(f"Cluster 1: {cluster1}\nCluster 2: {cluster2}")

    # calculate new centroids
    m1_old = m1
    m1 = []
    m1 = np.mean(cluster1, axis=0) # axis=0 means column wise
    m2_old = m2
    m2 = []
    m2 = np.mean(cluster2, axis=0) # axis=0 means column wise
    print(f"m1: {m1}, m2: {m2}")

    if m1[0] == m1_old[0] and m1[1] == m1_old[1] and m2[0] == m2_old[0] and m2[1] == m2_old[1]:
        break

    # adjusting differences of adjustment between m1 and m1_old
    xAvg = 0.0
    xAvg = math.fabs(m1[0] - m1_old[0]) + math.fabs(m2[0] - m2_old[0])
    xAvg /= 2
    yAvg = 0.0
    yAvg = math.fabs(m1[1] - m1_old[1]) + math.fabs(m2[1] - m2_old[1])
    yAvg /= 2

    if xAvg > yAvg:
        difference = xAvg
    else:
        difference = yAvg
    
    print(f"Difference: {difference}")
    iterations += 1


print(f"Cluster 1 centroid: {m1}")
print(f"Cluster 1 points: {cluster1}")
print(f"Cluster 2 centroid: {m2}")
print(f"Cluster 2 points: {cluster2}")

c1 = np.array(cluster1)
c2 = np.array(cluster2)

plt.plot(c1[:, 0], c1[:, 1], "o") # cluster 1 points
plt.plot(c2[:, 0], c2[:, 1], "*") # cluster 2 points
plt.plot([m1[0], m2[0]], [m1[1], m2[1]], "^") # centroids
plt.show()

P6 = [0.25,0.5]
print(f"\n\nP6 belongs to {'cluster 1' if cluster1.__contains__(P6) else 'cluster 2'}")
print(f"Population of cluster around m2: {cluster2.__len__()}")
print(f"Updated m1: {m1}, m2: {m2}")
