from collections import Counter
x = int(input())
show_sizes = list(map(int, input().split()))
n = int(input())
size_vs_price = []
for i in range(n):
    sublist = list(map(int, input().split()))
    size_vs_price.append(sublist) 

show_sizes_dict = Counter(show_sizes)

total = 0
for size, price in size_vs_price:
    if(size in show_sizes_dict.keys()):
        if(show_sizes_dict[size] > 0):
            total += price 
            show_sizes_dict[size] -= 1

print(total)



