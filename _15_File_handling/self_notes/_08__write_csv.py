# write the data into csv file
import csv

with open('Python.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name', 'Rank']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'Rank': 'B', 'first_name': 'Parker', 'last_name': 'Brian'})
    writer.writerow({'Rank': 'A', 'first_name': 'Smith',
                     'last_name': 'Rodriguez'})
    writer.writerow({'Rank': 'B', 'first_name': 'Jane', 'last_name': 'Oscar'})
    writer.writerow({'Rank': 'B', 'first_name': 'Jane', 'last_name': 'Loive'})

print("Writing complete")


# write data using pandas
import pandas

df = pandas.read_csv('employeedata.csv',
                     index_col='Employee',
                     parse_dates=['Hired'],
                     header=0,
                     names=['Employee', 'Hired', 'Salary', 'Sick Days'])
df.to_csv('hrdata_modified.csv')
print("Data Export to csvfile completed")