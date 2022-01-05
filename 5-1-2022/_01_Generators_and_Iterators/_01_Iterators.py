x = "My name is Meow"
iterobj = iter(x)

while True:
    try:
        print(next(iterobj))
    except StopIteration as stp:
        break


