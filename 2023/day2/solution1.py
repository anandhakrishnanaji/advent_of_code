import re

RED_LIMIT = 12
GREEN_LIMIT = 13
BLUE_LIMIT = 14

GAME_NO_REGEX = "^Game (\d+):"


def generate_regex(color):
    return f"(\d+) {color}"


def game_number_if_valid(x):
    if not x:
        return 0

    game_number = int(re.search(GAME_NO_REGEX, x).group(1))

    max_red = max(map(int, re.findall(generate_regex("red"), x)))
    max_green = max(map(int, re.findall(generate_regex("green"), x)))
    max_blue = max(map(int, re.findall(generate_regex("blue"), x)))

    return (
        game_number
        if max_red <= RED_LIMIT and max_green <= GREEN_LIMIT and max_blue <= BLUE_LIMIT
        else 0
    )


input_file = open("input.txt", "r")
data = input_file.read()
total_sum = sum(list(map(game_number_if_valid, data.split("\n"))))

print(total_sum)
