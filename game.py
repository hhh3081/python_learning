# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 18:28:24 2018

@author: huhuide
"""
import time
print("""
      如果你为男性请输入F，女性请输入M
""")
sex = input("请输入性别：")



if sex=="M":
    print("""
      你觉得自己美丽吗？
      美丽，请输入 1
      不美丽， 请输入 2
""")
    a = input("请输入选项：")
    if a=="1":
        print("""
        满分十分，你给自己打几分      
        """)
        score = int(input("请输入分数："))
        if score >=10:
            print("哼！！")
            time.sleep(2)
            print("你的美已经超出了天际！！")
        if score >=9:
            print("哼！！")
            time.sleep(2)
            print("你真自恋！！")
            time.sleep(2)
            print("你是白痴加大笨蛋")
        elif score>=7:
            print("你真的很漂亮！！！")
            time.sleep(2)
            print("魔镜说你是天底下最美丽的女人!!")
            time.sleep(2)
            print("哈哈哈哈，it is a joke")
        else:
            print("你丑的让我紧闭双眼不敢睁开！！")
    else:
        print("不要气馁，不漂亮没关系，谁说一定要漂亮的！！")
        time.sleep(2)
        print("enenen.....")
        time.sleep(2)
        print("不美丽的人都很有才华！！！")
        time.sleep(2)
        print("我猜你一定是比你身边的人都优秀")
        time.sleep(2)
        print("it is a joke")
    input("仍然觉得自己美丽或者帅气的话请按enter")

if sex=="F":
    print("""
      你觉得自己帅气吗？
      帅气，请输入 1
      不帅气， 请输入 2
""")
    a = input("请输入选项：")
    if a=="1":
        print("""
        满分十分，你给自己打几分      
        """)
        score = int(input("请输入分数："))
        if score >=10:
            print("哼！！")
            time.sleep(2)
            print("你的帅气已经超出了天际！！")
        if score >=9:
            print("哼！！")
            time.sleep(2)
            print("你真自恋！！")
            time.sleep(2)
            print("你是白痴加大笨蛋")
        elif score>=7:
            print("你真的很帅气！！！")
            time.sleep(2)
            print("魔镜说你是天底下最帅气的人!!")
            time.sleep(2)
            print("哈哈哈哈，it is a joke")
        else:
            print("你丑的让我紧闭双眼不敢睁开！！")
    else:
        print("不要气馁，不帅没关系，谁说一定要帅的！！")
        time.sleep(2)
        print("enenen.....")
        time.sleep(2)
        print("不帅的人都很有才华！！！")
        time.sleep(2)
        print("我猜你一定是比你身边的人都优秀")
        time.sleep(2)
        print("it is a joke")

    input("仍然觉得自己美丽或者帅气的话请按enter")
