dir_dic = {}

dir_regex = "^\$ cd [a-z\/]$"
ls_regex = "^\$ ls$"

with open('input.txt') as f:
    file_line = f.readline().strip("\n")
    while (file_line):
