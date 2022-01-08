list_ = [5,8,12,16,3,18,1]
index = 0
def rec_lin(x, elem, index):
    if(x[0] == elem):
        return index 
    else:
        index += 1
        return rec_lin(x[1:], elem, index)

print(rec_lin(list_, 18, index))