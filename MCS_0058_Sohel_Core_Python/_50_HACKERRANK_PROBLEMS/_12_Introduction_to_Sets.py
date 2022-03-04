array = {161,182,161,154, 176,170,167,171,170,174}

def average(array):
    sum = 0
    array = set(array)
    n = len(array)
    for num in array:
        sum += num
    avg = sum/n
    out = round(avg,3)
    return out
    

out = average(array)
print(out)