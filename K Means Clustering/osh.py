import numpy as np
import matplotlib.pyplot as plt

clusters = []
temp_clusters = [[], [], [], [], [], []]

x = [[], [], [], [], [], []]
y = [[], [], [], [], [], []]


# Loading data from CSV files into data and centers list
dp = 'data.csv'
data = np.genfromtxt(dp, delimiter=",")

dp = 'centers.csv'
centers = np.genfromtxt(dp, delimiter=",")

# print(data.shape)
# print(centers.shape)

# The main K-Means Clustering algorithm starts from here
iterator = 0
while True:
    for s in data:
        dist = []
        for c in centers:
            dist.append(np.linalg.norm(c - s))
        # print(dist)
        min_val = min(dist)
        # print(min_val)
        index = dist.index(min_val)
        # print(index)
        temp_clusters[index].append(s.tolist())
    # print(temp_clusters)

    for i in range(6):
        for item in temp_clusters[i]:
            x[i].append(item[0])
            y[i].append(item[1])
    # print(x)
    # print(y)

    # print(centers)
    for k in range(6):
        x_avg = sum(x[k]) / len(x[k])
        centers[k][0] = x_avg

        y_avg = sum(y[k]) / len(y[k])
        centers[k][1] = y_avg

    iterator += 1

    shift = 0
    if iterator > 1:

        for s in data:
            index_01 = 0
            index_02 = 0

            for m in range(6):
                is_found = False
                for item in clusters[m]:
                    if s[0] == item[0]:
                        if s[1] == item[1]:
                            # print(f'cluster found at: {m}')
                            index_01 = m
                            is_found = True
                            break
                if is_found:
                    break

            for n in range(6):
                is_found = False
                for item in temp_clusters[n]:
                    if s[0] == item[0]:
                        if s[1] == item[1]:
                            # print(f'temp cluster found at: {n}')
                            index_02 = n
                            is_found = True
                            break
                if is_found:
                    break

            if index_01 != index_02:
                # print(f'cluster found at: {index_01}')
                # print(f'temp cluster found at: {index_02}')
                shift += 1

            # print(shift)
        if shift < 10:
            clusters = temp_clusters.copy()
            break

    clusters = temp_clusters.copy()
    for j in range(6):
        temp_clusters[j].clear()
        x[j].clear()
        y[j].clear()


# This part is for plotting 
xc = []
yc = []
for c in centers:
    xc.append(c[0])
    yc.append(c[1])

colors = ['firebrick', 'olive', 'deepskyblue', 'mediumvioletred', 'rebeccapurple', 'slategrey']

for n in range(6):
    plt.scatter(x[n], y[n], s=10, color=colors[n])
    plt.scatter(xc[n], yc[n], s=90, marker='s', color='black')
plt.title("K-Means Clustering")
plt.show()
