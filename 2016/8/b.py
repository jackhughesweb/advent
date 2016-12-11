import re

def createRectangle(state, width, height):
    for i in range(height):
        for j in range(width):
            state[i][j] = True
    return state

def rotateRow(state, y, by):
    while by > 0:
        last = state[y][len(state[y]) - 1]
        state[y][1:(len(state[y]))] = state[y][:(len(state[y]) - 1)]
        state[y][0] = last
        by = by - 1
    return state

def rotateColumn(state, x, by):
    while by > 0:
        last = state[len(state) - 1][x]
        for i in range(len(state) - 1, 0, -1):
            state[i][x] = state[i - 1][x]
        state[0][x] = last
        by = by - 1
    return state


def parseInstruction(txt, state):
    if re.match('rect [0-9]+x[0-9]+', txt):
        size = re.findall('rect ([0-9]+)x([0-9]+)', txt)
        width = int(size[0][0])
        height = int(size[0][1])
        return createRectangle(state, width, height)
    elif re.match('rotate column x=[0-9]+ by [0-9]+', txt):
        size = re.findall('rotate column x=([0-9]+) by ([0-9]+)', txt)
        x = int(size[0][0])
        by = int(size[0][1])
        return rotateColumn(state, x, by)
    elif re.match('rotate row y=[0-9]+ by [0-9]+', txt):
        size = re.findall('rotate row y=([0-9]+) by ([0-9]+)', txt)
        y = int(size[0][0])
        by = int(size[0][1])
        return rotateRow(state, y, by)
    else:
        print('Not found')

with open('input.txt') as txt:
    currentState = []
    for i in range(6):
        row = []
        for j in range(50):
            row += [False]
        currentState += [row]
    for line in txt:
        currentState = parseInstruction(line, currentState)
    count = 0
    for i in range(len(currentState)):
        row = ""
        for j in range(len(currentState[i])):
            if currentState[i][j]:
                count = count + 1
                row = row + "#"
            else:
                row = row + "."
        print(row)
