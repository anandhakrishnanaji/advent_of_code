import re
s = 0
dir_dic = {}
dir_stack = []

dir_regex = r"^\$ cd ([a-z\/]+)$"
file_regex = r"^(\d+) [a-z\.]+$"
back_regex = r"^\$ cd \.\.$"

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
            s += int(g2[1])
        elif (g3):
            last_dir = "_".join(dir_stack)
            dir_stack.pop()
            dir_dic["_".join(dir_stack)] += dir_dic[last_dir]
        file_line = f.readline().strip("\n")


while (len(dir_stack) > 1):
    dir_dic["_".join(dir_stack[:-1])] += dir_dic["_".join(dir_stack)]
    dir_stack.pop()

diff = 70000000 - dir_dic["/"]
needed_diff = 30000000 - diff
print(min(map(lambda y: y[1], filter(
    lambda x: x[1] > needed_diff, dir_dic.items()))))
