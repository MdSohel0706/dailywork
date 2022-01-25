import itertools as it

counter = it.count()
print(next(counter))
print(next(counter))
print(next(counter))

print("*"*30)

counter = it.count(start = 5, step = -2.4)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

print("*"*30)

counter = it.count() 
lst = [100,200,300,400,500]
enout = list(zip(counter,lst))
print(enout)

print("*"*30)

enout = list(zip(range(10),lst))
print(enout)

print("*"*30)
enout = list(it.zip_longest(range(10),lst))
print(enout)

print("*"*30)

lst = [1,2,3]
counter = it.cycle(lst)
for i in range(10):
    print(next(counter))

print("*"*30)

counter = it.repeat(100, times = 3)
print(next(counter))
print(next(counter))
print(next(counter)) # throws StopIteration error if we use next(counter) more than times

print("*"*30)

squares = map(pow, range(10), it.repeat(2))
print(list(squares))

print("*"*30)

squares = it.starmap(pow, [(1,2),(2,3),(3,5),(4,2)])
print(list(squares))

print("*"*30)



