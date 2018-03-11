import pandas as pd
import numpy as np

file = 'F:\\py3.6_workspace\\0201_txt\\20140804_train_8h.csv'

data = pd.DataFrame(pd.read_csv(file,header=None))
data.columns=['Num','Lat','Lng','Status','Time']#设置列名
print(data)

#根据车辆编号、时间记录进行排序
data = data.sort_values(by=['Num','Time'])

data.to_csv("F:/py3.6_workspace/0201_txt/20140804_train_sort.csv",
            sep=',',header=False,index=False)
