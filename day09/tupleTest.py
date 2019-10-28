#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/10/28 10:58 
# @Author : Alex
# @Site :  
# @File : tupleTest.py 
# @Software: PyCharm

mixed_tuple=(2,)
print(mixed_tuple)

tuple=(1,2,['a','b'])
print(str(tuple))

dict1={"a":1,"b":2,"c":'apple'}
for ele in dict1:
    print(ele)
    print(dict1[ele])

for item in dict1.items():
    print(item)

for key,elem in dict1.items():
    print(key,elem)