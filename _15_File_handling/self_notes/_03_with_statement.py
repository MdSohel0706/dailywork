'''
The with statement can be used while opening a file.

advantage: it will take care of closing file which is opened by it

Hence we need not to close the file explicity.

In case of exception also, 'with statement' will close the file before the exception
handled.
'''
# with statement to open a file and write data
with open('sample.txt', 'w') as f:
    f.write('I am attending the session\n')
    f.write('python is attractive\n')


"""# with statement to open a file and read data
with open('sample.txt', 'r') as data:
    for line in data:
        print('line')

# with statement to open a file and append update purpose
with open('sample.txt',"a") as f:
    f.write("well come to python")"""

"""f = open('sample.txt', 'r') #
s = f.read()
print(s)

name = open("sample.txt","w")
obj = name.write("suma priya")
print(obj)"""

with open("jpg","wb") as f:
    f.write("img.jpg")












