import re

md = [[]]*9
file = open('input.txt')
file_line = file.readline()
while file_line:
    elements = file_line.strip().split(" ")
    print(len(elements))
    break
    if elements[0] == '1':
        break
    for val, index in enumerate(elements):
        if val:
            md[index].push(val[1])
    file_line = file.readline()

pattern = r"^move (/d{1,2}) from (/d) to (/d)$"
while (file_line):
    g = re.search(pattern, file_line.strip())
    n = int(g(1))
    fr = int(g(2))-1
    to = int(g(3))-1
    md[to] = md[fr][:n]+md[to]
    md[fr] = md[n:]

print([a for a in md])

file.close()