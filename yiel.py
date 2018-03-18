import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import math


class Cell(object):
	def __init__(self, numPoints, effectCell, quatified, clusterNo):
		self.numPoints = numPoints 		# 点的个数
		self.effectCell = effectCell 	# 0/1值，标记是否为有效单元格，0表示无效
		self.quatified = quatified 		# 0/1值，判断密度是否达到阈值
		self.clusterNo = clusterNo 		# 所属类别01 0表示离散点

# 计算某个点所处单元格的位置编号
def loc_cell(x, y):
	return str(y * cellrow - (cellrow - x))

# 求有效单元格数量
def eff_cell_num():
	effect_num = 0
	
	# 遍历每一个点，并得到该点所属单元格，并对所属单元格的点的个数加一
	for num in range(len(x)):
		cell_x = math.ceil((x[num] - (-6))/interval)
		cell_y = math.ceil((y[num] - (-6))/interval)
		# print(cell_x, '-', cell_y)
		cells[loc_cell(cell_x,cell_y)].numPoints += 1

	# 对单元格按点的个数按照矩阵形式输出,并提取出有效单元格
	for i in range(1,cellrow+1):
		for j in range(1,cellcolumn+1):
			if cells[loc_cell(i,j)].numPoints != 0:
				cells[loc_cell(i,j)].effectCell = 1 #有效单元格effectCell值置1
				effect_num += 1
			else:
				del cells[loc_cell(i,j)] # 删除无效单元格
	return effect_num

# 求密度阈值
def density(no):
	# 对字典按照字典中每个对象的numPoints值进行升序排序
	sort_cells = sorted(cells.items(), key = lambda dic:dic[1].numPoints)

	# 取出所有有效单元格的点的个数，并组成list格式，转换为array类型
	List = [cell_object[1].numPoints for cell_object in sort_cells]
	a = np.array((List))
	print(a)
	# 求二四分位数，即中位数%50 和 三四分位数%75

	# 中位数所在位置
	loc_q2 = math.ceil((no + 1)/2)
	q3 = math.ceil(np.median(a))

	# 三四分位数所在位置
	loc_q3 = math.ceil((no + 1)*3/4)
	q4 = math.ceil(np.percentile(a, 75))

	m = 0 # 二四与三四之间点的个数总和
	n = loc_q3 - loc_q2 + 1 # 点的个数在二四与三四之间的单元格的数目
	for i in range(loc_q2, loc_q3):
		m += a[i+1]
	return(m/n)

if __name__ == '__main__':
	## 全局变量声明
	cellrow = 12
	cellcolumn = 12
	interval = 12/cellrow # 步长
	effectCell_num = 0 # 统计有效单元格数量
	cells = {} # 存储每个单元格对象

	file = open('F:\\py3.6_workspace\\0127\\sample80.txt','r')
	lines = file.readlines()
	x = [float(line.strip('\n').split(' ')[0]) for line in lines] #纬度
	y = [float(line.strip('\n').split(' ')[1]) for line in lines] #经度
	
	# 初始化每个单元格对象
	for i in range(1,cellrow**2+1):
		cells[str(i)] = Cell(0,0,0,0)

	effectCell_num = eff_cell_num()
	print('有效单元格数目：', effectCell_num)
	print('密度阈值：', density(effectCell_num))