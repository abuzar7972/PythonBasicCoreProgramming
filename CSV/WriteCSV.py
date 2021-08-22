"""
*Author : Abuzar Shaikh
*Date   : 20-08-2021
*Time   : 1 PM
*Title  : CSV file write operation
"""
import csv

# Method 1:
# with open('abc.csv', 'w') as csvfile:
#     fieldnames = ['first_name', 'last_name', 'Rank']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#
#     writer.writeheader()
#     writer.writerow({'Rank': '1', 'first_name': 'Parker', 'last_name': 'Brian'})
#     writer.writerow({'Rank': '2', 'first_name': 'Smith', 'last_name': 'Rodriguez'})
#     writer.writerow({'Rank': '3', 'first_name': 'Jane', 'last_name': 'Oscar'})
#     writer.writerow({'Rank': '4', 'first_name': 'Jane', 'last_name': 'Loive'})
#
# print("************* Writing complete ****************")

# Method 2:
class CSVFileWriter:
    @staticmethod
    def csvWriter():
        fields = ['Name', 'Branch', 'Year', 'CGPA']

        # data rows of csv file
        rows = [['Nikhil', 'COE', '2', '9.0'],
                ['Sanchit', 'COE', '2', '9.1'],
                ['Aditya', 'IT', '2', '9.3'],
                ['Sagar', 'SE', '1', '9.5'],
                ['Prateek', 'MCE', '3', '7.8'],
                ['Sahil', 'EP', '2', '9.1']]

        # name of csv file
        filename = "abc.csv"

        # writing to csv file
        with open(filename, 'w') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)

            # writing the fields
            csvwriter.writerow(fields)

            # writing the data rows
            csvwriter.writerows(rows)
        print("************* Writing complete ****************")

cSVFileWriter = CSVFileWriter()
cSVFileWriter.csvWriter()
