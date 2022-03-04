s = ['()',')(()))','(','(())((()())())',')test','hi())(','(hello))','hello','(hell(0))']
for each in s:
    stk = []
    flag = 1
    for letter in each:
        if(letter == "("):
            stk.append(letter)
        elif(letter == ")"):
            try:
                stk.pop()
            except:
                flag = 0
    if(flag == 1):
        if(not stk):
            print(each," : ", True)
        else:
            print(each," : ",False)