import re

path = 'input.txt'

with open(path, 'r') as file:

    data = file.read()
    
    cards = re.sub('Card\s*(\d+): ', '', data).split('\n')

total_cards = len(cards)   

extra_cards = {}

num_of_cards = {}

for number, card in enumerate(cards):

    number += 1

    card = card.split(' | ')

    winning_numbers = [num for num in card[0].split(' ') if num]

    numbers_on_card = [num for num in card[1].split(' ') if num]

    extra_cards[number] = len(set(winning_numbers) & set(numbers_on_card))

    num_of_cards[number] = 1

for number, extras in extra_cards.items():

    starting_num = number

    for i in range(num_of_cards[number]):

        card_num = starting_num

        for j in range(extras):

            card_num += 1

            if card_num > total_cards: continue
            
            num_of_cards[card_num] += 1

print(sum(num_of_cards.values()))