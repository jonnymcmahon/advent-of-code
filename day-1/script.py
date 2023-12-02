import re
import time

path = 'input.txt'

result = []

nums = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}

with open(path, 'r') as file:

    data = file.read()

    data = re.sub('[abcdjklmpqyz]', '', data).split('\n')

for string in data:

    first_index = len(string)
    last_index = -1

    for numeral, word in nums.items():
        
        if numeral in string:

            if string.find(numeral) < first_index:

                first_index = string.find(numeral)
                first_num = numeral

            if string.rfind(numeral) > last_index:
                
                last_index = string.rfind(numeral)
                last_num = numeral

        if word in string:

            if string.find(word) < first_index:

                first_index = string.find(word)
                first_num = numeral

            if string.rfind(word) > last_index:
                
                last_index = string.rfind(word)
                last_num = numeral

    string = first_num + last_num

    if len(string) <= 1:
    
        result.append(int(string + string))
    
        continue
    
    result.append(int(string[0] + string[len(string) - 1]))

print(sum(result))