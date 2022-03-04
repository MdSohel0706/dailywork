def sum(a,b = 10):
    print(a+b)

sum(5)

def fun(b, *arguments):
    print(arguments)
    print("b = ",b)

fun(1,2,3,4,5)

def fun2(a,**kwargs):
    print(kwargs)
    print("a = ",a)

fun2(20,b = "Firstname", c = "Lastname")