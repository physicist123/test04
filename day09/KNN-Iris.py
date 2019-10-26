#-*-coding:utf8-*-
#1.准备数据集
from sklearn.datasets import load_iris
#2.使用加载读取数据存入一个变量中
iris=load_iris()
#3.查验数据规模
print (iris.data.shape) #(150L, 4L)
#4.数据集说明查看
print (iris.DESCR)
#5.切分数据集
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test =train_test_split(iris.data,iris.target,
                                                   test_size=0.25,random_state=33)

from sklearn.datasets import load_iris
iris=load_iris()
print(iris.data.shape)#(150, 4)

from sklearn.cross_decomposition import train_test_split

X_train,X_test,y_train,y_test=train_test_split(iris.data,iris.target,test_size=0.25,random_state=33)
print(X_train.shape,X_test.shape)