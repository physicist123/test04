#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/10/28 12:28 
# @Author : Alex
# @Site :  
# @File : whileTest.py 
# @Software: PyCharm

num=55

while True:
    inputNum=int(input("输入："))
    if inputNum==num:
        break
    elif inputNum>num:
        print("bigger")
        continue
    else:
        print("lower")
        continue
print("Bingo,You are right")

a_list = [0, 1, 2]

print("using continue:")
for i in a_list:
    if not i:
         continue
    print(i)

print("using pass:")
for i in a_list:
     if not i:
        pass
     print(i)
