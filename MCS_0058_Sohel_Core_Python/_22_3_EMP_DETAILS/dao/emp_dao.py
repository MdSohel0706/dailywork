'''
Created on Dec 23, 2019

@author: madhu
'''
from _22_3_EMP_DETAILS.helper.utilities import conn

class DAO:

    def __init__(self):
        pass

    def is_valid(self,eid):
        cursor = conn.cursor()
        try:
            cursor.execute("select * from EMP_DETAILSS where ecode = %s"%(eid))
        except Exception as e:
            cursor.execute("ROLLBACK")
            return None
        else:
            res = cursor.fetchall()
            if res:
                return True # "Success"

    def save(self,cust_data):
        # 8. Receive the data from Service
        cursor = conn.cursor()
        try:
            # 9. Prepare respective SQL Query (CRUD)
            query = 'INSERT INTO EMP_DETAILSS values(%s,%s,%s,%s,%s,%s,%s)'
            # 10.Execute query and commit the transaction with DB
            cursor.execute(query,cust_data)
            conn.commit()
            # 11. Return response to Service
            return "Success"
        except Exception as e:
            print("Exception occured :",e)
        finally:
            cursor.close()
            conn.close()
