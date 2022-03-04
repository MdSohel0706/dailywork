'''
Created on Mar 20, 2020

@author: madhu


'''
from _22_1_DB_Access._03_EMP_Refactored.utilities import conn, emp_update_sal

try:
    cursor = conn.cursor()
    res = cursor.execute(emp_update_sal)
    print("Updation : ", res)
    conn.commit()
except Exception as exce:
    print("Exception occured : ", exce)
finally:
    print("Closing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()