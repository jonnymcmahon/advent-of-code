import re
import pandas as pd
import time

start_time = time.time()

path = 'input.txt'

with open(path, 'r') as file:

    data = file.read().split('\n')

class Range:

    def __init__(self, start, length):
        self.source_start = start
        self._length = length

    def start(self):
        return self.source_start

    def end(self):
        return self.source_start + self._length - 1

    def length(self):
        return self._length

    def split_left(self, length):
        range1 = Range(self.source_start, length)
        range2 = Range(length + self.source_start, self._length - length)

        return range1, range2

    def split_right(self, length):
        range1 = Range(length + self.source_start, self._length - length)
        range2 = Range(self.source_start, length)

        return range1, range2

    def map(self, new_start):
        self.source_start = new_start


def generate_ranges(seeds):

    ranges_list = []

    for key, seed in enumerate(seeds):

        if key % 2 == 0:

            start = int(seed)
            length = int(seeds[key + 1])

            ranges_list.append(Range(start, length))

    return ranges_list


def load_data(data):

    ranges = generate_ranges(re.sub('seeds: ', '', data[0]).split(' '))

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

    return ranges, almanac, range, titles


def transpose(r, title, new_ranges, uncomputed_ranges):

    for dest, source, range_ in zip(almanac[title][0], almanac[title][1], almanac[title][2]):

        source_start = source
        source_end = source + range_ - 1

        dest_start = dest

        #if completely outside source range, ignore
        if r.end() < source_start: continue

        if r.start() > source_end: continue

        #if completely inside range, calculate new range
        if r.start() >= source_start and r.end() <= source_end:

            offset = r.start() - source_start
            
            r.map(dest_start + offset)

            new_ranges.append(r)

            return

        #if inside range, split left / right
        if r.start() < source_start and r.end() < source_end:

            r1, r2 = r.split_left(source_start - r.start())

            r2.map(dest_start)

            uncomputed_ranges.append(r1)
            new_ranges.append(r2)

            return


        if r.start() > source_start and r.end() > source_end:

            r1, r2 = r.split_right(source_end - r.start() + 1)

            offset = r.start() - source_start

            r2.map(dest_start + offset)

            uncomputed_ranges.append(r1)
            new_ranges.append(r2)

            return

    new_ranges.append(r)

    return

ranges, almanac, maximum, titles = load_data(data)

for title in titles:

    new_ranges = []
    uncomputed_ranges = []

    for r in ranges:

        transpose(r, title, new_ranges, uncomputed_ranges)
    
    while len(uncomputed_ranges) > 0:

        for key, r in enumerate(uncomputed_ranges):

            transpose(r, title, new_ranges, uncomputed_ranges)

            uncomputed_ranges.pop(key)

    ranges = new_ranges

lowest = maximum

for r in ranges:

    location = r.start()

    if location < lowest:

        lowest = location

end_time = time.time()

print(lowest)

print((end_time - start_time) * 1000, 'ms')