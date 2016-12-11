import re

def getPalindromes(txt):
    chars = list(txt)
    returnList = []
    if len(chars) < 3:
        return False
    for i in range(0, len(chars) - 2):
        if chars[i] == chars[i+2] and not chars[i] == chars[i+1]:
            returnList += [chars[i] + chars[i+1] + chars[i+2]]
    return returnList

def swapPalindrome(txt):
    chars = list(txt)
    return chars[1] + chars[0] + chars[1]

def isValid(txt):
    pattern = re.compile(r'\[([^\]]+)\]')
    ps = getPalindromes(pattern.sub('.', txt))
    for outerPal in ps:
        for inner in pattern.findall(txt):
            if swapPalindrome(outerPal) in inner:
                return True
    return False

with open('input.txt') as txt:
    count = 0
    for line in txt:
        if isValid(line):
            count = count + 1
    print(count)
