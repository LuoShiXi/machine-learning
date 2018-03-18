import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# plt.style.use("ggplot")
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif']=['SimHei']
plt.figure(figsize=(8,6))
plt.grid(linestyle = "--")      #设置背景网格线为虚线

a = ([1,1,1,2,2.5,2.5,2.5,2.5,2.5,3,3,3,3,3,3,4,4,4,4,4,4,4,5,5,5,5,5,5,6,6,7,\
	1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,\
	3,3,4,4,5,5,5])
df = pd.DataFrame(a)
# print(df)

#用matplotlib来画出箱型图
plt.boxplot(x=df.values,whis=1.5,meanline=False)
# plt.savefig('box.svg',format='svg')
#建议保存为svg格式，再用inkscape转为矢量图emf后插入word中
plt.show()

#用pandas自带的画图工具更快
# df.boxplot()
# plt.show()
