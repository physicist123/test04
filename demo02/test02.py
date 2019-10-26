

def say_hi():
    print("hi")
say_hi()

def sum(a,b):
    c=a+b
    print(c)
sum(20,30)

def say_hello():
    return "hello"
a=say_hello()
print(a)

def practice(str,times):
    b=str*times
    return b
c=practice("love ",4)
print(c)

for j in range(1,5):
    print(j,end=" ")