import re

def containsPalindrome(txt):
    chars = list(txt)
    if len(chars) < 4:
        return False
    for i in range(0, len(chars) - 3):
        if chars[i] == chars[i+3] and chars[i+1] == chars[i+2] and not chars[i] == chars[i+1]:
            return True
    return False

def isValid(txt):
    pattern = re.compile(r'\[([^\]]+)\]')
    for item in pattern.findall(txt):
        if containsPalindrome(item):
            return False
    return containsPalindrome(pattern.sub('.', txt))

with open('input.txt') as txt:
    count = 0
    for line in txt:
        if isValid(line):
            count = count + 1
    print(count)
