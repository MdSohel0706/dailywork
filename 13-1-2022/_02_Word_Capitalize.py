import re
import os
def solve(s):
    l = len(s)
    rex = r'^[a-z]'
    if(re.findall(rex, s[0])):
        s = s.capitalize()
    for i in range(1,l):
        if(s[i-1] == " " and re.findall(rex, s[i])):
            s = s[:i] + s[i].upper() + s[i+1:]
    return s
    
if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)


    
