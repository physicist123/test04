
import numpy as np
import numpy.linalg as la

data = [
    [1,2,3],
    [2,3,4]
]
U,sigma,VT=la.svd(data)
print(U)
print(sigma)
print(VT)