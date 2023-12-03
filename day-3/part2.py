import re

path = 'input.txt'

with open(path, 'r') as file:

    data = file.read()
    
    data = re.sub('[+#*$/=%&@-]', 'X', data).split('\n')

class Graph:

    def __init__(self, data):
        
        self.graph = []

        self.symbol_locations = {}
        
        for y, line in enumerate(data):

            self.graph.append([char for char in line])

        self.left_neighbours = [
            (-1, -1), (-1, 0), (-1, 1)
        ] # (x, y)

        self.middle_neightbours = [
            (0, -1), (0, -1)
        ] # (x, y)

        self.right_neighbours = [
            (1, -1), (1, 0), (1, 1)
        ] # (x, y)


    def find_number(self, line, x, y):
        
        bool = True

        number = self.graph[y][x]

        x_lookup = x

        while bool is True:

            x_lookup += 1

            if x_lookup < len(line) and line[x_lookup].isnumeric():
                number += self.graph[y][x_lookup]
            else:
                bool = False

        self.numbers_list[x,y] = self.numbers_list.get((x,y), number)

        return len(number) - 1


    def generate_numbers_list(self):

        self.numbers_list = {}

        num_len = 0

        for y, line in enumerate(self.graph):
    
            for x, character in enumerate(line):

                if character.isnumeric():

                    if num_len > 0:
                        num_len -= 1
                        continue

                    num_len = self.find_number(line, x, y)


    def check_for_limits(self, x, x_offset, y, y_offset):

        if (x + x_offset) < 0 or (y + y_offset) < 0 or (x + x_offset) > 139 or (y + y_offset) > 139:
            return True


    def check_neighbours(self, x , y, num_len):
        
        for x_offset, y_offset in self.left_neighbours:

            if self.check_for_limits(x, x_offset, y, y_offset): continue

            if self.graph[y + y_offset][x + x_offset] == 'X':
                
                return (y + y_offset), (x + x_offset), True

        for x_offset, y_offset in self.right_neighbours:

            x_offset += num_len - 1

            if self.check_for_limits(x, x_offset, y, y_offset): continue

            if self.graph[y + y_offset][x + x_offset] == 'X':
                
                return (y + y_offset), (x + x_offset), True

        x_offset = 0

        limit = num_len - 1

        while x_offset <= limit:

            above_valid = True
            below_valid = True

            if (y - 1) < 0:
                above_valid = False
            if (y + 1) > 139:
                below_valid = False

            if (x + x_offset) > 139:
                break

            if above_valid and self.graph[y - 1][x + x_offset] == 'X':
                return (y - 1), (x + x_offset), True
            
            if below_valid and self.graph[y + 1][x + x_offset] == 'X':
                return (y + 1), (x + x_offset), True

            x_offset += 1

        return False


    def find_symbol_locations(self):

        self.generate_numbers_list()
        
        for (x,y), number in self.numbers_list.items():

            result = self.check_neighbours(x, y, len(number))

            if result:
                    
                y_symbol = result[0]
                x_symbol = result[1]

                if (x_symbol, y_symbol) not in self.symbol_locations:
                    self.symbol_locations[x_symbol, y_symbol] = [int(number)]
                else:
                    self.symbol_locations[x_symbol, y_symbol].append(int(number))


    def calculate_gear_ratios(self):

        self.find_symbol_locations()

        total_gear_ratios = 0

        for coords, number in self.symbol_locations.items():
            
            if len(number) == 2:
                
                gear_ratio = number[0] * number[1]

                total_gear_ratios += gear_ratio

        print(total_gear_ratios)


graph = Graph(data)

graph.calculate_gear_ratios()