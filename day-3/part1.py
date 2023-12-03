import re

path = 'input.txt'

with open(path, 'r') as file:

    data = file.read()
    
    data = re.sub('[+#*$/=%&@-]', 'X', data).split('\n')

class Graph:

    def __init__(self, data):
        
        self.graph = []

        self.valid_numbers = []
        
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
                
                return True

        for x_offset, y_offset in self.right_neighbours:

            x_offset += num_len - 1

            if self.check_for_limits(x, x_offset, y, y_offset): continue

            if self.graph[y + y_offset][x + x_offset] == 'X':
                
                return True

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
                return True
            
            if below_valid and self.graph[y + 1][x + x_offset] == 'X':
                return True

            x_offset += 1

        return False


    def check_valid_numbers(self):

        self.generate_numbers_list()
        
        for (x,y), number in self.numbers_list.items():

            if self.check_neighbours(x, y, len(number)):
                
                self.valid_numbers.append(int(number))

        print(sum(self.valid_numbers))


graph = Graph(data)

solution = graph.check_valid_numbers()