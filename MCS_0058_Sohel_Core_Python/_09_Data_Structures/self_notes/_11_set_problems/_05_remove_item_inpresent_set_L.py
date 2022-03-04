'''
Remove an item from a set if it is present in the set.
'''
colors = {'Red', 'Indigo', 'Orange', 'magenta', 'Yellow', 'Green'}
# Discard() removes an element if it is present
# Where as remove() throws error if the element is not present
colors.discard('black')
print('After discarding an element - ',colors)
colors.discard('Orange')
print('After discarding an element - ',colors)