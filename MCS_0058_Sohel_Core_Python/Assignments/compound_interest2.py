amount = float(input("Enter the amount in the savings account : "))
after1year = amount*((1+(4/100))**1)
after2year = amount*((1+(4/100))**2)
after3year = amount*((1+(4/100))**3)
print("Amount after 1st year = {:.2f}".format(after1year))
print("Amount after 2nd year = {:.2f}".format(after2year))
print("Amount after 3rd year = {:.2f}".format(after3year))