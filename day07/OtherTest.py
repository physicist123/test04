

import numpy as np

zeros = np.zeros((3,4))
print(zeros)

arr = np.array([[1, 2, 1], [2, 3, 4]])
print(arr)

print(np.unique(arr))

#矩阵乘法
x=np.array([[1,2,3],[4,5,6]])
y=np.array([[6,23],[-1,7],[8,9]])
print(x)
print(y)
print(x.dot(y))
print(np.dot(x,y))

X=np.random.randn(5,5)
print(X)
print(X.T)

