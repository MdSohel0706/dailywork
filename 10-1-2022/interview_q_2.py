from itertools import combinations, permutations
def palindrome(str1):
    reverse=str1[::-1]
    if str1==reverse:
        return str1

def permutaion(str1):
    list1=[""]
    for size in range(1,len(str1)+1): #determining the length of each combination
        combins=combinations(str1,size)  #storing the combinations of one required length
        #list2 = []

        for one_combin in combins: 
            combin_word = "".join(one_combin) #printing each combination word
            permutes = permutations(combin_word,size)
            print("Printing all permutations of length ",size," for ",combin_word," : ")
            list2 = []
            for one_permute in permutes:
                permute_word = "".join(one_permute)
                print(permute_word)
                list2.append(permute_word)
            list2 = list(set(list2))
            for m in list2:
                if(palindrome(m)):
                    list1.append(m)


    print("\nPrinting the required result : ")
    for i in list1:
        print(i)
    print("Total required permutations : ",len(list1))
        
permutaion('aaccb')