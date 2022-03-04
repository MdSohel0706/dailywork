def appendAnddelete(s, t, k):
    if(len(s) < len(t)):
        min = s 
    else:
        min = t
    i = 0
    for i in range(len(min)):
        if(s[i] == t[i]):
            i += 1
        else:
            break
    s = s[i:]
    t = t[i:]
    print("S = ",s)
    print("T = ",t)
    req = len(s)+len(t)
    if(req <= k):
        return "Yes"
    else:
        return "No"

print(appendAnddelete("aaaaa","aa",8))