
import pandas as pd
import numpy as np

obj=pd.Series(range(3),index=['a','b','c'])
print(obj)
obj2=obj.reindex(['c','a','b','f'])
print(obj)
obj3=obj.reindex(['c','a','b','f'],fill_value=0)
print(obj)
obj4=obj.reindex(['c','a','b','f'],method='ffill')
print(obj)

s1 = pd.Series(range(10, 20), index = range(10))
s2 = pd.Series(range(20, 25), index = range(5))
print(s1)
print(s2)
print(s1+s2)

