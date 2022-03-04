'''
REQ:  Find length of the strings given by customer and save into db

CRUD           - R
Datattypes     - int string
STATE,BEHVAIOR -
'''


from _22_2_DB_String._2_CREATE_mulitple_strs._1_controller import get_str_len

# UI Layer
if __name__ == '__main__':
    str1 = input("Enter string details  : ")
    resp = get_str_len(str1)  # flask, django
    print("String length :", resp)