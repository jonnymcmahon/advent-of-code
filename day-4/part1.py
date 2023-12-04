import re

path = 'input.txt'

with open(path, 'r') as file:

    data = file.read()
    
    cards = re.sub('Card\s*(\d+): ', '', data).split('\n')

total_points = 0

for card in cards:

    card = card.split(' | ')

    winning_numbers = [num for num in card[0].split(' ') if num]

    numbers_on_card = [num for num in card[1].split(' ') if num]

    match_number = len(set(winning_numbers) & set(numbers_on_card))

    if match_number == 0: continue

    points = 1

    match_number -= 1

    while match_number > 0:
        points *= 2

        match_number -= 1

    total_points += points

print(total_points)