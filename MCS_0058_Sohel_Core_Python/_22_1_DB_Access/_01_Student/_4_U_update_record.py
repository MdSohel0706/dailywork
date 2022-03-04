'''
Created on Mar 20, 2020

@author: madhu
'''
import psycopg2
try:
    conn = psycopg2.connect(database="postgres", 
                            user="postgres",
                            password="vn2",
                            host="localhost",
                            port="5432")
    cursor = conn.cursor()
    query = "UPDATE STUDENT set name = 'MadhuSudhan Naidu Nettem' where student_id = 101"
    res = cursor.execute(query)
    print("Record Updated successfully : ", res)
    conn.commit()
except Exception as exce:
    print("Exception occured : ",exce)
finally:
    print("Closing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()