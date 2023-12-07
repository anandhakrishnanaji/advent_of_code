import re

REGEX_PATTERN = r"^Card\s+\d+:\s+((\d+\s+)+)\|((\s+\d+)+)$"

input_file = open("input.txt", "r")
data = input_file.read()

sum = 0

for match in re.finditer(REGEX_PATTERN, data, re.MULTILINE):
    winning_set = set([int(x) for x in match.group(1).split()])
    playing_set = set([int(x) for x in match.group(3).split()])

    sum += int(2 ** (len(winning_set.intersection(playing_set)) - 1))

print(sum)
