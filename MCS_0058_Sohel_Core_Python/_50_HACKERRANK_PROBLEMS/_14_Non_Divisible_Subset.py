from itertools import combinations

def nonDivisibleSubset(k, s):
    for i in range(2,(len(s)+1)): #loop to select number of elements in subset
        outlist = []
        output = 1
        matching_subset_found = False
        subsets = combinations(s,i)
        for subset in subsets:
            matching_pair_found = False
            pairs = combinations(subset,2)
            for pair in pairs:
                if(pair[0] + pair[1] == k):
                    matching_pair_found == True
                    break
            if(matching_pair_found == True):
                matching_subset_found = True 
                break
    if(matching_subset_found == False):
        outlist.append(i)
        
    return outlist[-1]
            

                    

print(nonDivisibleSubset(7,[278,576,496,727,410,124,338,149,209,702,282,718,771,575,436]))