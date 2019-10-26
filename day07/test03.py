
import numpy as np
import pandas as pd

df_obj = pd.DataFrame(np.random.randn(5,4), columns = ['a', 'b', 'c', 'd'])
print(df_obj)
print(df_obj.sum())

print(df_obj.max())
print(df_obj.max(axis=1))

print(df_obj.min(axis=1, skipna=False))#按行填充，NA值自动排除
print(df_obj.describe())
print(df_obj.info())

