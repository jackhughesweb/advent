import re

def parse(txt):
    return re.findall('(R|L|U|D)', txt)
    
def move(current, direction):
    if direction == 'R':
        opts = {1: 1,
                2: 3,
                3: 4,
                4: 4,
                5: 6,
                6: 7,
                7: 8,
                8: 9,
                9: 9,
                'A': 'B',
                'B': 'C',
                'C': 'C',
                'D': 'D'}
        return opts[current]
    else:
        if direction == 'L':
            opts = {1: 1,
                    2: 1,
                    3: 2,
                    4: 3,
                    5: 5,
                    6: 5,
                    7: 6,
                    8: 7,
                    9: 8,
                    'A': 'A',
                    'B': 'A',
                    'C': 'B',
                    'D': 'D'}
            return opts[current]
        else:
            if direction == 'U':
                opts = {1: 1,
                        2: 2,
                        3: 1,
                        4: 4,
                        5: 5,
                        6: 2,
                        7: 3,
                        8: 4,
                        9: 9,
                        'A': 6,
                        'B': 7,
                        'C': 8,
                        'D': 'B'}
                return opts[current]
            else:
                opts = {1: 3,
                        2: 6,
                        3: 7,
                        4: 8,
                        5: 5,
                        6: 'A',
                        7: 'B',
                        8: 'C',
                        9: 9,
                        'A': 'A',
                        'B': 'D',
                        'C': 'C',
                        'D': 'D'}
                return opts[current]

with open('input.txt') as txt:
    buttons = []
    current = 5
    for line in txt:
        for direction in parse(line):
            current = move(current, direction)
        buttons = buttons + [str(current)]
    print(''.join(buttons))
