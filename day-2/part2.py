import re

path = 'input.txt'

with open(path, 'r') as file:

    data = file.read()
    
    data = re.sub('Game [0-9]*: ', '', data).split('\n')

power = 0

for game in data:

    game_cubes = {
        'red': [],
        'blue': [],
        'green': []
    }

    cubes = re.sub(';', ',', game).split(', ')

    for cube in cubes:

        number, colour = cube.split(' ')

        game_cubes[colour].append(int(number))

    power += (max(game_cubes['red']) * max(game_cubes['blue']) * max(game_cubes['green']))

print(power)

        
