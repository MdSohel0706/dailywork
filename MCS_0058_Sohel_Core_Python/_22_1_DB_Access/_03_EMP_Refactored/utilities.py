'''

@author: madhu

helper.py
utils.py
utilities.py
properties.py
'''
import psycopg2
conn = psycopg2.connect(database="postgres", 
                        user="postgres",
                        password="vn2",
                        host="localhost",
                        port="5432")

emp_create_q = """
        create table EMP_101(empno INT, 
                            ename TEXT, 
                            job TEXT,
                            mgr INT,
                            hiredate DATE,
                            sal INT,
                            comm INT,
                            deptno INT,
                            primary key(empno),  
                            foreign key(deptno) references dept_101(deptno))
        """
emp_insert_q = 'INSERT INTO EMP_101 VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
emp_update_sal = "UPDATE EMP_101 set sal = 25000 where empno = 7839"
EMP_DATA_SEL = "SELECT * FROM EMPLOYEE"