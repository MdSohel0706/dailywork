'''
CSV File

A csv stands for "comma separated values", which is defined as a simple file format that uses specific
structuring to arrange tabular data. It stores tabular data such as spreadsheet or database in plain text
and has a common format for data interchange. A csv file opens into the excel sheet, and the rows and columns
data define the standard format.

The CSV module work is used to handle the CSV files to read/write and get data from specified columns.

Reading CSV files

Python provides various functions to read csv file. We are describing few method of reading function.

    Using csv.reader() function

In Python, the csv.reader() module is used to read the csv file. It takes each row of the file and makes
a list of all the columns.

'''

# Read a CSV file
"""import csv
with open('python.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'The Column names are as follows {", ".join(row)}')
            line_count += 1
        print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')

"""
# Reading csv files with Pandas

'''
The Pandas is defined as an open-source library which is built on the top of the NumPy 
library. It provides fast analysis, data cleaning, and preparation of the data for the user.

Reading the csv file into a pandas DataFrame is quick and straight forward. We don't need to 
write enough lines of code to open, analyze, and read the csv file in pandas and it stores 
the data in DataFrame.

Here, we are taking a slightly more complicated file to read, called hrdata.csv, which 
contains data of company employees.
'''

"""
import pandas
df = pandas.read_csv('hrdata.csv')
print("Data of company employess: ", df)
"""
import csv
# file1 = open('phone_dataset - Copy (1).csv','r')
# csv_file = csv.reader(file1)
# for i in csv_file:
#     print(i)
# file1.close()

# file1 = open('text1.txt','w')
file2 = open('phone_dataset - Copy (1).csv','w')
csv_file = csv.writer(file2)
# file1.close()
x = ['shiva','prasad','satish']
csv_file.writerow(x)
file2.close()

