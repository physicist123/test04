
import numpy as np

#导入数据
from sklearn.datasets import load_boston
boston=load_boston()
print(boston.DESCR)

X=boston.data
y=boston.target

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=33)

print(np.max(boston.target))
print(np.mean(boston.target))
#特征工程
#对特征列和结果列进行标准化处理
from sklearn.preprocessing import StandardScaler
ss_X=StandardScaler()
ss_y=StandardScaler()

X_train=ss_X.fit_transform(X_train)
X_test=ss_X.transform(X_test)

y_train=ss_y.fit_transform(y_train)
y_test=ss_y.transform(y_test)

from sklearn.tree import DecisionTreeRegressor
dtr=DecisionTreeRegressor()
dtr.fit(X_train,y_train)
y_predict=dtr.predict(X_test)
print(dtr.score(X_test,y_test))




