def gen(limit):
    for i in range(limit):
        if(i % 3 == 0):
            yield i 

x = gen(19)
print(x.__next__())
print(x.__next__())
for i in x:
    print(i) 