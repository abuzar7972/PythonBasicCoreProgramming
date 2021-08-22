"""
*Author : Abuzar Shaikh
*Date   : 20-08-2021
*Time   : 1 PM
*Title  : JSON read
"""
import json


class CSVFileReader:
    @staticmethod
    def csvFileReader():
        with open('abc.json') as f:
            data = json.load(f)

        print(data)


cSVFileReader = CSVFileReader()
cSVFileReader.csvFileReader()
