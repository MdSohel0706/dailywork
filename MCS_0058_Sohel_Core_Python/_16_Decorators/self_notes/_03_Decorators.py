# Python program to illustrate functions
# Functions can return another function

def create_adder(x):
    def adder(y):
        return (x+y)

    return adder

add15 = create_adder(15)
print(add15(10))

'''
In the above example, we have created a function inside of another function and then have returned the function created inside.
The above three examples depict the important concepts that are needed to understand decorators. 
After going through them let us now dive deep into decorators. 
'''

