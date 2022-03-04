my_dict = {"A":{"id":100,"name":"Sohel","salary":{"Basic":1000,"Special":2000,"HR":3000}}, "B":{"id":200,"name":"Sasi","salary":{"Basic":500,"Special":1500,"HR":2500}}, "A":{"id":300,"name":"Rak","salary":{"Basic":99,"Special":999,"HR":9999}}}

for outer_key in my_dict.keys():
    print("Key = ",outer_key," Value = ",my_dict[outer_key])

print("----------")
l = ["c","o","m","e"]
print(l[-3:-2])