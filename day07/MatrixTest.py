
import numpy as np
a=np.mat("1 2;3 4")
print(a)

x2=np.matrix("1 2;3 4")
print(x2)
x3=np.matrix("1,2;3,4")
print(x3)

x4 = np.matrix([1, 2, 3])
print(x4)

randn = np.random.randn(2, 3)
print(randn)
print(np.ceil(randn))
print(np.multiply(randn, randn))
