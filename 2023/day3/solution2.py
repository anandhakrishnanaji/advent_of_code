import re
import math

DEFAULT_HASH_VALUE = (0, [])
hash = {}


def add_valid_symbols_to_hash(x):
    index, (start, end), value = x

    valid_start, valid_end = max(0, start - 1), min(end, cols)
    valid_low, valid_high = max(0, index - 1), min(index + 1, rows)

    for i in range(valid_low, valid_high + 1):
        for j in range(valid_start, valid_end + 1):
            if data[i][j] != "." and not data[i][j].isdigit():
                hash_value = hash.get((i, j), DEFAULT_HASH_VALUE)
                hash[(i, j)] = (hash_value[0] + 1, hash_value[1] + [value])


def get_digits_with_positions(data):
    digit_with_positions = []

    for index, j in enumerate(data):
        digit_with_positions += [
            (index, i.span(), int(i.group())) for i in re.finditer("\d+", j)
        ]

    return digit_with_positions


def get_gear_ratio():
    return sum([math.prod(values) for count, values in hash.values() if count == 2])


input_file = open("input.txt", "r")
data = input_file.read().split("\n")
data.pop()

cols = len(data[0]) - 1
rows = len(data) - 1

for i in get_digits_with_positions(data):
    add_valid_symbols_to_hash(i)

print(get_gear_ratio())
