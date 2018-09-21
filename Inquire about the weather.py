# -*- coding: utf-8 -*-
#Inquire about the weather
#查询天气
 
from urllib import request
from city import city
import json

with request.urlopen('http://www.baidu.com') as f:
    web=f.read()

cityname = input("你想查询哪个城市的天气?\n")
citycode =city.get(cityname)

if citycode:
    url=('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode)
    content=request.urlopen(url).read()
    date = json.loads(content)
    result=date['weatherinfo']
    str_temp=("%s\n%s~%s"%(result['weather'],result['temp1'],result['temp2']))
    print(str_temp)
else:
    print("没有找到该城市")
