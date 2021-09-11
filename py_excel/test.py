import matplotlib.pyplot as plt
import numpy as np
import math
x=[1,2,3,4,5,6,7,8,9,10]
y=np.array([math.sin(j) for j in x])

fig, axs = plt.subplots(2)
fig.suptitle('Vertically stacked subplots')
axs[0].plot(x, y)
axs[0].annotate("h=1",xy=[x[0],x[0]])
axs[0].text(x[0],y[0],"ttt")
axs[1].plot(x, -y)
plt.xlabel("Delay(ms)")
plt.ylabel("ALM")
plt.show()