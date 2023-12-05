import re

dir_dic = {}

dir_regex = r"^\$ cd ([a-z\/]+)$"
file_regex = r"^(\d+) [a-z\.]+$"
back_regex = r"^\$ cd \.\.$"

dir_stack = []

with open('input.txt') as f:
    file_line = f.readline().strip("\n")
    while (file_line):
        g1 = re.search(dir_regex, file_line)
        g2 = re.search(file_regex, file_line)
        g3 = re.search(back_regex, file_line)
        if (g1):
            dir_stack.append(g1[1])
            dir_dic["_".join(dir_stack)] = 0
        elif (g2):
            dir_dic["_".join(dir_stack)] += int(g2[1])
        elif (g3):
            last_dir = "_".join(dir_stack)
            dir_stack.pop()
            dir_dic["_".join(dir_stack)] += dir_dic[last_dir]
        file_line = f.readline().strip("\n")


while (len(dir_stack) > 1):
    dir_dic["_".join(dir_stack[:-1])] += dir_dic["_".join(dir_stack)]
    dir_stack.pop()

sum = 0
for k, v in dir_dic.items():
    if (v <= 100000):
        sum += v

print(sum)
