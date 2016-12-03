import re

def parse(txt):
    return re.search('([0-9]+)(?:\s+)([0-9]+)(?:\s+)([0-9]+)', txt)

with open('input.txt') as txt:
    count = 0
    a = []
    b = []
    c = []
    for line in txt:
        items = parse(line)
        a = a + [int(items.group(1))]
        b = b + [int(items.group(2))]
        c = c + [int(items.group(3))]
        a.sort()
        b.sort()
        c.sort()
        if len(a) > 2:
            if a[2] < (a[0] + a[1]):
                count = count + 1
            if b[2] < (b[0] + b[1]):
                count = count + 1
            if c[2] < (c[0] + c[1]):
                count = count + 1
            a = []
            b = []
            c = []
    print(count)
