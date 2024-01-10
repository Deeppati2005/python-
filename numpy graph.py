import numpy as np
import matplotlib.pyplot as plt

x = ['c', 'c++', 'java', 'python']
y = [10, 9, 25, 22]
a = np.arange(len(y))
plt.bar(x, y, color=['r', 'g', 'black', 'y'])
plt.show()
