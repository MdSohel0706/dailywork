'''
Get the length in bytes of one array item in the internal representation.
'''
import array as arr
arr1 = arr.array('i', [5, 83, 272, 92, 73, 83, 52])
print('array elements - ', arr1)
print(arr1.itemsize)
# print(arr1[0].itemsize)