
try:
    amt = 1000
    if amt < 5000:
        raise NameError("Insuff. Funds") # Raise exception manually
except NameError as name:
    print("AN EXCEPTION OCCURED ::", name)

'''
In Java, below line is object cration

Java   : NameError name = NameError("Insuff. Funds")

Python : name = NameError("Insuff. Funds")  # Rem. all scenarios
         NameError name = NameError("Insuff. Funds")   #Exception handling
'''