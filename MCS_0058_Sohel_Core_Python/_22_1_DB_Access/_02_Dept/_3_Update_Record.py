'''
Created on Mar 20, 2020

@author: madhu
'''
import psycopg2
#Step1 : Get connection
try:
    conn = psycopg2.connect(database="postgres", 
                            user = "postgres", 
                            password = "vn2", 
                            host = "localhost", 
                            port = "5432")
    print("Conn type  :",type(conn))
    print("Connection :",conn)
    #Step2 : Get cursor on db connection
    cursor = conn.cursor()
    #Step3 : Execute sql query 
    res = cursor.execute("UPDATE dept_001 set dname = 'MYSALES' where deptno = 30")
    print("Updation : ",res)
    #Step4: Commit the transaction
    conn.commit()
except Exception as exce:
    print("Exception occured : ",exce)
finally:
    print("Closing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()