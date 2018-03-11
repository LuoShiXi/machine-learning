import re

match = re.search(r"3 (?P<date>.+)",
                  "4,30.631682,104.076166,0,2014/8/3 08:37:40")
try:
    print(match.group('date'))
except:
    print("Erro")
    
#i = match.group('date')
#i = int(i)
#print(i)

#date = [1,5,9,0]
#date.append(i)

#print(sorted(date))
