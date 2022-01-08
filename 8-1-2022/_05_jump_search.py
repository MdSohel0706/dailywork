def linear_search(list_, element, step, i):
    index = -1
    for k in range(step):
        if(list_[i + k] == element):
            index = i + k
        return index

def jump_search(list_, element):
    i = 0
    length = len(list_) - 1
    exit = False
    step = int(input("Enter the step size for jumping : "))
    while(exit == False):
        if(element < list_[0]):
            print("Element not present in list.")
            exit = True
        elif(i < length):
            if(list_[i] == element):
                print(f"Element found at {i} index.")
                exit = True
            elif(list_[i] < element):
                i += step   
        elif(i >= length or list_[i] > element):
            i -= step 
            if(list_[i] < element):
                index = linear_search(list_, element, step, i)
                if(index != -1):
                    print("Element found at {} index.".format(index)) 
                else:
                    print("index = ",index)
                    print("Element not present in list.")
            exit = True

list_ = [1,4,7,10,15,17,24,36,38,43,49,55,56]
element = -20
jump_search(list_, element)
