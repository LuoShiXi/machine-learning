import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

file = 'F:\\py3.6_workspace\\0201_txt\\20140804__09_89h_01.csv'
data = pd.read_csv(file)

x = data.iloc[:,0]
y = data.iloc[:,1]
print(max(x),max(y))
print(min(x),min(y))

plt.scatter(x,y,s=4,c='k',alpha=0.5)
#以下语句为显示中文字符
zhfont1 = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\simsun.ttc')
plt.title('成都市交通散点图',fontproperties=zhfont1)

plt.xlim((min(x),max(x)))
plt.xticks(np.linspace(min(x),max(x),8,endpoint=True))
plt.xlabel('Latitude')
plt.ylim((min(y),max(y)))
plt.ylabel('Langitude')
plt.show()
##一天，8点到9点30分的数据
