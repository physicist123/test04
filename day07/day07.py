
import numpy as np

randn = np.random.randint(0, 10,7)
print(randn)
print(type(randn))
print(randn.ndim)
print(randn.shape)
print(randn.dtype)

z=np.random.uniform(size = (3, 4)) # 'size='可省略，（0,1）之间的均匀分布
print(z)

rand1 = np.random.rand(2, 3)
print(rand1)

#5.产生高斯分布的样本值
k=np.random.normal(0,1,10)
#参数顺序：1.均值 2.标准差 3.生成多少样本
print(k)


