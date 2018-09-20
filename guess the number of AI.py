#guess the number of AI
#会玩猜数字的AI
 
from random import randint
import time


def ai(num):

   h=randint(1,c*2)

   def guessing(g,mi,mm):
      print("%d?"%g)
      time.sleep(0.4)
      if g > num:
         print("太大了！")
         mm=g
         g=mi+(g-mi)//2
         time.sleep(0.4)
         guessing(g,mi,mm)
      elif g < num:
         print("太小了！")
         mi=g
         g=g+(mm-g)//2
         time.sleep(0.4)
         guessing(g,mi,mm)
      else:
         print("恭喜你猜对了！")
         return
      
   guessing(h,0,c*2)

print("************************")
print("*这是一个会玩猜数字的AI*")
print("************************\n")


c=input("请输入要猜的数值：")


while True:
   try:
      c=int(c)
      break
   except ValueError:
      c=input("请输入数字:")
time.sleep(0.4)
ai(c)
