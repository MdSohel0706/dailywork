def check_for_zerodivision(func):
    def inner(a,b):
        if(b == 0):
            print("Division not possible")
            return None
        else:
            print('*'*30)
            func(a,b)
            print('*'*30)

    return inner

@check_for_zerodivision
def divide(a,b):
    print(a/b)

divide(1020,0)