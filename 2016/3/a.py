import re

def parse(txt):
    return re.search('([0-9]+)(?:\s+)([0-9]+)(?:\s+)([0-9]+)', txt)

with open('input.txt') as txt:
    count = 0
    for line in txt:
        items = parse(line)
        n1 = int(items.group(1))
        n2 = int(items.group(2))
        n3 = int(items.group(3))
        a = sorted([n1, n2, n3])
        if a[2] < (a[0] + a[1]):
            count = count + 1
    print(count)
