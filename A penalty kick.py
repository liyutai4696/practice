#A penalty kick
#点球大战
 
from random import randint
import time

print("**********")
print("*点球大战*")
print("**********\n")


fx=['左','中','右']

rl=0
ai=0

lc=0

while True:

   lc+=1
   if lc%2:
      l=lc//2+1
      print("第%d轮" % l)
   if lc%2 :
      print("人类进攻!")
      xz=input("请选择进攻方向:(左边|中间|右边)")

      while True:
         if xz in[None,'']:
            xz=input("请选择正确的进攻方向:(左边|中间|右边)")
         elif xz[0] in fx:
            break
         else:
            xz=input("请选择正确的进攻方向:(左边|中间|右边)")

      
      fs=fx[randint(0,2)]
      if xz[0]!=fs:
         rl+=1
   else:
      print("AI进攻!")
      fs=fx[randint(0,2)]
      xz=input("请选择防守方向:(左边|中间|右边)")
      
      while True:
         if xz in[None,'']:
            xz=input("请选择正确的防守方向:(左边|中间|右边)")
         elif xz[0] in fx:
            break
         else:
            xz=input("请选择正确的防守方向:(左边|中间|右边)")
      

      if xz[0]!=fs:
         ai+=1

   print("现在的得分是:人类 %d VS %d AI" % (rl,ai))
   
   if (lc/2)>=5:
      if rl>ai:
         print("人类获胜!")
         break
      elif ai>rl:
         print("AI获胜!")
         break
