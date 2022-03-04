'''
You are given a string .
Your task is to print all possible permutations of given size  of the string in lexicographic sorted order.
'''

import itertools as it
s, k = input().split()
k = int(k)

perms = it.permutations(s, k)
L = []
for perm in perms:
    L.append("".join(perm))

L.sort()
for word in L:
    print(word)