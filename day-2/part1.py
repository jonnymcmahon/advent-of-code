import re

path = 'input.txt'

with open(path, 'r') as file:

    data = file.read()
    
    data = re.sub('Game ', '', data).split('\n')

limits = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

possible_games = []

for game in data:

    possible = True
    
    game = game.split(': ')

    game_id = int(game[0])

    cubes = re.sub(';', ',', game[1]).split(', ')

    for cube in cubes:

        if possible == False:
            break

        cube = cube.split(' ')
        
        if int(cube[0]) > limits[cube[1]]:

            possible = False

    if possible == True:
        possible_games.append(game_id)

print(sum(possible_games))