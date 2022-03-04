'''
Append items from iterable to the end of the array
'''
import array as arr
arr1 = arr.array('i', [53, 92, 43, 93, 41, 6])
arr2 = arr.array('i', [54, 92, 54, 98, 42, 91])
arr_rolls = arr.array('i',[64, 83, 92, 75, 3])
arr3 = arr.array('d', [74.94, 72.84, 2.03, 93.73, 5, 5.2, 42.5])
# print('type of arr_rolls', type(arr_rolls[0]))


# Append elements on e by one - append()
def app_arr(array1, array2):
    if type(array1[0]) == type(array2[0]):
        for i in array2:
            array1.append(i)
        return array1
    return 'Cannot Append'


# Add all elements at once - extend()
def ext_arr(array1, array2):
    if type(array1[0]) == type(array2[0]):
        array1.extend(array2)
        return array1
    return 'Array elements should be of same datatype to extend/append'


print('After appending arr1 - ',app_arr(arr1, arr2))
print('After appending arr_rolls to arr2 - ', ext_arr(arr2, arr_rolls))
print('Appending arr3 and arr_rolls - ', ext_arr(arr_rolls, arr3))