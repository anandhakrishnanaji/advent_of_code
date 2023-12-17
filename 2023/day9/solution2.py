def shrink(array):
    temp = []
    for k in range(len(array) - 1):
        temp.append(array[k] - array[k + 1])
    return temp


def is_zero(array):
    return all([not i for i in array])


input_file = open("input.txt", "r")
data = [
    [int(m) for m in i.split(" ")][::-1] for i in input_file.read().split("\n")[:-1]
]

history_list = []

for i in data:
    temp = i
    history = 0
    count = 0
    while not is_zero(temp):
        value = -temp[-1] if count % 2 else temp[-1]
        history += value
        temp = shrink(temp)
        count += 1
    history_list.append(history)

print(sum(history_list))
