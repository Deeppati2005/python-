# create a random matrix and caluclate each rows
import random
l = []
for i in range(5):
    x = []
    for j in range(5):
        a = random.randint(1, 9)
        x.append(a)
    l.append(x)
for i in l:
    s = 0
    for j in i:
        s = s+j
    print(i, "=", s)
