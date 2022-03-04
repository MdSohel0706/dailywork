'''
table of the given number
'''
n = int(input('Enter a num'))


def mul_table(num, max):
    table = ''
    for i in range(1, max+1):
        table += str(f'{num} * {i} = {num * i} \n')
    return table


if __name__ == '__main__':
    print(mul_table(n, 10))