
import numpy as np
import pandas as pd
path="D:\software\PyCharm Community Edition 2019.2\projects\PythonProjects\day07\SklearnTest.txt"
data = pd.read_csv(path)
print(data)
print(data.index)
print(data.values)
print(data.columns)

print(data.describe())
print(data.info())

print(data.query("is_date==-1"))
print(data.drop("is_date",axis=1))
