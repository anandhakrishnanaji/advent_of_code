h = (0, 0)
t = (0, 0)
hash_list_1d = []


def move_head_and_tail(dir, mag):
    global h, t
    h = move(h, dir, mag)
    while (should_move(t, h)):
        t = move(t, dir, 1)
        hash_list_1d.append(t)


def move(t, dir, mag):
    if (dir == "U"):
        return t[0], t[1]+mag
    if (dir == "D"):
        return t[0], t[1]-mag
    if (dir == "R"):
        return t[0]+mag, t[1]
    return t[0]-mag, t[1]


def should_move(t, h):
    return not (h[0] == t[0] or h[1] == t[1])


with open('input.txt') as f:
    data = [x.strip() for x in f.read().split("\n")]


for i in data:
    if not i:
        break
    dir = i[0]
    mag = int(i[-1])
    move_head_and_tail(dir, mag)

max_width = max(hash_list_1d, key=lambda x: x[1])[1]+1
max_height = max(hash_list_1d, key=lambda x: x[0])[0]+1
res_array = [list("."*max_width) for i in range(max_height)]

for x, y in hash_list_1d:
    res_array[x][y] = "#"
res_array[0][0] = "S"

for li in res_array[::-1]:
    print("".join(li))
