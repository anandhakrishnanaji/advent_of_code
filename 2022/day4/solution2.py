def does_pair_enclose(p1, p2):
    a, b = tuple(map(int, p1.split("-")))
    c, d = tuple(map(int, p2.split("-")))
    return (c >= a and c <= b) or (d >= a and d <= b) or (c < a and d > b)


pair_list = []
with open('input.txt') as f:
    pairs = [x.strip().split(",") for x in f.readlines()]
    pair_list = list(filter(lambda x: does_pair_enclose(*x), pairs))

print(len(pair_list))
