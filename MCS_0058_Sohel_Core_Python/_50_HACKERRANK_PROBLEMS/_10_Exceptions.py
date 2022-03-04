n = int(input())
inlist = []

for i in range(n):
    try:
        y = list(map(int, input().split()))
        print(y[0] // y[1])
    except ValueError as v:
        print("Error Code: {}".format(v))
    except TypeError as t:
        print("Error Code: {}".format(t))
    except ZeroDivisionError as z:
        print("Error Code: {}".format(z))
