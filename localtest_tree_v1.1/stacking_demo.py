#!/usr/bin/env python
# -*- coding: utf-8 -*-
# file: stacking_demo.py

#参照：https://www.jianshu.com/p/7fc9aa03ec11

from sklearn import datasets
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
iris = datasets.load_iris()
# 特征
iris_feature = iris.data
# 分类标签
iris_label = iris.target
iris_target_name=iris['target_names']
feature_names = iris['feature_names']
# 划分
X_train, X_test, Y_train, Y_test = train_test_split(iris_feature, iris_label, test_size=0.3, random_state=42)


from mlxtend.feature_selection import ColumnSelector
from sklearn.pipeline import make_pipeline
from sklearn.ensemble import ExtraTreesClassifier
from xgboost import XGBClassifier
import lightgbm
from sklearn.ensemble import AdaBoostClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import RandomForestClassifier
from mlxtend.classifier import StackingClassifier
import numpy as np

#初级学习器
clf1 = GradientBoostingClassifier()
clf2 = RandomForestClassifier()


sclf = StackingClassifier(classifiers=[clf1,clf2],
                              # use_probas=True, #类别概率值作为meta-classfier的输入
                              # average_probas=False,  是否对每一个类别产生的概率值做平均
                          meta_classifier=LogisticRegression())

sclf.fit(X_train, Y_train)
Y_pred = sclf.predict(X_test)
print("预测结果集：",Y_pred)

