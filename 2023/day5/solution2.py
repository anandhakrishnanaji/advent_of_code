import math
import numpy as np

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

min_seed = math.inf

for i in range(0, len(seeds), 2):
    k = seeds[i]
    range_val = seeds[i + 1]
    qseeds = np.arange(k, k + range_val)
    qseeds_clone = qseeds.copy()
    tqseeds = qseeds_clone.copy()
    for sub_list in map_list:
        tqseeds = qseeds_clone.copy()
        for dest, source, range_lim in sub_list:
            x = tqseeds - source
            diff = dest - source
            filter_array = np.logical_and(x >= 0, x < range_lim)
            qseeds_clone[filter_array] += diff
    min_seed = min(min_seed, min(qseeds_clone))
    print(min_seed, min(qseeds_clone))

print(min_seed)
