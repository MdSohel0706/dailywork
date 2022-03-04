cost = float(input("Enter the cost of meal : "))
print("Grand Total = {:.2f}\nTax = {:.2f}\nTip = {:.2f}".format((cost+(cost*25/100)+(cost*18/100)),(cost*25/100),(cost*18/100)))