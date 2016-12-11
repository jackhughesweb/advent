from collections import Counter

with open('input.txt') as txt:
    counters = []
    for line in txt:
        for index, char in enumerate(list(line.rstrip())):
            while index >= len(counters):
                counters = counters + [Counter()]
            counters[index].update(char)
    string = ''
    for counter in counters:
        string += counter.most_common(1)[0][0]
    print(string)
