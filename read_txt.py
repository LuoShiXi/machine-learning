import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import math

file = open('F:\\py3.6_workspace\\0127\\sample80.txt','r')
lines = file.readlines()

x = [float(line.strip('\n').split(' ')[0]) for line in lines]
y = [float(line.strip('\n').split(' ')[1]) for line in lines]

# x.append(-6)
# x.append(6)
# y.append(-6)
# y.append(6)

cellrow = 10
cellcolumn = 10
interval = 12/cellrow # 步长

class Cell(object):
	def __init__(self, numPoints, effectCell, quatified, clusterNo):
		self.numPoints = numPoints 		# 点的个数
		self.effectCell = effectCell 	# 0/1值，标记是否为有效单元格，0表示无效
		self.quatified = quatified 		# 0/1值，判断密度是否达到阈值
		self.clusterNo = clusterNo 		# 所属类别01 0表示离散点

# 计算某个点所处单元格的位置编号
def loc_cell(x, y):
	return str(y * cellrow - (cellrow - x))

cells = {}
# 初始化每个单元格对象
for i in range(1,cellrow**2+1):
	cells[str(i)] = Cell(0,0,0,0)
# print(cells)

# 遍历每一个点，并得到该点所属单元格，并对所属单元格的点的个数加一
for num in range(len(x)):
	cell_x = math.ceil((x[num] - (-6))/interval)
	cell_y = math.ceil((y[num] - (-6))/interval)
	# print(cell_x, '-', cell_y)
	cells[loc_cell(cell_x,cell_y)].numPoints += 1

# 对单元格按点的个数按照矩阵形式输出,并提取出有效单元格
effectCell_num = 0 # 统计有效单元格得个数
end = ''
for i in range(1,cellrow+1):
	for j in range(1,cellcolumn+1):
		if j == cellrow:
			end = "\n\n"
		else:
			end = '   '
		print(''.join(str(cells[loc_cell(i,j)].numPoints)),end = end)
		if cells[loc_cell(i,j)].numPoints != 0:
			cells[loc_cell(i,j)].effectCell = 1 #有效单元格effectCell值置1
			effectCell_num += 1
		else:
			del cells[loc_cell(i,j)] # 删除无效单元格
print('有效单元格数目：', effectCell_num)

# print(cells)
# 对字典按照字典中每个对象的numPoints值进行升序排序
sort_cells = sorted(cells.items(), key = lambda dic:dic[1].numPoints)
# print(sort_cells)

# 取出所有有效单元格的点的个数，并组成list格式，转换为array类型
List = [cell_object[1].numPoints for cell_object in sort_cells]
print(List)
a = np.array((List))
print(a)
# 求二四分位数，即中位数%50 和 三四分位数%75

# 中位数所在位置
loc_q3 = math.ceil((effectCell_num + 1)/2)
q3 = math.ceil(np.median(a))
print('二四分位数所在位置为：',loc_q3,'二四分位数为：',q3)

# 三四分位数所在位置
loc_q4 = math.ceil((effectCell_num + 1)*3/4)
q4 = math.ceil(np.percentile(a, 75))
print('三四分位数所在位置为：',loc_q4,'三四分位数为：',q4)

m = 0 # 二四与三四之间点的个数总和
n = loc_q4 - loc_q3 + 1 # 点的个数在二四与三四之间的单元格的数目

for i in range(loc_q3, loc_q4):
	m += a[i+1]
print('二四与三四之间点的个数总和:', m,\
	'\n点的个数在二四与三四范围之间的单元格的数目：',n)
print('密度阈值：', m/n)
# print(a[loc_q3])
# print(a[loc_q4])
# print(a)






# print(x)
# print(y)



# print(max(x),max(y))
# print(min(x),min(y))

# plt.scatter(x, y, s=1, c='k', alpha=0.5)

# plt.xlim((-6,6))
# plt.ylim((-6,6))

# plt.xticks(np.linspace(-6,6,10,endpoint=True))
# plt.yticks(np.linspace(-6,6,10,endpoint=True))

# plt.show()