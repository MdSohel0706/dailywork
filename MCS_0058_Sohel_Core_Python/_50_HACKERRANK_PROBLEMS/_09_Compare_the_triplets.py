a = list(map(int, input().split()))
b = list(map(int, input().split()))
def compareTriplets(a, b):
    outlist = []
    alice_score = 0
    bob_score = 0
    for x,y in zip(a,b):
        if(x > y):
            alice_score += 1
        if(y > x):
            bob_score += 1
    outlist.append(alice_score)
    outlist.append(bob_score)
    return outlist

print(compareTriplets(a,b))

