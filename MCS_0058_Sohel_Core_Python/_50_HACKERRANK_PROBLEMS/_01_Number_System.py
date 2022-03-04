def print_formatted(number):
    number_str = str(number)
    for i in range(1,(number+1)):
        dec = str(i)
        adjustsize = len(number_str)
        print(dec.rjust(len(binary(number))), end = " ")
        print(octal(i).rjust(len(binary(number))), end = " ")
        print(hexadecimal(i).rjust(len(binary(number))), end = " ")
        print(binary(i).rjust(len(binary(number))))

def octal(number):
    output_list = []
    while(number != 0):
        output_list.append(str(number%8))
        number = number // 8
    output_list.reverse()
    output = "".join(output_list)
    return output

def binary(number):
    output_list = []
    while(number != 0):
        output_list.append(str(number%2))
        number = number // 2
    output_list.reverse()
    output = "".join(output_list)
    return output

def hexadecimal(number):
    map_dict = {0 : "0", 1 : "1", 2 : "2", 3 : "3", 4 : "4", 5 : "5", 6 : "6", 7 : "7", 8 : "8", 9 : "9",
    10 : "A", 11 : "B", 12 : "C", 13 : "D", 14 : "E", 15 : "F"}
    output_list = []
    while(number != 0):
        output_list.append(map_dict[number%16])
        number = number // 16
    output_list.reverse()
    output = "".join(output_list)
    return output
"""
if __name__ == '__main__':
    limit = int(input())
    print_formatted(limit)
    print("abc".rjust(4))
"""