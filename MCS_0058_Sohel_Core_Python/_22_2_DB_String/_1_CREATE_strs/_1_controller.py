

'''
    Part I                     Part II           Part III
    UI                        --> PL        ---> Database
    (HTML,CSS,Javascript)        (Python)        (Mysql, Postgresql, Mongodb)

UI --1-->                    Python                                   ----> Database
         --2.I-->  Controller  --2.II-->  Service  --2.III-->  DAO -->
         <--3.3--              <--3.2--             <--3.1--       <--

3 responsibilities:
     I. Controller --> Receive input from customer, validate it.
    II. Service    --> Implement business logic
   III. DAO        --> Prepare query and interact with database,get results
'''


'''
Mobileno : Client validations --> 10 digit,all numbers  
           Server validations --> valid no or not  

'''

'''
Controller   :
---------------
     1. Receive the request data from UI,     (json,xml to dict) 
   2.1. Perform server side validations and
         if success: Pass the data to Service layer
         else      : Send error response details
   2.2. Pass the data to Service layer
     3. Receive response from Service layer 
     4. Prepare resp data and send to UI
             
'''

'''
REQ:  Find length of each word  string(, separated) and store the results to db 
Criteria: User will give string along with his userid. 
          Last word in the string can be considered as userid
hello,world,welcome,to,python,MadhuNettem
output: hello - 5
        world - 6
        ....


CRUD            - Create, Retrieve
Data types      - string int 
STATE, BEHAVIOR -
'''
from _22_2_DB_String._1_CREATE_strs._2_service import get_len

# Controller
def get_str_len(in_str):
    if in_str == '':
        return "Enter valid string"
    else:
        # st_len = _2_service.get_len(in_str)
        word_data = get_len(in_str)
        #print(word_data)
        return {'user_id': word_data[1],
                'st_len': len(word_data[0].keys()),
                'words': word_data[0]}

# UI Layer
if __name__ == '__main__':
    str1 = input("Enter string : ")
    resp = get_str_len(str1)  # calling controller layer  (flask, django)
    #print("String length :", resp)
    print("Welcome Mr : ", resp['user_id'])
    print("Total words : ", resp['st_len'])
    print("Word details  : ")
    for word, count in resp['words'].items():
        print(word, "----", count)