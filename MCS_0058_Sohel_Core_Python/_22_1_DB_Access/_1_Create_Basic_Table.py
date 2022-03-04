'''
Created on Mar 20, 2020

@author: madhu

https://www.tutorialspoint.com/postgresql/postgresql_python.htm
https://pynative.com/python-postgresql-tutorial/

UI    --->   Python   --->  Database
      <---    Java    <---
              .Net
'''
# Step 1 : Get connection
# Step 2 : Get cursor on db connection
# Step 3 : Prepare SQL Query
# Step 4 : Execute SQL query
# Step 5 : Commit the transaction

'''
Hostname      :   vn2tech.cgfvhuzburei.us-east-2.rds.amazonaws.com
Port          :   5432
Maintenance DB:   postgres
Username      :   postgres /  vn2tech123 
'''
# > python -m pip install psycopg2   (check for this library in site-packages)_
import psycopg2

try:
    # Step1 : Get connection
    conn = psycopg2.connect(host="localhost",
                            port="5432",
                            user="postgres",
                            password="vn2")
    print("Connection object : ", type(conn), conn)

    # Step2 : Get cursor on db connection
    my_cursor = conn.cursor()
    print("Cursor object : ", type(my_cursor), my_cursor)

    # Step3: Prepare SQL Query
    query = "CREATE TABLE FILE_DATA10(filename VARCHAR(20) PRIMARY KEY, filesize VARCHAR(20), extension VARCHAR(20), uploadedtime VARCHAR(20), uploadedby VARCHAR(20), sub_files_ext VARCHAR(20),Files_count VARCHAR(20))"

    # Step4 : Execute sql query
    my_cursor.execute(query)

    # Step5: Commit the transaction
    conn.commit()

    print("** Table created successfully **")
except Exception as exce:
    print("Exception occured : ", exce)
finally:
    print("Closing cursor and connection to POSTGRESQL")
    my_cursor.close()
    conn.close()


'''
import psycopg2
try:
    conn = psycopg2.connect(host = "localhost",
                            port = "5432",
                            database="postgres",
                            user = "postgres", 
                            password = "vn2")
    cursor = conn.cursor()
    emp_table_cr = 'create table command'
    cursor.execute(emp_table_cr)
    conn.commit()
except Exception exec:
    print("Exception occured : ", exec)
finally:
    cursor.close()
    conn.close()
'''



