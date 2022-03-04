'''
Iterate over sets
'''

set1 = {34, 23, 45, 83, 92, 54}
set2 = set((34, 73, 'Forset', 'animate', 73))

print('Iterating over set1 - ')
for val in set1:
    print(val)

print()
print('Iterating over set2 - ')
for i , n in enumerate(set2):
    print(i , n)

print()
print("Iterating over set2 using comprehension  ")
[print(val) for val in set2]