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

with open('input.txt') as txt:
    count = 0
    for line in txt:
        items = parse(line)
        chars = items.group(1)
        num = int(items.group(2))
        check = items.group(3)
        charsList = list(filter(notDash, list(chars)))
        common = Counter(charsList).most_common(6)
        common.sort(compareTuples)
        charsListCount = list(map(listToCheck,common[0:5]))
        checkList = ''.join(charsListCount)
        if checkList == check:
            count = count + num
    print(count)
