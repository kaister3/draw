import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 50)
y = np.sin(2 * x)

plt.plot(x, y, "y*-", label="y=sin(x)")
plt.plot(x, y * 2, "m--", label="y=2sin(x)")
plt.legend();

plt.title("sin(x) & 2sin(x)")

plt.xlim(0, 6)
plt.ylim(-3, 3)
plt.xticks((0, np.pi*0.5, np.pi*1.5, np.pi*2));

plt.xlabel("x")
plt.ylabel("y")

plt.show()