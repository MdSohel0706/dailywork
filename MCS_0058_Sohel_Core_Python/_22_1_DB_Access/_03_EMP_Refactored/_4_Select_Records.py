'''
Created on Mar 20, 2020

@author: madhu
'''
from _22_1_DB_Access._03_EMP_Refactored.utilities import conn, EMP_DATA_SEL

try:
    cursor = conn.cursor()
    # cursor.execute("SELECT * FROM EMP")
    cursor.execute(EMP_DATA_SEL)
    print("\n-----Retrieving records from db table employee-------")
    records = cursor.fetchall()
    for each in records:
        print(each)
except Exception as exce:
    print("Exception occured : ",exce)
finally:
    print("\nClosing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()