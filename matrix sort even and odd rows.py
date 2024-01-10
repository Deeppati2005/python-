# sort even  rows in asscending order and even rows in decening order
import random
l = []
for i in range(5):
    x = []
    for j in range(5):
        a = random.randint(1, 9)
        x.append(a)
    l.append(x)
c = 0
for i in l:
    if c % 2 == 0:
        i.sort()
    else:
        i.sort(reverse=True)
    print(i)
    c += 1
