def addition(*args):
    return sum(args)

def multiplication(*args):
    result = 1
    for i in args:
        result = result * i
    return result

def subtraction(a,b):
    result = a - b
    return result

def division(a,b):
    result = a / b
    return result
