#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/10/28 14:06 
# @Author : Alex
# @Site :  
# @File : ExceptionTest.py 
# @Software: PyCharm


while True:
    try:
        x=int(input("num:"))
        break
    except ValueError:
        print("not valid value")