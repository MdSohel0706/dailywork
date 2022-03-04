from itertools import combinations
n = int(input())
inplist = []
for i in range(n):
    inplist.append(int(input()))

result = []
outset = set()
outlist = list(combinations(inplist, 3))

for comb in outlist:
    sum1 = 0
    for i in range(len(comb)):
        sum1 += comb[i]
    if(sum1 == 0 and set(comb) not in outset):
        outset.add(comb)
        result.append(list(comb))

print(outset)