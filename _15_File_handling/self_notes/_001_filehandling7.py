import Emp, pickle
f = open("emp.dat","rb")
try:
    while(True):
        obj = pickle.load(f)
        obj.display()
except EOFError:
    print("End of file reached ...")