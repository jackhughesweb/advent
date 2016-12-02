import re

def parse(txt):
    return re.findall('(R|L|U|D)', txt)
    
def move(current, direction):
    if direction == 'R':
        opts = {1: 2,
                2: 3,
                3: 3,
                4: 5,
                5: 6,
                6: 6,
                7: 8,
                8: 9,
                9: 9}
        return opts[current]
    else:
        if direction == 'L':
            opts = {1: 1,
                    2: 1,
                    3: 2,
                    4: 4,
                    5: 4,
                    6: 5,
                    7: 7,
                    8: 7,
                    9: 8}
            return opts[current]
        else:
            if direction == 'U':
                opts = {1: 1,
                        2: 2,
                        3: 3,
                        4: 1,
                        5: 2,
                        6: 3,
                        7: 4,
                        8: 5,
                        9: 6}
                return opts[current]
            else:
                opts = {1: 4,
                        2: 5,
                        3: 6,
                        4: 7,
                        5: 8,
                        6: 9,
                        7: 7,
                        8: 8,
                        9: 9}
                return opts[current]

with open('input.txt') as txt:
    buttons = []
    current = 5
    for line in txt:
        for direction in parse(line):
            current = move(current, direction)
        buttons = buttons + [str(current)]
    print(''.join(buttons))
