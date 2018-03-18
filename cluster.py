import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

file = open('F:\\py3.6_workspace\\0127\\B_12_1.75_7outToPy.txt','r')

x = []
lines = file.readlines()
for line in lines:
	x.append([float(line.strip('\n').split(' ')[0]),float(line.strip('\n').split(' ')[1])])
# print(x)
# y = [float(line.strip('\n').split(' ')[1]) for line in lines]
clust = [int(line.strip('\n').split(' ')[2]) for line in lines]
# print(x, y, clust)
x= np.array(x)
# print(x,clust)
# plt.style.use("ggplot")
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif']=['SimHei']

colors = ['k','r','g','orange','b','sienna','k','m','darkviolet','peru']
markers = ['+','*','^','.','o','<','s','p','3','4']

def paint():
	for i in range(len(x)):
		plt.scatter(x[i,0], x[i,1], s=30, marker = markers[clust[i]], c=colors[clust[i]], alpha=0.5)
		print('')
	# if clust[i] == 1:
	# 	plt.scatter(x[i,0], x[i,1], s=30, marker='*', c='b', alpha=0.5)
	# if clust[i] == 2:
	# 	plt.scatter(x[i,0], x[i,1], s=30, marker='^', c='r', alpha=0.5)
	# if clust[i] == 3:
	# 	plt.scatter(x[i,0], x[i,1], s=30, marker='+', c='k', alpha=0.5)
	# if clust[i] == 4:
	# 	plt.scatter(x[i,0], x[i,1], s=30, marker='o', c='m', alpha=0.5)
	# if clust[i] == 5:
	# 	plt.scatter(x[i,0], x[i,1], s=30, marker='x', c='orange', alpha=0.5)
plt.xlim((-6, 6))
plt.ylim((-6, 6))
paint()
plt.xticks(np.linspace(-6,6,10,endpoint=True))
plt.yticks(np.linspace(-6,6,10,endpoint=True))
plt.savefig('B_12_1.75_7.svg',format='svg')
plt.show()