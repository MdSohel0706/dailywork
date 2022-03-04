'''
Created on Mar 20, 2020

@author: madhu

https://www.tutorialspoint.com/postgresql/postgresql_python.htm
https://pynative.com/python-postgresql-tutorial/
'''
import psycopg2
#Step1 : Get connection
try:
    conn = psycopg2.connect(database="postgres", 
                            user="postgres",
                            password="vn2",
                            host="localhost",
                            port="5432")
    print("Conn type  :", type(conn))
    print("Connection :", conn)
    #Step2 : Get cursor on db connection
    cursor = conn.cursor()
    #Step3: Prepare SQL Query
    query = "create table dept_001(deptno INT PRIMARY KEY,dname TEXT,loc TEXT)"
    #Step3 : Execute sql query
    cursor.execute(query)
    print("DEPT Table Created")
    #Step4: Commit the transaction
    conn.commit()
except Exception as exce:
    print("Exception occured : ",exce)
finally:
    print("Closing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()
