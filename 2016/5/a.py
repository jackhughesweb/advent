import hashlib

def isNextPass(txt):
    return txt[:5] == '00000'

def getNextLetter(txt, index):
    currentIndex = index
    m = hashlib.md5()
    m.update((txt + str(currentIndex)))
    dig = m.hexdigest()
    while not isNextPass(dig):
        currentIndex = currentIndex + 1
        m = hashlib.md5()
        m.update((txt + str(currentIndex)))
        dig = m.hexdigest()
    return [currentIndex, dig[5:6]]
    
with open('input.txt') as txt:
    for currentLine in txt:
        line = currentLine.rstrip()
        password = ''
        i = 0
        while len(password) < 8:
            (newindex, p) = getNextLetter(line, i)
            i = newindex + 1
            password = password + p
        print(password)
