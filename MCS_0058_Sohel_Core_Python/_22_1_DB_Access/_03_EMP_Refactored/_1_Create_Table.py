'''
@author: madhu

https://www.tutorialspoint.com/postgresql/postgresql_python.htm
https://pynative.com/python-postgresql-tutorial/
'''
from _22_1_DB_Access._03_EMP_Refactored.utilities import conn, emp_create_q

try:
    cursor = conn.cursor()
    cursor.execute(emp_create_q)
    print("EMP Table Created")
    conn.commit()
except Exception as exce:
    print("Exception occured : ",exce)
finally:
    print("Closing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()
