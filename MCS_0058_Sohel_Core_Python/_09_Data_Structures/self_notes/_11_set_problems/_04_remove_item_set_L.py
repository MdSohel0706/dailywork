'''
Remove item(s) from set
'''
colors = {'Red', 'Indigo', 'Orange', 'magenta', 'Yellow', 'Green'}
# pop removes random element from the set
colors.pop()
print('After removing an element - ', colors)
# remove() removes specified element from the set
colors.remove('magenta')
print('After removing specified element - ', colors)