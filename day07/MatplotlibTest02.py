
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)
# 在subplot上作图
x = np.arange(1, 100)
ax1.plot(x, x)
ax2.plot(x, -x)
ax3.plot(-x, x)
ax4.plot(-x, -x)
plt.show()



