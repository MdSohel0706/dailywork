'''
Created on Mar 20, 2020

@author: madhu
'''
from _22_1_DB_Access._03_EMP_Refactored.utilities import conn, emp_insert_q

def _get_data_from_txt():
    emp_records = []
    with open('emp_data.txt') as e_data:
        data = e_data.read().split('\n')
    for each in data:
        emp_records.append(each.split(', '))
    #print(emp_records)
    li = []
    for each in emp_records:
        empno = int(each[0])
        ename = each[1]
        job = each[2]
        if each[3] == 'null':
            mgr = None
        else:
            mgr = each[3]
        hiredate = None
        sal = int(each[5])
        if each[6] =='null':
            comm = None
        else:
            comm = int(each[6])
        deptno = int(each[7])
        print([empno, ename, job, mgr, hiredate, sal, comm, deptno])
        li.append([empno, ename, job, mgr, hiredate, sal, comm, deptno])
    return li

try:
    cursor = conn.cursor()
    data = _get_data_from_txt()  # protected method
    for each in data:
        cursor.execute(emp_insert_q, tuple(each))
    conn.commit()
    print("----Records inserted into employee successfully-----")
except Exception as exce:
    print("Exception occured : ", exce)
finally:
    print("Closing cursor and connection to POSTGRESQL")
    cursor.close()
    conn.close()

