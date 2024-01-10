import numpy as np
import matplotlib.pyplot as plt

x = ['c', 'c++', 'java', 'python']
y = [10, 9, 25, 22]
plt.pie(y, labels=x, autopct="%.2f%%")
plt.show()
