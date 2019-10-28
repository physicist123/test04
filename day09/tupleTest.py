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

aList=[x*2 for x in range(10)]
print(aList)

freshfruit=['banana','loganberry','passion fruit']
list3=[]
for x in freshfruit:
    list3.append(x.strip())
print(list3)

aList4=list(map(lambda x:x.strip(),freshfruit))
print(aList4)

aList5=[-1,-4,6,7.5,-2.3,9,-11]
print(list(i for i in aList5 if i>5))

def printParam(first,*second,**third):
    print(str(first))
    print(second)
    print(third)

printParam("hello",1,3,5,a="haha",b="hehe")

bList=[1,3,5,7,9]
for i in bList:
    if i >=5:
        print(i*2)
    elif i<5:
        print(i)


