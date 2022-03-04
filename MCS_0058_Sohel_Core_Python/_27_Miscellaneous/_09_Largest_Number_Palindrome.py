import itertools as it

largest = -1
innum = int(input("Enter input number : "))
strinnum = str(innum)
combins = it.permutations(strinnum,len(strinnum))
for comb in combins:
    word = "".join(comb)
    if(word == word[::-1]):
        if(int(word) > largest):
            largest = int(word) 

print(largest)





