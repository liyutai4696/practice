#File processing
#文件处理1-计算分数
import os

f = open('scores.txt','r',encoding='UTF-8')

lines=f.readlines()
f.close

results=[]

for line in lines:
   date=line.split()

   sum = 0

   for s in date[1:]:
      sum+=int(s)
      
   result = '%s\t:%d\n'%(date[0],sum)
   results.append(result)

print(results)
output = open('result.txt','w',encoding='UTF-8')
output.writelines(results)
output.close()
