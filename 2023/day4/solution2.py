import re

REGEX_PATTERN = r"^Card\s+(\d+):\s+((\d+\s+)+)\|((\s+\d+)+)$"

input_file = open("input.txt", "r")
data = input_file.read()

n = len(data.split("\n")) - 1
array = [1 for i in range(n)]

for match in re.finditer(REGEX_PATTERN, data, re.MULTILINE):
    winning_set = set([int(x) for x in match.group(2).split()])
    playing_set = set([int(x) for x in match.group(4).split()])

    game_number = int(match.group(1))

    count = len(winning_set.intersection(playing_set))
    for i in range(game_number, game_number + count):
        array[i] += array[game_number - 1]

print(sum(array))
