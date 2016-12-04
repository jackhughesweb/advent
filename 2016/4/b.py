import re
from collections import Counter

def parse(txt):
    return re.search('((?:[A-z]+-)+)([0-9]+)\[([A-z]+)\]', txt)

def notDash(txt):
    return not txt == '-'

def listToCheck((a,b)):
    return a

def compareTuples(a, b):
    if a[1] > b[1]:
        return -1
    else:
        if a[1] == b[1]:
            if a[0] > b[0]:
                return 1
            else:
                return -1
        else:
            return 1

def removeDecoy(chars, check):
    charsList = list(filter(notDash, chars))
    common = Counter(charsList).most_common(6)
    common.sort(compareTuples)
    charsListCount = list(map(listToCheck,common[0:5]))
    checkList = ''.join(charsListCount)
    return checkList == check


def caeserMap(char):
    opts = {'a': 'b',
            'b': 'c',
            'c': 'd',
            'd': 'e',
            'e': 'f',
            'f': 'g',
            'g': 'h',
            'h': 'i',
            'i': 'j',
            'j': 'k',
            'k': 'l',
            'l': 'm',
            'm': 'n',
            'n': 'o',
            'o': 'p',
            'p': 'q',
            'q': 'r',
            'r': 's',
            's': 't',
            't': 'u',
            'u': 'v',
            'v': 'w',
            'w': 'x',
            'x': 'y',
            'y': 'z',
            'z': 'a'}
    try:
        return opts[char]
    except KeyError:
        return '-'

def caeserShift(str, shift):
    strList = list(str)
    for a in range(0,shift):
        strList = map(caeserMap, strList)
    return ''.join(strList)

def decode(chars):
    for a in range(0,26):
        if 'north' in caeserShift(chars, a):
            return True
    return False

with open('input.txt') as txt:
    for line in txt:
        items = parse(line)
        chars = items.group(1)
        num = int(items.group(2))
        check = items.group(3)
        charsList = list(chars)
        if removeDecoy(charsList, check):
            if decode(chars):
                print(num)
