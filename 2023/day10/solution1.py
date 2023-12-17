import pdb
import sys

sys.setrecursionlimit(1000000)


def dfs(loc, steps):
    i, j = loc

    if (
        i < 0
        or i >= nrows
        or j < 0
        or j >= ncols
        or data[i][j] == "."
        or (distance_matrix[i][j] != -1 and steps >= distance_matrix[i][j])
    ):
        return

    distance_matrix[i][j] = steps

    if data[i][j] == "S":
        dfs((i + 1, j), steps + 1)
        dfs((i - 1, j), steps + 1)
    elif data[i][j] == "|":
        dfs((i + 1, j), steps + 1)
        dfs((i - 1, j), steps + 1)
    elif data[i][j] == "-":
        dfs((i, j - 1), steps + 1)
        dfs((i, j + 1), steps + 1)
    elif data[i][j] == "L":
        dfs((i - 1, j), steps + 1)
        dfs((i, j + 1), steps + 1)
    elif data[i][j] == "J":
        dfs((i - 1, j), steps + 1)
        dfs((i, j - 1), steps + 1)
    elif data[i][j] == "7":
        dfs((i + 1, j), steps + 1)
        dfs((i, j - 1), steps + 1)
    elif data[i][j] == "F":
        dfs((i + 1, j), steps + 1)
        dfs((i, j + 1), steps + 1)


def find_s(data):
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == "S":
                return (i, j)


input_file = open("input.txt", "r")
data = input_file.read().split("\n")[:-1]

s_location = find_s(data)

nrows = len(data)
ncols = len(data[0])

distance_matrix = [[-1 for i in range(ncols)] for j in range(nrows)]

dfs(s_location, 0)

print(max(map(max, distance_matrix)))
