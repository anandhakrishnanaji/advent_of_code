import re


def generate_regex(color):
    return f"(\d+) {color}"


def game_number_if_valid(x):
    if not x:
        return 0

    max_red = max(map(int, re.findall(generate_regex("red"), x)))
    max_green = max(map(int, re.findall(generate_regex("green"), x)))
    max_blue = max(map(int, re.findall(generate_regex("blue"), x)))

    return max_red * max_green * max_blue


input_file = open("input.txt", "r")
data = input_file.read()
total_sum = sum(list(map(game_number_if_valid, data.split("\n"))))

print(total_sum)
