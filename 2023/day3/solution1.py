import re


def check_if_valid_digit(x):
    index, (start, end), _ = x

    valid_start, valid_end = max(0, start - 1), min(end, cols)
    valid_low, valid_high = max(0, index - 1), min(index + 1, rows)

    for i in range(valid_low, valid_high + 1):
        for j in range(valid_start, valid_end + 1):
            if data[i][j] != "." and not data[i][j].isdigit():
                return True

    return False


def get_digits_with_positions(data):
    digit_with_positions = []

    for index, j in enumerate(data):
        digit_with_positions += [
            (index, i.span(), int(i.group())) for i in re.finditer("\d+", j)
        ]

    return digit_with_positions


input_file = open("input.txt", "r")
data = input_file.read().split("\n")
data.pop()

cols = len(data[0]) - 1
rows = len(data) - 1

digits_with_positions = get_digits_with_positions(data)

total_sum = sum(
    map(lambda x: x[2], filter(check_if_valid_digit, digits_with_positions))
)

print(total_sum)
