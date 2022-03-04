alist = [1,2,3,4,1,2,3,2,1]

'''
[1,1,1] = 1
[2,2,2] = 8
[3,3] = 9
[4] = 4
sum = 22
'''
outlist = []
sum = 0
while(alist):
    num = alist[0]
    count_num = alist.count(num)
    sum += pow(num,count_num)
    while(num in alist):
        try:
            alist.remove(num)
        except:
            pass 
    
print(sum)


