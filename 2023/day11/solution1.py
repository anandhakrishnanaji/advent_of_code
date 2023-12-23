import numpy as np


def manhattan_distance(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)


input_file = open("input.txt", "r")
data = list(map(list, input_file.read().split("\n")[:-1]))

np_matrix = np.array(data)

vcs = []
hcs = []

rows, cols = np_matrix.shape

for i in range(rows):
    if all(np_matrix[i, :] == "."):
        vcs.append(i + len(vcs))

for i in range(cols):
    if all(np_matrix[:, i] == "."):
        hcs.append(i + len(hcs))

for i in vcs:
    np_matrix = np.insert(np_matrix, i + 1, ".", axis=0)

for i in hcs:
    np_matrix = np.insert(np_matrix, i + 1, ".", axis=1)

galaxies = []

rows, cols = np_matrix.shape

for i in range(rows):
    for j in range(cols):
        if np_matrix[i, j] == "#":
            galaxies.append((i, j))

sum = 0

for index in range(len(galaxies)):
    for j in range(index + 1, len(galaxies)):
        sum += manhattan_distance(galaxies[index], galaxies[j])

print(sum)
