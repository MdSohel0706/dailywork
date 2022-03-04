'''
Add member(s) in a set.
'''

set1 = set()
colors = set()
list_of_colors = ['Yellow', 'Red', 'Green', 'Indigo', 'magenta', 'Orange']
set1.add(34)
set1.add(54)
print('After adding elements to set1',set1)
set1.add((46, 345, 92))
print('After adding few more elements to set1 ', set1)
print()
colors.add('Yellow')
print('After adding a element to colors - ', colors)
colors.update(list_of_colors)
print('After adding few more elements to colors - ',colors)