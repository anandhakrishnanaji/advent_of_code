import numpy as np
import pdb


def manhattan_distance(a, b):
    dist = 0
    x1, y1 = a
    x2, y2 = b

    for i in range(min(x1, x2), max(x1, x2)):
        diff = 1000000 if i in vcs else 1
        dist += diff

    for i in range(min(y1, y2), max(y1, y2)):
        diff = 1000000 if i in hcs else 1
        dist += diff

    return dist


input_file = open("input.txt", "r")
data = list(map(list, input_file.read().split("\n")[:-1]))

np_matrix = np.array(data)

vcs = []
hcs = []

rows, cols = np_matrix.shape

for i in range(rows):
    if all(np_matrix[i, :] == "."):
        vcs.append(i)

for i in range(cols):
    if all(np_matrix[:, i] == "."):
        hcs.append(i)

galaxies = []

for i in range(rows):
    for j in range(cols):
        if np_matrix[i, j] == "#":
            galaxies.append((i, j))
sum = 0

for index in range(len(galaxies)):
    for j in range(index + 1, len(galaxies)):
        sum += manhattan_distance(galaxies[index], galaxies[j])

print(sum)
