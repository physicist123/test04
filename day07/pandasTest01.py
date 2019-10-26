
import pandas as pd

series = pd.Series(range(10))
print(series)
print(series.ndim)
print(series.index)
print(series.values)
print(type(series))

print(series.tail())

print(series[2])

dic = {2001: 17.8, 2002: 20.1, 2003: 16.5}
data = pd.Series(dic)
print(data)

print(type(data))
print(data.index)
print(data.values)

data.name="456"
data.index.name="123"
print("=="*20)
print(data)
print(data.name)
print(data.index.name)