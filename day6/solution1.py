file = open("input.txt", "r")
data = file.read().strip("\n")
for i in range(len(data)-4):
    if (len(set(data[i:i+4])) == 4):
        print(i+4)
        break
file.close()
