"""
*Author : Abuzar Shaikh
*Date   : 20-08-2021
*Time   : 1 PM
*Title  : CSV file read operation 
"""
import pandas

class CSVFileReader:
    @staticmethod
    def csvRead():
        df = pandas.read_csv('abc.csv')
        print(df)

cSVFileReader = CSVFileReader()
cSVFileReader.csvRead()
