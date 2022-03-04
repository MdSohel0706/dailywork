def recfib(n):
    if(n<=1):
        return n
    else:
        return (recfib(n-1) + recfib(n-2))

k = int(input("Enter no of terms : "))
for i in range(1,(k+1)):
    print(recfib(i))

