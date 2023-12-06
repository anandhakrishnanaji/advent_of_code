def get_first_digit(x):
    for i in x:
        if i.isdigit():
            return i


def string_sum(x):
    first_digit = get_first_digit(x)
    last_digit = get_first_digit(x[::-1])

    if first_digit == None:
        return 0

    return int(first_digit + last_digit)


input_file = open("input.txt", "r")
data = input_file.read()
total_sum = sum(list(map(string_sum, data.split("\n"))))

print(total_sum)
