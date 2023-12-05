import numpy as np


def max_or_zero(li):
    if not len(li):
        return -1
    return max(li)


with open('input.txt') as f:
    data = [list(map(int, x)) for x in f.read().split("\n")]

data = np.array(data)
(x, y) = data.shape
total = 2*(x+y-2)
for i in range(1, x-1):
    for j in range(1, y-1):
        large = min(max_or_zero(data[i, :j]), max_or_zero(data[i, j+1:]),
                    max_or_zero(data[:i, j]), max_or_zero(data[i+1:, j]))
        if (large < data[i, j]):
            total += 1

print(total)
