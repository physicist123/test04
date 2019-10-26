
from sklearn.datasets import load_digits
digits=load_digits()
print(digits.keys())
print(digits.DESCR)
print("--"*20)

X=digits.data
y=digits.target
print(X.shape)


a=122
b=122
print(id(122))
print(id(a))
print(id(b))

if __name__ == '__main__':
    print("hello")
    print("world")

