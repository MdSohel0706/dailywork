def merge_the_tools(s,k):
    i = 0 
    while(i < (len(s)-(k-1))):
        sub = s[i : (i+k)]
        #print("Sub = ",sub)
        outsub = ""
        j = 0
        while(j < len(sub)):
            if(sub[j] not in sub[0:j]):
                outsub += sub[j]
            j += 1
        if outsub:
            print(outsub)
        i += k

if __name__ == "__main__":
    string, k = input(), int(input())
    merge_the_tools(string, k)
