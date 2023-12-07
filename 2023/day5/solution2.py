import re

MAP_TITLES = [
    "seed-to-soil map:",
    "soil-to-fertilizer map:",
    "fertilizer-to-water map:",
    "water-to-light map:",
    "light-to-temperature map:",
    "temperature-to-humidity map:",
    "humidity-to-location map:",
]

map_list = []

input_file = open("input.txt", "r")
data = input_file.read().split("\n")

seeds = list(map(int, filter(lambda x: x.isdigit(), data[0].split())))

for index, value in enumerate(MAP_TITLES):
    start_index = data.index(value)
    temp_index = start_index + 1

    temp_list = []

    while data[temp_index] != "":
        temp_list.append(tuple(map(int, data[temp_index].split())))
        temp_index += 1

    map_list.append(temp_list)

final_seeds = []

memory = [{} for i in MAP_TITLES]

for i in range(0, len(seeds), 2):
    [start, range_val] = seeds[i : i + 2]
    mid_list = map(x[1] for x in map_list[0])
    valid_start = 
    for seed in range(k, k + range_val):
        for index, sub_list in enumerate(map_list):
            if memory[index].get(seed):
                seed = memory[index][seed]
                continue
            for dest, source, range_lim in sub_list:
                if seed in range(source, source + range_lim):
                    memory[index][seed] = dest + (seed - source)
                    seed = dest + (seed - source)
                    break
        print(seed)
        final_seeds.append(seed)

print(min(final_seeds))
