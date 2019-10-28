
import pandas as pd

data = pd.read_csv("buy.csv",sep=",")
print(data)
#2.数据进行简单的探索性分析
print(data.head(3))
print(data.info())
print(data.describe())
print(data.columns)

print("==================")
X=data.drop("Class:buy_computer",axis=1)
y=data["Class:buy_computer"]
print(X)
print(y)

print("=============================================================")
from  sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=22,test_size=0.2)
print(X_train)
print("=================")
print(X_test)

#4.使用训练集训练模型
from sklearn.tree import DecisionTreeClassifier
dtc=DecisionTreeClassifier(criterion='entropy')
print(dtc.fit(X_train,y_train))

#5.使用模型进行预测
y_pred=dtc.predict(X_test)
#6.使用测试集测试模型情况
print("model in trainset score is:%.2f%%"%(dtc.score(X_train,y_train)))
print("model in testset score is:%.2f%%"%(dtc.score(X_test,y_test)))

#混淆矩阵
from  sklearn.metrics import confusion_matrix
print(confusion_matrix(y_true=y_test,y_pred=y_pred))

#7.保存模型
from   sklearn.externals import joblib
joblib.dump(dtc,"buyDataSet.dot")




