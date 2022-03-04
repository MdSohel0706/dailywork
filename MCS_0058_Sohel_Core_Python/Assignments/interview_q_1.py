def ipermute():
    n = int(input())
    L = []
    for i in range(n):
        L.append(int(input()))
    size = 1
    while(size <= n):   #size selecting
        for i in range(0,(n-size+1)): #start selecting  
                extra = []
                slice = L[i:(i+size)]   #(i+size) means end selecting
                #print("*"*10)
                #print("Slice = ",slice)
                for p in range(0,i):
                    extra.append(L[p])
                for p in range((i+size),n):
                    extra.append(L[p])
                #print("Extra = ",extra)
                #print("*"*10)
                not_possible = False
                set1 = set(slice)
                ideal = list(range(1,(len(slice)+1)))
                outcast = set1.difference(ideal)
                outcast_list = list(outcast)
                subsitutes = list((set(ideal)).difference(set(slice)))
                if(len(outcast_list) > 2):
                    not_possible = True 
                    break
                else:
                    if()
                    

                if(not_possible == True):
                    continue

                
        size +=1
            
            


def required(L):
    arranged = True
    L.sort()
    ideal = list(range(1,(len(L))+1))
    for i in range(len(L)):
        if(L[i] != ideal[i]):
            arranged = False
    return arranged

ipermute()