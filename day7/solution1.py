import re

dir_dic = {}

dir_regex = r"^\$ cd ([a-z\/]+)$"
file_regex = r"^(\d+) .*$"

dir_stack = []

with open('input.txt') as f:
    file_line = f.readline().strip("\n")
    while (file_line):
        g1 = re.search(dir_regex, file_line)
        g2 = re.search(file_regex, file_line)
        if (g1):
            dir_stack.append(g1[1])
            dir_dic[g1[1]] = 0
        elif (g2):
            dir_dic[dir_stack[-1]] += int(g2[1])
        elif (file_line == "$ cd .."):
            last_dir = dir_stack.pop()
            dir_dic[dir_stack[-1]] = dir_dic[dir_stack[-1]] + dir_dic[last_dir]
        file_line = f.readline().strip("\n")

print(dir_dic)
sum = 0
for k, v in dir_dic.items():
    if (v <= 100000):
        sum += v

print(sum)
