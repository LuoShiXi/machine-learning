import matplotlib.pyplot as plt
import numpy as np

# X = np.random.normal(1,2,20)
# Y = np.random.normal(2,3,20)

X = [np.random.uniform(0.7,2.2) for i in range(100)]
Y = [np.random.uniform(1.6,3.2) for i in range(100)]
# print(X)
X +=[2.6,3.5,3.4,2.5,0.5,3.2,2.7]
X +=[np.random.uniform(0,4) for i in range(30)]
Y +=[0.3,1.2,4.5,3.7,0.8,4.0,3.3]
Y +=[np.random.uniform(0,4) for i in range(30)]
# X = X.append([])
# Y = Y.append([0.3,1.2,4.5,3.7])
# T = np.arctan2(Y,X)#for color value

plt.grid() # == plt.grid(True)
plt.grid(color='b' , linewidth='0.3' ,linestyle='--')

plt.scatter(X,Y,s=10,c='k',alpha=0.5)
plt.xlim((0,4))
plt.ylim((0,4))
plt.xticks(np.linspace(0,4,5,endpoint=True))
plt.yticks(np.linspace(0,4,5,endpoint=True))
plt.savefig('compare_b.svg',format='svg')
plt.show()