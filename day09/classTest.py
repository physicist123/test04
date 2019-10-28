#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/10/28 14:34 
# @Author : Alex
# @Site :  
# @File : classTest.py 
# @Software: PyCharm

class Operation:
    def __init__(self,xnew,ynew):
        self.x=xnew
        self.y=ynew
    def add(self):
        return self.x+self.y

x=float(input("X:"))
y=float(input("Y:"))
obj=Operation(x,y)
print(obj.add())