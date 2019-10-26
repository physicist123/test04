

def sayHello():
    print("hello baby")
    return "123"

def method1(a,b,c):
    print(a+b+c)

list=[1,2,3]
method1(*list)


g = lambda x,y:x+y
print(g(4,5))
if __name__ == '__main__':
    method1(10,10,10)
    # sayHello()
    info=sayHello()
    print(info)