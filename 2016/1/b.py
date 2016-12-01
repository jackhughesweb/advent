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
        
def getNextCoords(current, direction, length):
    coords = []
    newCurrent = current
    mask = {1: (1,0),
            2: (0,1),
            3: (-1,0),
            4: (0,-1)}
    currentMask = mask[direction]
    for i in range(1,length+1):
        newCurrent = (newCurrent[0] + currentMask[0], newCurrent[1] + currentMask[1])
        coords = coords + [newCurrent]
    return [newCurrent, coords]
    
def getFirstMatch(coords):
    lowestindex = 1000000
    result = 1000000
    for index1, i in enumerate(coords):
        for index2, j in enumerate(coords):
            if i[0] == j[0] and i[1] == j[1]:
                if index2 < lowestindex and index2 > index1:
                    result = abs(i[0]) + abs(i[1])
                    lowestindex = index2
    return result


with open('input.txt') as txt:
    up = 0
    right = 0
    # 1 north, 2 east, 3 south, 4 weat
    direction = 1
    current = (0,0)
    coords = [(0,0)]
    for line in txt:
        for allitem in parse(line):
            item = parseSet(allitem)
            direction = newDirection(direction, item[0])
            nC = getNextCoords(current, direction, item[1])
            current = nC[0]
            coords = coords + nC[1]
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
    print(getFirstMatch(coords))
