import re


def split_into_letters(line):
    elements = []
    for i in range(1, len(line), 4):
        elements.append(line[i])
    return elements


md = [[] for i in range(9)]
file = open('input.txt')
file_line = file.readline()
while file_line:
    elements = split_into_letters(file_line.strip("\n"))
    if elements[0] == '1':
        break
    for index, val in enumerate(elements):
        if val.strip():
            md[index].append(val)
    file_line = file.readline()

file.readline()
file_line = file.readline()
pattern = r"^move (\d{1,2}) from (\d) to (\d)$"

while (file_line):
    g = re.search(pattern, file_line.strip("\n"))
    n = int(g[1])
    fr = int(g[2])-1
    to = int(g[3])-1
    md[to] = md[fr][:n] + md[to]
    md[fr] = md[fr][n:]
    file_line = file.readline()

print("".join([a[0] for a in md]))

file.close()
