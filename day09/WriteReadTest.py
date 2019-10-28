#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/10/28 13:56 
# @Author : Alex
# @Site :  
# @File : WriteReadTest.py 
# @Software: PyCharm

sentence="""\
I love learning python
because python is fun
and also easy to use
"""
f=open('sentences.txt','w')
f.write(sentence)
f.close()

f=open('sentences.txt')
while True:
    line=f.readline()
    if len(line)==0:
        break
    print(line)
f.close()