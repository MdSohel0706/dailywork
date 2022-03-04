
# Python program to remove leading zeros
# an IP address and print the IP
 
# function to remove leading zeros
def removeZeros(ip):
    masklist = ip.split("/")
    mask = masklist[-1]
    masklist = masklist[0:(len(masklist)-1)]
    ip = ".".join(masklist)
    # splits the ip by "."
    # converts the words to integeres to remove leading removeZeros
    # convert back the integer to string and join them back to a string
    new_ip = ".".join([str(int(i)) for i in ip.split(".")]) 
    new_ip = new_ip +"/"+ mask

    return new_ip
 
ip ="001.200.001.004/24"
print(removeZeros(ip))
