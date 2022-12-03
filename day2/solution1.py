dic = {"X": 1, "Y": 2, "Z": 3, "A": 1, "B": 2, "C": 3}


def score(a, b):
    if (dic[a] == dic[b]):
        return 3 + dic[b]
    elif (abs(dic[a]-dic[b]) < 2):
        return dic[b] if dic[a] > dic[b] else 6 + dic[b]
    return 6+dic[b] if dic[a] > dic[b] else dic[b]


with open('input.txt') as f:
    lines = [x.strip().split(" ") for x in f.readlines()]
    print(sum(list(map(lambda x: score(x[0], x[1]), lines))))
