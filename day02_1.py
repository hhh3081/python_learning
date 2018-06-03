# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 08:25:28 2018

@author: lenovo
"""
import json
import urllib.request as r 

print("欢迎使用全球天气app")
print("1.查看当前天气,2.查看其它城市天气,3.保存当前城市")

response = r.urlopen(url.format(city)).read().decode("utf-8","ignore")
menno = input("请输入菜单：")
if menno == "1":
    print("1.查看当前天气")
    city = input("please input city:")
    url = "http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric"
    w = json.loads(response)
    for i in range(0,40,8):
        description = w["list"][i]["weather"][0]["description"]
        pressure = w["list"][i]["main"]["pressure"]
        temp_max = w["list"][i]["main"]["temp_max"]
        dt_txt = w["list"][i]["dt_txt"]
        print("当前城市：{}\n天气情况：{}\n气压：{}\n最高温度：{}\n时间：{}".format(city,description,pressure,temp_max,dt_txt))
        print("*"*10)
if menno=="2":
    print("2.查看其它城市天气")
    
if menno=="3":
    print("3.保存当前城市")





