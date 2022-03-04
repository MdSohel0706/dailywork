''''''
'''
Service   :
---------------
     1. Receive the validated data from Controller
     2. If required interact with database for more data (dao layer call)
     3. Implement business logic as per give requirement
     4. Call dao layer(Pass the data) for data persistence
     5. Get response from DAO and send it to controller

'''
from _22_2_DB_String._1_CREATE_strs._3_dao import save_to_db

# Business logic
def get_len(str_val):
    words = {}
    data = str_val.split(",")
    c_data = data[0:-1]
    user_id = data[-1]
    #print(c_data,user_id)
    le = 0
    for word in c_data:
        for char in word:
            le += 1
        words[word] = le
    res = save_to_db(user_id, c_data, le)
    if res:
        return words, user_id
    else:
        return "Something happened!!"