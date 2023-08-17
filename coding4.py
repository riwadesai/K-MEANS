import pandas as pd
import random
import matplotlib.pyplot as plt
from numpy import array
import numpy as np

data = pd.read_csv("/Users/riwadesai/Documents/mathfordatascience/pok.csv", delimiter=",", usecols=["Sp. Atk", "Sp. Def"])

# initialize list of data points, center points and clusters
## all points are tuples of coordinates
point_list = array((data["Sp. Atk"], data["Sp. Def"]))
print("matrix dimension is:",len(point_list[0]), "x", len(point_list))
point_list = list(zip(data["Sp. Atk"], data["Sp. Def"]))
print("Enter number of clusters")# random for now; later, take as user input and have a default value too
k=int(input())
def random_number(dataset):
    return random.choice(dataset)


center_list = []
for i in range(k):
    center_list.append(random_number(point_list))

cluster_list = [[] for _ in range(k)]
prev_cluster_list = []

a=list()
b=list()
c=list()
d=list()
for i in point_list:
    a.append(i[0])
    b.append(i[1])
for j in center_list:
    c.append(j[0])
    d.append(j[1])

plt.scatter(a,b,color="black")
plt.title("initial centres for clustering")
plt.scatter(c,d,color="red",marker="x")
plt.draw()
plt.show()
#to generate random colours
color=["#"+''.join([random.choice('0123456789ABCDEF') for i in range(6)])
       for j in range(k)]

# helper function
def find_min_dist(pt, pt_list):
    '''
    Returns index i such that distance between pt and pt_list[i]
    is minimum when pt is compared to all pts in pt_list
    
    pt is a tuple of x-coordinate and y-coordinate
    '''
    for i in range(len(pt_list)):
        dist = (pt[0] - pt_list[i][0])**2 + (pt[1] - pt_list[i][1])**2
        if i == 0 or dist < min_dist:
            min_dist = dist
            min_dist_index = i
    
    return min_dist_index



# run algorithm till clusters stabilize
while(cluster_list != prev_cluster_list):
    prev_cluster_list = cluster_list
    cluster_list = [[] for _ in range(k)]     # reset clusters

    # add points to cluster with nearest center
    for point in point_list:
        i = find_min_dist(point, center_list)
        cluster_list[i].append(point)

    

    # recompute cluster centers
    for i in range(k):
        x_coordinates = [point[0] for point in cluster_list[i]]
        x_avg = sum(x_coordinates)/len(x_coordinates) 

        y_coordinates = [point[1] for point in cluster_list[i]]
        y_avg = sum(y_coordinates)/len(y_coordinates) 

        center_list[i] = (x_avg, y_avg)
def find_var_distance(pt1,pt2):
    dist = ((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)
    return dist


def variance (cluster, center):
    s = 0
    for i in range(len(cluster)):
        s = s + (find_var_distance(cluster[i], center))
    return s/len(cluster)


# print output
for i in range(k):
    cluster = cluster_list[i]
    print("CLUSTER " + str(i+1) + ":")
    print("No. of observations: " + str(len(cluster)))
    print("Mean: " + str(center_list[i]))
    print("Variance: " + str(variance(cluster, center_list[i])))
    print("\nPoints: ")
    print(cluster)
    print("\n" * 5)

plt.title("final clusters")
for i in range(k):
    c=color[i]
    for j in range(len(cluster_list[i])):
        plt.scatter(cluster_list[i][j][0],cluster_list[i][j][1], color=c)
for i in range(k):
    plt.scatter(center_list[i][0],center_list[i][1],color='black',marker="x")
plt.xlabel("Sp.Attack")
plt.ylabel("Sp.Def")
plt.show()
plt.draw()

print("K = " + str(k))
print("=" * 30 + "\n\n")