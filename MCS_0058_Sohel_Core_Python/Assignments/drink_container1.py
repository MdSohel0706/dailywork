n = int(input("Enter the number of containers : "))
bottles = []
i = 1
while(i <= n):
    bottles.append(float(input("Enter volume : ")))
    i += 1

refund = 0
for i in bottles:
    if(i <= 1):
        refund += 0.10
    else:
        refund += 0.25

print("Refund = {:.2f}".format(refund))