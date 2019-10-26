

import pandas as pd
import numpy as np

array = np.random.randn(2, 3)
print(array)

data = pd.DataFrame(array)
print(data)

dict_data = {'A': 1,
	             'B': pd.Timestamp('20170426'),
	             'C': pd.Series(1, index=list(range(4)),dtype='float32'),
	             'D': np.array([3] * 4,dtype='int32'),
	             'E': ["Python","Java","C++","C"],
	             'F': 'ITCast' }
#print dict_data
df_obj2 = pd.DataFrame(dict_data)
print(df_obj2)

print(df_obj2["E"])
df_obj2["apple"]=123
print(df_obj2)

del df_obj2["F"]
print(df_obj2)

ix_ = df_obj2.ix[:,"D"]
print(ix_)

dfl = pd.DataFrame(np.random.randn(5,4), columns=list('ABCD'),
                   index=pd.date_range('20130101',periods=5))

print(dfl)
print(dfl.loc['20130102':'20130104',"A":"C"])


