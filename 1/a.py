import re

def parse(txt):
    return re.findall('((?:R|L)[0-9]+)', txt)

def parseSet(txt):
    r = re.search('(R|L)([0-9]+)', txt)
    return [r.groups()[0], int(r.groups()[1])]

def newDirection(direction, rl):
    if rl == "R":
        opts = {1: 2,
                2: 3,
                3: 4,
                4: 1}
        return opts[direction]
    else:
        opts = {1: 4,
                2: 1,
                3: 2,
                4: 3}
        return opts[direction]


with open('1-input.txt') as txt:
    up = 0
    right = 0
    # 1 north, 2 east, 3 south, 4 weat
    direction = 1
    for line in txt:
        for allitem in parse(line):
            item = parseSet(allitem)
            direction = newDirection(direction, item[0])
            if direction == 1:
                up = up + item[1]
            else:
                if direction == 2:
                    right = right + item[1]
                else:
                    if direction == 3:
                        up = up - item[1]
                    else:
                        right = right - item[1]
    print(abs(up) + abs(right))
