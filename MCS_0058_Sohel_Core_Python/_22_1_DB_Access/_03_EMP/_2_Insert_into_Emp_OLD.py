'''
Created on Mar 20, 2020

@author: madhu
'''
import psycopg2
from distutils.dist import command_re
#Step1 : Get connection
try:
    conn = psycopg2.connect(database="postgres", 
                            user="postgres",
                            password="vn2",
                            host="localhost",
                            port="5432")

    #Step2 : Get cursor on db connection
    cursor = conn.cursor()

    #Step3 : Retrieve emp data
    emp_records = []
    with open('emp_data.txt') as e_data:
        data = e_data.read().split('\n')
        for each in data:
            emp_records.append(each.split(', '))
    print(emp_records)
    for each in emp_records:
        print(each)
        empno = int(each[0])
        ename = each[1]
        job = each[2]
        if each[3] == 'null':
            mgr = None
        else:
            mgr = each[3]
        hiredate = None
        sal = int(each[5])
        if each[6] == 'null':
            comm = None
        else:
            comm = int(each[6])
        deptno = int(each[7])
        li = []
        li.extend([empno, ename, job, mgr, hiredate, sal, comm, deptno])
        print(li)

        # Step4 : Execute sql query
        query = 'INSERT INTO EMPLOYEE1 VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
        cursor.execute(query, tuple(li))
        # 'INSERT INTO EMP_30 VALUES('7839', 'KING', 'PRESIDENT', 'null',
        #            "'17-11-1981,dd-mm-yyyy'", '5000', 'null', '10')
    print("----Records inserted into DEPT successfully-----")    

    #Step 5: Commit the transaction
    conn.commit()
except Exception as exce:
    print("Exception occured : ", exce)
finally:
    print("Closing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()