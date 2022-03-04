

# typing module
def get_data(in_data: str):   # def get_dat(int in_data):
    print("Data is : ", in_data + 'Welcome')

# get_data(100)  # ERROR
get_data("Hello World")
# get_data([1, 2, 3, 4, 5]) # ERROR

# Addition functionality : 1+2 = 3  1+2+3 = 6      10+20+30+40 = 100
# Adding numbers is a behavior
print("-----------*args for Method overloading-----------")
def get_data(*args):
    print(type(args), "   Data is : ", args)

get_data()   # ()
get_data(100)  # (100,)
get_data(100, 200)  # (100,200)
get_data(100, 200, 300)  # (100, 200, 300)
get_data(100, 200, 300, 400)
get_data(100, 200, 300, 400, 500)
get_data(100, 10.4, 'Hello', True, [1,2,3,4], ('a','b','c'), {1:1,2:2}, {1,2,3})

print("-----------**kwargs for Method overloading-----------")
def get_data(**kwargs):  # keyword arguments
    print(type(kwargs), "   Data is : ", kwargs)
get_data()  # {}
get_data(id=100)  # {'id'=100}
get_data(id=100, email='nettemmadhu@') # {id=100, email='nettemmadhu@'}
get_data(id=100, name='MadhuN', sal=20000)

'''
print(1+2+3)  #     def __add__(self, *args, **kwargs): # real signature unknown
      1+2+3+4
      1+2+3+4+5     
'''



def get_data(*in_list):
    print(type(in_list),in_list)
    sum = 0
    for each in in_list:
        for val in each:
            sum += val
    print("Final sum : ",sum)
get_data([1,2,3,4,5], [1,2,4,6,5], (4,3,2,2))