import numpy as np


def scenic_score(li, x):
    if not np.any(li >= x):
        return len(li)
    # print(np.where(li>=x)[])
    return np.where(li >= x)[0][0]+1


with open('input.txt') as f:
    data = [list(map(int, x)) for x in f.read().split("\n")]

data = np.array(data)
(x, y) = data.shape
max = 0
for i in range(1, x-1):
    for j in range(1, y-1):
        cur = data[i, j]
        large = scenic_score(data[i, :j][::-1], cur) * \
            scenic_score(data[i, j+1:], cur) *\
            scenic_score(data[:i, j][::-1], cur) * \
            scenic_score(data[i+1:, j], cur)
        if (large > max):
            max = large

print(max)
