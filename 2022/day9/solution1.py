h = (0, 0)
t = (0, 0)
hash_list_1d = set()


def get_new_dir(h, t, dir):
    if (dir == "U" or dir == "D"):
        return "R" if h[0] > t[0] else "L"
    return "U" if h[1] > t[1] else "D"


def move_head_and_tail(dir, mag):
    global h, t
    for i in range(mag):
        h = move(h, dir)
        if (should_move(t, h)):
            t = move(t, dir)
            mj = t
            if h[0] != t[0] and h[1] != t[1]:
                t = move(t, get_new_dir(h, t, dir))
            hash_list_1d.add(t)


def move(k, dir):
    if (dir == "U"):
        return k[0], k[1]+1
    if (dir == "D"):
        return k[0], k[1]-1
    if (dir == "R"):
        return k[0]+1, k[1]
    return k[0]-1, k[1]


def should_move(t, h):
    return not (abs(h[0] - t[0]) <= 1 and abs(h[1] - t[1]) <= 1)


with open('input.txt') as f:
    data = [x.strip() for x in f.read().split("\n")]


for i in data:
    dir = i[0]
    mag = int(i.split()[-1])
    move_head_and_tail(dir, mag)

print(len(hash_list_1d))
