hash = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def extract_digits(x):
    n = len(x)
    dig_list = []

    for i in range(n):
        for j in range(i, n + 1):
            if j == i and x[i].isdigit():
                dig_list.append(x[i])
            if x[i:j] in hash:
                dig_list.append(hash[x[i:j]])

    return 0 if not dig_list else int(dig_list[0] + dig_list[-1])


input_file = open("input.txt", "r")
data = input_file.read()
total_sum = sum(list(map(extract_digits, data.split("\n"))))

print(total_sum)
