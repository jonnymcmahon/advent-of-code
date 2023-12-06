import re
import pandas as pd
import time
from functools import reduce

start_time = time.time()

path = 'input.txt'

with open(path, 'r') as file:

    data = file.read().split('\n')

def load_data(data):

    input = {}

    for line in data:

        title = re.search('\D+:', line).group()
        
        line = re.sub('\D', ' ', line)
        line = line.replace(' ', '')

        input[title[:-1]] = line

    return input
        
def process_race(race_time, record):
 
    winners = 0

    for i in range(race_time + 1):

        t_hold = i
        t_run = race_time - i

        distance = t_hold * t_run

        if distance > record:
            winners += 1

    return winners


input = load_data(data)

winners = []

winners.append(process_race(int(input['Time']), int(input['Distance'])))

result = reduce(lambda x, y: x * y, winners)

end_time = time.time()

print((end_time - start_time) * 1000, 'ms')

print(result)