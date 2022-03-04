'''
Create an array of 5 integers and display the array items. Access individual element through indexes.
'''
# import array as arr
# array1 = arr.array('i',[3, 8, 4, 9, 6])
# print(array1)

import array as arr
a = arr.array('d', [1.1, 3.5, 4.5])
# print(a)
print("Accessing Elements using for loop -")
for i in range(0, 3):
    print(a[i])

# print('\n')
# array_of_colors = arr.array('B', ('B', 'Y', 'R', 'B', 'P', 'O'))
# print('Accessing Elements of array_of_colors')
# for i in range(len(array_of_colors)):
#     print(array_of_colors[i])