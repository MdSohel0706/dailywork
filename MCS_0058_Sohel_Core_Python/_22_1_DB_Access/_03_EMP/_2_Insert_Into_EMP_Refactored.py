'''
Created on Mar 20, 2020

@author: madhu
'''
import psycopg2

def _get_data_from_txt():
    emp_records = []
    with open('emp_data.txt') as e_data:
        data = e_data.read().split('\n')
    for each in data:
        emp_records.append(each.split(', '))
    #print(emp_records)
    li = []
    for each in emp_records:
         #print([empno,ename,job,mgr,hiredate,sal,comm,deptno])
        li.append([each[0],each[1],each[2],each[3],each[4],each[5],each[6],each[7]])
    return li

try:
    # Step1 : Get connection
    conn = psycopg2.connect(database="postgres",
                            user="postgres",
                            password="vn2",
                            host="localhost",
                            port="5432")
    # Step 2 : Get cursor on db connection
    cursor = conn.cursor()
    # Step 3 : Retrieve emp data
    data = _get_data_from_txt()
    print(data)
    # Step 4 : Execute Query
    query = 'INSERT INTO employee1 VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
    for each in data:
        print("each record data:", each)
        cursor.execute(query, tuple(each))
    # Step 5: Commit the transaction
    conn.commit()
    print("----Records inserted into EMPLOYEE successfully-----")
except Exception as exce:
    print("Exception occured : ", exce)
finally:
    print("Closing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()