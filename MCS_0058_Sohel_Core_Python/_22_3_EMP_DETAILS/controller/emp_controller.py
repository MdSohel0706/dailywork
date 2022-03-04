'''
@author: madhu
This is Controller layer

'''

import json
from _22_3_EMP_DETAILS.service.emp_service import EmpService

# Controller
def save_emp_data(in_file):
    # 1. Receive data from UI (Here from json file)
    with open(in_file) as file_obj:
        data = json.load(file_obj)
    # print("Data received from employee :", data)
    # 2. Extract the data
    e_code = data["eCode"]
    user_id = data['userId'].capitalize()
    tech = data['tech'].capitalize()
    role = data['role'].capitalize()
    region = data['region'].capitalize()
    mobile = data['mobile']
    email = data['email'].upper()
    emp = EmpService(e_code, user_id, tech, role, region, mobile, email)
    # 3. Perform server side validations
    res = emp.validate_uid()
    if res:
        # 4.2. send exception message to UI
        return "User already exists"
    else:
        # 4.1. pass data to SERVICE layer
        res = emp.save_emp_details()
        # 13. Receive the data from Service, and send to UI
        return res
    
