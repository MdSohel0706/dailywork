def substring_game(st):
    A = []
    B = []
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    length = len(st)
    for i in range(length):
        for j in range((i+1),(length + 1)):
            sub = st[i:j]
            if(sub[0] in vowels):
                A.append(sub)
            else:
                B.append(sub)

    print("A = ",A)
    print("B = ",B)
    if(len(A)>len(B)):
        print("A is winner")
    else:
        print("B is winner")

input_string = input("Enter a string : ")
substring_game(input_string)
