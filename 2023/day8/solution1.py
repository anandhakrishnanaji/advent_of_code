import re
import pdb

REGEX_PATTERN = r"^(\w{3}) = \((\w{3}), (\w{3})\)$"

input_file = open("input.txt", "r")
data = input_file.read()

hash = {}

direction = data.split("\n")[0]
for match in re.findall(REGEX_PATTERN, data, re.MULTILINE):
    hash[match[0]] = {"L": match[1], "R": match[2]}

current = "AAA"
count = 0

while current != "ZZZ":
    for i in direction:
        if current == "ZZZ":
            break
        current = hash[current][i]
        count += 1

print(count)
