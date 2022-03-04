t1 = (1, 2, 3, 4, 5)
# t1[2] = 10 # ERROR Tuple is immutable

t1 = (1, 2, 3, [4, 5, 6], 7)
# t1[3] = 100 # ERROR
print("Before -- ",t1)
t1[3].append(100)
print("After -- ",t1)