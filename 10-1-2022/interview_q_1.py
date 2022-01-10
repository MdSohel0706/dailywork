class Num:
    def __init__(self):
        self.n = int(input())
        self.L = []
        self.count = 0
    def ipermute(self):
        for i in range(self.n):
            self.L.append(int(input()))
        size = 1
        while(size <= self.n):   #size selecting
            for i in range(0,(self.n-size+1)): #start selecting  
                extra = []
                slice = self.L[i:(i+size)]   #(i+size) means end selecting
                print("*"*10)
                print("Slice = ",slice) #slic is the sublist of the slice which we shall check
                for p in range(0,i):
                    extra.append(self.L[p])
                for p in range((i+size),self.n):
                    extra.append(self.L[p])
                print("Extra = ",extra) #extra is what is left in the whole array if not for those elements
                not_possible = False
                set1 = set(slice)
                ideal = list(range(1,(len(slice)+1)))   #ideal is the ideal list we want to get of variable length
                outcast = set1.difference(ideal) #outcasts are the elements present in slice but not in the ideal
                outcast_list = list(outcast)
                print("Outcasts = ",outcast)
                substitutes = set(ideal).difference(set(slice)) #substitutes are the elements present in ideal but not in slice
                subsitutes_list = list(substitutes)
                print("Substitutes = ",substitutes)
                if(len(outcast_list) > 2):
                    not_possible = True 
                    continue
                else:
                    subs_in_extras_or_not = substitutes.intersection(set(extra))    #self explanatory from name of variable
                    print("Subs in extras present = ",subs_in_extras_or_not)
                    if(subs_in_extras_or_not == substitutes):
                        self.count += 1   
                        print("Count = ",self.count) 
                        break  
            print("*"*10)   
            size +=1
        return self.count 

numb = Num()
number_of_possibilities = numb.ipermute()
print("Possibilities = ",number_of_possibilities)