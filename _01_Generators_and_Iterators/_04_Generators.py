def gen_fib(limit):
    first = 0
    second = 1
    while(first < limit):
        third = first + second
        yield first
        first = second 
        second = third

for i in gen_fib(100):
    print(i)