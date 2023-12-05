def win(x):
    return 6 + (x+1) % 3 if x != 2 else 9


def lose(x):
    return (x-1) % 3 if x != 1 else 3


def draw(x):
    return 3+x


dic = {"X": lose, "Y": draw, "Z": win, "A": 1, "B": 2, "C": 3}


with open('input.txt') as f:
    lines = [x.strip().split(" ") for x in f.readlines()]
    print(sum(list(map(lambda x: dic[x[1]](dic[x[0]]), lines))))
