cost = float(input("Enter the cost of meal : "))
tax = cost*25/100
tip = cost*18/100
grand_total = cost + tax + tip
print("Grand Total = {:.2f}\nTax = {:.2f}\nTip = {:.2f}".format(grand_total,tax,tip))