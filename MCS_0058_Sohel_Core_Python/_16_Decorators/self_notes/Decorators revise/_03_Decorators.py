def create_adder(x,operation):
    def adder(y):
        return x+y

    def subtractor(y):
        return x-y
    
    try:
        assert operation == 'add'
        return adder
    except:
        return subtractor

adder = create_adder(10,'add')
print(adder(15))
print(create_adder(10,'add')(45))
print(create_adder(50,'sub')(15))

print(type(adder))
print(type(adder(5)))
print(type(create_adder))
print(type(create_adder(10,'add')))
print(type(create_adder(10,'sub')(45)))

