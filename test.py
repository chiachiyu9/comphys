import numpy as np
import matplotlib.pyplot as plt
#2024.03.04 from github

x = np.linspace(0, 1, 100)
y = np.sin(x)

plt.figure(1)
plt.plot(x, y)

plt.figure(2)
plt.plot(y,x)

plt.show()


