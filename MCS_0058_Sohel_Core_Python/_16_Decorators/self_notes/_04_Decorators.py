@gfg_decorator
def hello_decorator():
    print("Gfg")

'''
The above code is equivalent to :

def hello_decorator():
    print("Gfg")
    
hello_decorator = gfg_decorator(hello_decorator)
'''


