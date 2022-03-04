#passing a function as an argument

def add(a,b):
    return (a + b)

def concat(a,b):
    return (str(a) + str(b))

def calling_func(a,b,func):
    return func(a,b)

print(calling_func(2,3,add))
print(calling_func(2,3,concat))
