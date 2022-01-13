def minion_game(s):
    stuart = 0
    kevin = 0
    l = len(s)
    for i in range(l):
        if(s[i] in 'AEIOU'):
            kevin += l - i
        else:
            stuart += l - i
    if(stuart > kevin):
        print("Stuart",stuart)
    elif(kevin > stuart):
        print("Kevin",kevin)
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)