import re
import pandas as pd

path = 'input.txt'

with open(path, 'r') as file:

    data = file.read().split('\n')

def load_data(data):

    seeds = re.sub('seeds: ', '', data[0]).split(' ')

    data.pop(0)

    almanac = {}

    titles = []

    is_title = False

    range = 0

    for line in data:

        if not line:
            is_title = True
            continue
        
        if is_title == True:

            index = line.rfind('-')
            line = line[index + 1:]
            title = re.sub(' map:', '', line)
            
            almanac[title] = {}

            titles.append(title)

            almanac[title][0] = []
            almanac[title][1] = []
            almanac[title][2] = []

            is_title = False
            continue

        nums = line.split(' ')

        almanac[title][0].append(int(nums[0]))
        almanac[title][1].append(int(nums[1]))
        almanac[title][2].append(int(nums[2]))

        maximum = max((int(nums[0]) + int(nums[2])), (int(nums[1]) + int(nums[2])))

        if maximum > range:
            range = maximum

    return seeds, almanac, range, titles

seeds, almanac, maximum, titles = load_data(data)

def transpose(seed, title):

    for dest, source, range_ in zip(almanac[title][0], almanac[title][1], almanac[title][2]):


        if seed < source: continue

        if seed >= source and seed < source + range_:

            diff = seed - source

            result = dest + diff

            return result
    
    return seed

lowest = maximum

for seed in seeds:

    seed = int(seed)

    for title in titles:

        seed = transpose(seed, title)

    if seed < lowest:

        lowest = seed

print(lowest)