#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/10/28 15:49 
# @Author : Alex
# @Site :  
# @File : numpyTest.py 
# @Software: PyCharm

import numpy as np
x=np.random.randint(0,10,size=(1,10))

print(x)
print(x.dtype)
print(x.ndim)

y=np.random.randint(0,10,7)
print(y)

z=np.random.uniform(0,1,size=(3,4))
print(z)

t=np.random.rand(3,4)
print(t)

s=np.random.binomial(10,.5,50)
print(s)

k=np.random.normal(0,1,10)
print(k)

s=np.random.chisquare(2,size=(2,3))
print(s)

