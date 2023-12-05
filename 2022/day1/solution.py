def list_of_string_sum(x):
    return sum(map(lambda y: int(y), x.split("\n")))


input_file = open("input.txt", "r")
data = input_file.read()
calories_by_each_elf = list(map(list_of_string_sum, data.split("\n\n")[:-1]))

elf_with_max_calories = max(calories_by_each_elf)
total_of_top3_elf_calories = sum(sorted(calories_by_each_elf)[-3:])

print(elf_with_max_calories)
print(total_of_top3_elf_calories)
