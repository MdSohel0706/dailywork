'''
Created on Dec 23, 2019

@author: madhu
'''
from _22_3_EMP_DETAILS.dao.emp_dao import DAO

class EmpService:
    
    def __init__(self, empcode, userId=None, tech=None, role=None, region=None, mobile=None, email=None):
        self.empcode = empcode
        self.userId = userId
        self.tech = tech
        self.role = role
        self.region = region
        self.mobile = mobile
        self.email = email

    def validate_uid(self):
        dao = DAO()
        rec_exists = dao.is_valid(self.empcode)
        return rec_exists

    def save_emp_details(self):
            # 5. Receives the data from Controller
            u_data = (self.empcode, self.userId, self.tech, self.role, self.region, self.mobile, self.email)
            # print(u_data)

            # 6. Implement business logic for the given requirement

            # 7. Pass the final data to DAO layer
            dao = DAO()
            res = dao.save(u_data)
            # 12. Receive the data from DAO , perform other operations on data and return the response to Controller
            return res

