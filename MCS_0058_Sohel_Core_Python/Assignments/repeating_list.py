A = list(range(1,11))
index = 2
count = 0
while(count < len(A)):
    if(index > (len(A)-1)):
        index = index % len(A)
        print(A[index])
        print("index = ",index)
    else:
        print(A[index])
        print("index = ",index)
    index += 3
    count += 1


