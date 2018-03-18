import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

file = open('F:\\py3.6_workspace\\0127\\sample80.txt','r')

lines = file.readlines()

x = [float(line.strip('\n').split(' ')[0]) for line in lines]
y = [float(line.strip('\n').split(' ')[1]) for line in lines]

plt.xlim((-6, 6))
plt.ylim((-6, 6))
plt.scatter(x, y, s=30,\
	c='k', alpha=0.5)
plt.xticks(np.linspace(-6,6,10,endpoint=True),fontsize=12)
plt.yticks(np.linspace(-6,6,10,endpoint=True))
plt.savefig('Simple80.svg',format='svg')
plt.show()