import re
import pandas as pd
import numpy as np

###接下来对数据进行初步排序，按照车号和时间两个条件进行排序，定义一个排序函数
def sortdata():
    file = 'F:\\py3.6_workspace\\0201_txt\\20140804__09_train_8h.csv'
    data = pd.DataFrame(pd.read_csv(file,header=None))
    data.columns=['Num','Lat','Lng','Status','Time']#设置列名
    #print(data)
    #根据车辆编号、时间记录进行排序
    data = data.sort_values(by=['Num','Time'])

    data.to_csv("F:/py3.6_workspace/0201_txt/20140804__09_train_sort.csv",
            sep=',',header=False,index=False)


###排序完成，现在对数据进行提取得到载客状态由0变为1的两天数据，并进一步对经纬度取平均值得到最终的数据
def final_01():
    file = 'F:\\py3.6_workspace\\0201_txt\\20140804__09_train_sort.csv'
    data = pd.read_csv(file)
    #lines = open(file,'r').readline()
    
    newfile_01 = open("./20140804__09_89h_01.csv","w+")
    newfile_01.truncate()
    
    taxi_num = data.iloc[:,0]   #车号
    taxi_lat = data.iloc[:,1]   #纬度
    taxi_lng = data.iloc[:,2]   #经度
    taxi_01 = data.iloc[:,3]    #载客状态：1为载客，0为无客
    taxi_time = data.iloc[:,4]  #时间记录
    num=0 #数据点个数统计
    i=j=1
    for i in range(i,max(taxi_num)):
        for j in range(j,len(taxi_num)):
            if taxi_num[j]==i and\
                taxi_01[j]==1 and\
                taxi_num[j-1]==i and\
                taxi_01[j-1]==0:
                
                #print(lines[j])     #载客状态为0的数据
                #print(lines[j+1])   #一分钟内，载客状态变为1的数据
                    
                #求出经纬度平均值,保留6位小数
                Lat = round((taxi_lat[j-1] + taxi_lat[j])/2 ,6) #纬度平均值
                Lng = round((taxi_lng[j-1] + taxi_lng[j])/2 ,6) #经度平均值
                #print(Lat,Lng)

                newfile_01.write(str(Lat)+','+str(Lng)+'\n')
                num+=1
            elif taxi_num[j]>i:
                break
    print(num)
    newfile_01.close()

if __name__ == '__main__':
    f1 = open("./20140804__09_train_8h.csv", "w+")
    f1.truncate()
    #清空文件内容
    #注意：仅当以"r+" "rb+" "w" "wb" "wb+"
    #等以可写模式打开的文件才可以执行该功能。

    for i in range(4,9):
        file_path = "./data/2014080"+str(i)+"_train.txt"
        f = open(file_path,"r")
        #j用来统计点数
        j=0
        for n in range((10**6)*5):
            lines = f.readline()
            if i==7:
                match = re.search(r'/14\ '+'(08:.)|(09:(([0-2]\d{1}.)|30:00))', lines)
            else:
                match = re.search(r'/'+str(i)+'\ '+'(08:.)|(09:(([0-2]\d{1}.)|30:00))', lines)
            if match:
                #print(lines)
                f1.write(lines)
                j=j+1
        f.close()
        print(file_path+'共有',j,'个点')
    f1.close()

    
    ##调用sort_data()函数，进行初步排序
    sortdata()

    
    ##调用final_01()函数，得到0_1状态数据，并平均经纬度值得到最后数据
    final_01()
###END
