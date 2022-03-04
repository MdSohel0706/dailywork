'''
Created on Mar 20, 2020

@author: madhu
'''
import psycopg2
import xlsxwriter   # python -m pip install xlsxwriter
try:
    conn = psycopg2.connect(database="postgres", 
                            user="postgres",
                            password="vn2",
                            host="localhost",
                            port="5432")
    print("Conn type  :", type(conn))
    print("Connection :", conn)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM EMPLOYEE")
    print("\n-----Retrieving records from db table DEPT-------")
    records = cursor.fetchall()
    workbook = xlsxwriter.Workbook('EDATA.xlsx')
    worksheet = workbook.add_worksheet()
    cell = 1
    for each in records:
        print(each)
        worksheet.write('A'+str(cell), each[0])
        worksheet.write('B'+str(cell), each[1])
        worksheet.write('C'+str(cell), each[2])
        worksheet.write('D'+str(cell), each[3])
        worksheet.write('E'+str(cell), each[4])
        worksheet.write('F'+str(cell), each[5])
        worksheet.write('G'+str(cell), each[6])
        worksheet.write('H'+str(cell), each[7])
        cell += 1
except Exception as exce:
    print("Exception occured : ", exce)
finally:
    print("\nClosing cursor and connection to POSTGRESQL")
    workbook.close()
    cursor.close()
    conn.close()