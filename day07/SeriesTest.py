
import pandas as pd
import numpy as np

obj = pd.Series([4, -7, 3, 6])
print(obj)
print(obj.values)
print(obj.index)

obj2=pd.Series([4,7,-5,3],index=['d','b','a','c'])
print(obj2)

print("="*50)
obj=pd.Series(['c','a','d','a','a','b','b','c','c'])
unique=obj.unique()
print(unique)
print(obj.value_counts) #计算出现频率



