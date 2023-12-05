def get_priority(ch):
    priority = ord(ch.lower()) - 96
    return priority if ch.islower() else priority + 26


intersection_list = []
with open('input.txt') as f:
    strings = [x.strip() for x in f.readlines()]
    intersection_list = [
        set(x[:len(x)//2]).intersection(set(x[len(x)//2:])).pop() for x in strings]
print(sum(list(map(get_priority, intersection_list))))
