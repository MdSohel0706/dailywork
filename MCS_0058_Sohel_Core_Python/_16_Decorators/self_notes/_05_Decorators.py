#defining a decorator
def hello_decorator(func):
    #inner1 is wrapper function in which the argument is called
    #inner function can access outer local functions, which is func in this case

    def inner1():
        print("Hello, this is before function execution.")
        #calling the actual function now inside the wrapper function
        func()
        print("This is after function exectution.")

    return inner1

#defining a function to be called inside wrapper function
def function_to_be_used():
    print("This is inside the function.")

#passing the function_to_be_called inside the decorator function to modify its behaviour
function_to_be_used = hello_decorator(function_to_be_used)

#calling the function
function_to_be_used()

