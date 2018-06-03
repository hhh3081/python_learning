# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 16:35:51 2018

@author: lenovo
"""
import urllib.request as req
import json

city = input("请输入拼音:")
#print(city)

url='http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'.format(city)
#print(url)

print("欢迎使用全球天气app")
print("1.查看当前天气,2.查看其它城市天气,3.保存当前城市")
menno = input("请输入菜单：")
if menno=="1":
    print("1.查看当前天气")
    
if menno=="2":
    print("2.查看其它城市天气")
    
if menno=="3":
    print("3.保存当前城市")

response = req.urlopen(url).read().decode("utf-8",'ignore')
#print(response)
data = json.loads(response)
#print(data)

weather=data['weather'][0]['description']
tem_max=data['main']['temp_max']
pressure=data['main']['pressure']
print("当前的城市是:{}\n天气:{}\n最高温度:{}\n气压:{}".format(city,weather,tem_max,pressure))
