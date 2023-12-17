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


def is_vertical_bar(char):
    return char == "|" or char == "L" or char == "J" or char == "7" or char == "F"


def is_horizontal_bar(char):
    return char == "-" or char == "L" or char == "J" or char == "7" or char == "F"


def have_vertical_bounds(loc):
    i, j = loc
    lower = upper = False
    for r in range(nrows):
        if r < i and is_horizontal_bar(data[r][j]):
            upper = True
        if r > i and is_horizontal_bar(data[r][j]):
            lower = True
    return upper and lower


input_file = open("input.txt", "r")
data = input_file.read().split("\n")[:-1]

s_location = find_s(data)

nrows = len(data)
ncols = len(data[0])

distance_matrix = [[-1 for i in range(ncols)] for j in range(nrows)]

dfs(s_location, 0)

dots = 0

for i in range(nrows):
    should_count = False
    cdots = 0
    tmp_dots = 0
    for j in range(ncols):
        if distance_matrix[i][j] != -1 and is_vertical_bar(data[i][j]):
            should_count = not should_count
            cdots += tmp_dots
            dots += tmp_dots
            tmp_dots = 0
            continue
        if (
            should_count
            and distance_matrix[i][j] == -1
            and have_vertical_bounds((i, j))
        ):
            tmp_dots += 1
    print(cdots)

# pdb.set_trace()
print(dots)
