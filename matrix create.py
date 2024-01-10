# create a random matrix of size 5x5 with some random values
import random
l = []
for i in range(5):
    x = []
    for j in range(5):
        a = random.randint(1, 9)
        x.append(a)
    l.append(x)
print(l)
