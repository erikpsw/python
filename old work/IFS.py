import random
import matplotlib.pyplot as plt

x = 0
y = 0
for n in range(1500):
    r = random.random()
    r = r * 100
    xn = x
    yn = y
    if r < 1:
        x = 0
        y = 0.16 * yn
    elif r < 86:
        x = 0.85 * xn + 0.04 * yn
        y = -0.04 * xn + 0.85 * yn + 1.6
    elif r < 93:
        x = 0.20 * xn - 0.26 * yn
        y = 0.23 * xn + 0.22 * yn + 1.6
    else:
        x = -0.15 * xn + 0.28 * yn
        y = 0.26 * xn + 0.24 * yn + 0.44
    plt.scatter(x, y,s=6,c='g',alpha=0.7)
plt.show()