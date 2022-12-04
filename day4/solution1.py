def does_pair_enclose(p1, p2):
    a, b = tuple(map(int, p1.split("-")))
    c, d = tuple(map(int, p2.split("-")))
    return a <= c and b >= d or a >= c and b <= d


pair_list = []
with open('input.txt') as f:
    pairs = [x.strip().split(",") for x in f.readlines()]
    pair_list = list(filter(lambda x: does_pair_enclose(*x), pairs))

print(len(pair_list))
