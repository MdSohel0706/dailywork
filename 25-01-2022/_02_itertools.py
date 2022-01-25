import itertools as it

str1 = 'abcd'
combs = it.combinations(str1,2)
for comb in combs:
    print("".join(comb))

str2 = 'abcd'
combs = it.permutations(str2,2)
for comb in combs:
    print("".join(comb))

print("*"*30)

numbers = [0,1,2,3,4]
repeated_permutations = it.product(numbers, repeat = 3) # permutations with replacement
for comb in repeated_permutations:
    print(comb)

print("*"*30)

numbers = [0,1,2,3,4]
repeated_combinations = it.combinations_with_replacement(numbers, 4) # creating combinations with replacement
for comb in repeated_combinations:
    print(comb)

print("*"*30)

letters = ['a','b','c','d','e']
numbers = [1,2,3,4]
names = ["Taylor", "McConaughey"]
combined = it.chain(letters,numbers,names)
for element in combined:
    print(element)

print("*"*30)

result = it.islice(range(10), 1, 8, 2) # syntax : islice(iterable, start index, stop index, step)
for i in result:
    print(i)

print("*"*30)

with open('file1.txt', 'r') as f:
    result = it.islice(f,3)
    for line in result:
        print(line)

print("*"*30)

letters = ['a','b','c','d','e','f','g','h']
selectors = [True,False,True,True,False,True,False,True]
result = it.compress(letters,selectors)
print(list(result))

print("*"*30)

def gt_2(x):
    if(x>2):
        return True
    else:
        return False 

numbers = [2,3,1,4,0,6,-3,2]
result = filter(gt_2, numbers)
print(list(result))

print("*"*30)

numbers = [2,3,1,4,0,6,-3,2]
result = it.filterfalse(gt_2, numbers)
print(list(result))

print("*"*30)
