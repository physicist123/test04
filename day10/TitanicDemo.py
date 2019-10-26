
import pandas as pd
import numpy as np
#1.获取数据
path="D:\\software\\PyCharm Community Edition 2019.2\\projects\\PythonProjects\\day10\\tantanic.txt"
data = pd.read_csv(path, sep=",")
#2.查看数据基本信息
print(data)
print(data.head(3))
print(data.describe())
print(data.info())
print(data.values)
#3.数据EDA
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# sns.catplot(x="sex", y="survived", hue="pclass", kind="bar", data=data)
# plt.show()
#4.特征工程
X = data[["pclass", "age", "sex"]]
y = data.survived
print(X.info())

# X["age"].fillna(value=X["age"].median(), inplace=True)
X["age"].fillna(X["age"].median(), inplace=True)
print(X.info())


from sklearn.model_selection import train_test_split

    # seed随机数种子---保证切分的结果的随机性
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=22)

from sklearn.feature_extraction import DictVectorizer, FeatureHasher

dv = DictVectorizer(sparse=False)
X_train_dv = dv.fit_transform(X_train.to_dict(orient="records"))
X_test_dv = dv.transform(X_test.to_dict(orient="records"))
print(X_train_dv)
print(dv.feature_names_)
#5.准备算法
from sklearn.ensemble import RandomForestClassifier,BaggingClassifier,AdaBoostClassifier
dtc = RandomForestClassifier()

# 6-超参数选择(网格搜索+交叉验证完成)
from sklearn.model_selection import GridSearchCV
# parameters = {'kernel': ('linear', 'rbf'), 'C': [1, 10]}
param_grid ={'criterion':("entropy","gini"),'max_depth':[10,20,30],"min_samples_split":[2,3,4,5],'min_samples_leaf':[1,2,3]}
cv = GridSearchCV(dtc,param_grid,cv=3)
cv.fit(X_train_dv,y_train)
print(cv.best_score_)
print(cv.best_params_)
# 0.8238095238095238
# {'criterion': 'entropy', 'max_depth': 10, 'min_samples_leaf': 3, 'min_samples_split': 2}
# 6-算法训练
print(dtc.fit(X_train_dv,y_train))
# 7-算法的检验
# model in trainset score is:0.86%
# model in testset score is:0.78%
print("model in trainset score is:%.2f%%"%(dtc.score(X_train_dv,y_train)))
print("model in testset score is:%.2f%%"%(dtc.score(X_test_dv,y_test)))
#7.预测
y_pred = dtc.predict(X_test_dv)
print(y_pred)

from sklearn.metrics import classification_report,confusion_matrix
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
#8.模型保存
# pd.to_pickle(dtc,"tatanic.pkl")
dtc_model = pd.read_pickle("tatanic.pkl")
y_test_pred = dtc_model.predict(X_test_dv)
print(y_test_pred)

df = pd.DataFrame(y_test_pred)
print(df)
# df.to_csv("tatinic.txt")
#9.模型可视化
from sklearn.tree import export_graphviz
# export_graphviz(dtc,out_file="tan.dot",filled=True,class_names=["no","yes"],feature_names=['age', 'pclass=1st', 'pclass=2nd', 'pclass=3rd', 'sex=female', 'sex=male'])
print(dtc.feature_importances_)
