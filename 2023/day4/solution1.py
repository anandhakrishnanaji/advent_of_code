import re

REGEX_PATTERN = r"^Card \d+: ((\d+\s+)+)\|((\s+\d+)+)$"

input_file = open("input.txt", "r")
data = input_file.read()

for i in re.finditer(REGEX_PATTERN, data, re.MULTILINE):
    print(i)
