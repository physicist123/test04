
from sklearn.feature_extraction import DictVectorizer
v = DictVectorizer(sparse=False)
D = [{'foo': 1, 'bar': 2}, {'foo': 3, 'baz': 1}]
X = v.fit_transform(D)
print(X)
print(v.feature_names_)
    # array([[2., 0., 1.],
    #        [0., 1., 3.]])
    # >>> v.inverse_transform(X) == \
    #     [{'bar': 2.0, 'foo': 1.0}, {'baz': 1.0, 'foo': 3.0}]
    # True
    # >>> v.transform({'foo': 4, 'unseen_feature': 3})
    # array([[0., 0., 4.]])