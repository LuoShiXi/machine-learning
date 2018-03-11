import pandas as pd

file = 'F:\\py3.6_workspace\\0201_txt\\20140804_train_sort.csv'
#file_open = open("./20140804_train_sort.csv","r")
data = pd.read_csv(file)

newfile_01 = open("./20140804_89h_01.csv","w+")
newfile_01.truncate()

taxi_num = data.iloc[:,0]   #车号
taxi_lat = data.iloc[:,1]   #纬度
taxi_lng = data.iloc[:,2]   #经度
taxi_01 = data.iloc[:,3]    #载客状态：1为载客，0为无客
taxi_time = data.iloc[:,4]  #时间记录

#lines = file_open.readlines()

num=0 #数据点个数统计
i=j=1
for i in range(i,max(taxi_num)):
    for j in range(j,len(taxi_num)):
        if taxi_num[j]==i and\
            taxi_01[j]==1 and\
            taxi_num[j-1]==i and\
            taxi_01[j-1]==0:
##                print(lines[j])     #载客状态为0的数据
##                print(lines[j+1])   #一分钟内，载客状态变为1的数据
                
                #求出经纬度平均值,保留6位小数
                Lat = round((taxi_lat[j-1] + taxi_lat[j])/2 ,6) #纬度平均值
                Lng = round((taxi_lng[j-1] + taxi_lng[j])/2 ,6) #经度平均值
                print(Lat,Lng)
                
##                #用平均值替换原数据，保留6位小数
##                lt = lines[j+1].split(',')
##                lt[1] = str(round(Lat,6))
##                lt[2] = str(round(Lng,6))
##                lines[j+1]=",".join(lt)
##                print(lines[j+1])
                
                #经纬度（点）写入文件20140804_89h_01.csv
                newfile_01.write(str(Lat)+','+str(Lng)+'\n')
                num+=1
        elif taxi_num[j]>i:
            break
print(num)
#file_open.close()
newfile_01.close()
