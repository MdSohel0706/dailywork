n = int(input("Enter the number of containers : "))
refund = 0
for i in range(0,n):
    bottle = float(input("Enter the volume of bottle : "))
    if(bottle <= 1):
        refund += 0.1
    else:
        refund += 0.25

print("Refund = {:.2f}".format(refund))