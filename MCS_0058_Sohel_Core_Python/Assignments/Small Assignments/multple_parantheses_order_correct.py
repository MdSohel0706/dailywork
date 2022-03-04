def mulpar(test_case):
    stk = []
    flag = 1
    try:
        for letter in test_case:
            if(letter == "["):
                stk.append(letter)
            elif(letter == "{"):
                stk.append(letter)
            elif(letter == "("):
                stk.append(letter)
            elif(letter == "]"):
                if(stk.pop() != "["):
                    flag = 0
            elif(letter == "}"):
                if(stk.pop() != "{"):
                    flag = 0
            elif(letter == ")"):
                if(stk.pop() != "("):
                    flag = 0
        if(flag == 1):
            return True
        else:
            return False
    except:
        return False

test_case = input("Enter expression : ")
print(mulpar(test_case))