'''
[ ((),(),(),()) , ((()),(())) , ((((())))) ] -> 5
[ ((),(),(),(),(),()) , ((()),(()),(())) , (((())),((()))) , ((((((())))))) ] -> 7
[ ((),(),(),(),(),(),(),()) , ((()),(()),(()),(())) , ((((()))),(((())))) , ((((((((())))))))) ] -> 9
[ (((((()))))) , ((),(),(),(),()) ] -> 6
'''
import sys
def nest_my_tuples(n):
    output = []
    output.append("(" * n + ")" * n)
    if(n <= 0):
        print("Number should be greater than 0")
        sys.exit()
    elif(n % 2 != 0):
        for i in range(2,n):
            if((n-1) % i == 0):
                a = int((n-1)/i)
                b = i
                p = ""
                for j in range(1,(i+1)):
                    x = "("*(int((n-1)/i)) + ")"*(int((n-1)/i))
                    p = p + x
                final = "("+p+")"
                output.append(final)
    else:
        output.append("(" + "()" * (n - 1) + ")")
    print(output)

n = int(input("Enter a number : "))
nest_my_tuples(n)