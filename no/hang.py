import re

f = open("./geoData.txt","r")
f1 = open("./geoData.csv","w+")
f1.truncate()

lines = f.readline()
print(lines)
data = lines.split(',')

i=0
for i in range(len(data)):
    newdata = data[i].replace(" ",',')
    print(newdata)
    f1.write(newdata+'\n')
f1.close()
f.close()
