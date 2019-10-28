#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/10/28 16:14 
# @Author : Alex
# @Site :  
# @File : numpyTest2.py 
# @Software: PyCharm

import numpy as np

arr=np.random.rand(3,4)
print(arr)
print(type(arr))

arr = np.random.randint(-1, 5, size = (3, 4)) # 'size='可省略
print(arr)
print(type(arr))

list=range(10)
arr=np.array(list)
print(arr)
print(arr.dtype)
print(arr.ndim)
print(arr.shape)

lis_lis=[range(10),range(10)]
arr=np.array(lis_lis)
print(arr)
print(arr.shape)
print(arr.ndim)
print(arr.dtype)

# np.zeros
zeros_arr = np.zeros((3, 4))

# np.ones
ones_arr = np.ones((2, 3))

# np.empty
empty_arr = np.empty((3, 3))


# np.empty 指定数据类型
empty_int_arr = np.empty((3, 3), int)

print('------zeros_arr-------')
print(zeros_arr)
print(empty_int_arr)
print(empty_arr)


