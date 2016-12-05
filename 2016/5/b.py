import hashlib

def isNextPass(txt):
    return txt[:5] == '00000' and txt[5:6].isdigit()

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
    return [currentIndex, int(dig[5:6]), dig[6:7]]

def placeInHash(hash, index, char):
    try:
        a = hash[index]
        if a == None:
            hash[index] = char
            return hash
        else:
            return hash
    except IndexError as e:
        return hash

def hashFilled(hash):
    return not None in hash

with open('input.txt') as txt:
    for currentLine in txt:
        line = currentLine.rstrip()
        password = [None, None, None, None, None, None, None, None]
        i = 0
        while not hashFilled(password):
            (newindex, d, p) = getNextLetter(line, i)
            i = newindex + 1
            password = placeInHash(password, d, p)
        print(''.join(password))
