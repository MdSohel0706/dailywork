'''
Reverse the order of the items in the array.
1. Using reverse()

2. Creating new array and adding them in reverse
'''
import array as arr
array_num = arr.array('i', [1, 3, 5, 3, 7, 1, 9, 3])
arr_id = arr.array('d',[6.3, 6.93, 63.43, 43.7, 93.5, 24.8, 83.6])
print('Array Before reversing - ',array_num)
# Reverse
array_num.reverse()
print('Array after reversing - ', array_num)


# def rev_arr(array1):
#     rev_array = arr.array('d',[])
#     lst1 = []
#     len(l