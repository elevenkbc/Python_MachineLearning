import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-3, 3.5, 0.5)
y = [var1**2 for var1 in x]
z = [var2 *2 for var2 in x]

fig = plt.figure(1)

ax = fig.add_subplot(211)
line1 = ax.plot(x, y, 'ro-')

ax = fig.add_subplot(212)
line2 = ax.plot(x, z, 'g-')

plt.show()
