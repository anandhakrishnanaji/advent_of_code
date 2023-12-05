def get_priority(ch):
    priority = ord(ch.lower()) - 96
    return priority if ch.islower() else priority + 26

def intersection_of_three(l):
    return get_priority(set(l[0]).intersection(set(l[1])).intersection(set(l[2])).pop())

grouped_list = []
with open('input.txt') as f:
    strings = [x.strip() for x in f.readlines()]
    grouped_list = zip(*(iter(strings),) * 3)

print(sum(list(map(intersection_of_three,grouped_list))))