# create a 3x3 matrix with some random values and transpose it
import random
m = [[random.randint(10, 50) for j in range(3)] for i in range(3)]
for i in m:
    print(i)
y = [[0 for i in range(3)] for j in range(3)]
for i in range(3):
    for j in range(3):
        y[i][j] = m[j][i]
print("Transpose:")
for i in y:
    print(i)
