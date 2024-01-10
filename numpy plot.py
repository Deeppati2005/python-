import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1.0, 10, 0.1)
print(x)
a = np.cos(x)
b = np.sin(x)
plt.plot(x, a)
plt.plot(x, b)
plt.show()
