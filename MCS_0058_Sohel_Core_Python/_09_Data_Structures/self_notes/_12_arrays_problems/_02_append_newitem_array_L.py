'''
Append a new item to the end of the array.
'''
import array as arr
# With Append() the element is automatically added to the end of the array
array_of_nums = arr.array('i', [5, 8, 9, 43, 5, 74, 3])
print('array_of_nums before appending element - ',array_of_nums)
array_of_nums.append(55)
print('array_of_nums after appending element - ',array_of_nums)
