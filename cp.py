l = [1, 2, 5, 7, 8, 10, 12, 20, 25]
t = 15
low = 0
high = len(l)-1
while (low <= high):
    if (l[low]+l[high] > t):
        high = high-1
    elif (l[low]+l[high] < t):
        low = low+1
    else:
        print(" ", l[low], " ", l[high])
        low = low+1
        high = high-1
