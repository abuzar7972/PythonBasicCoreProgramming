import json


class CSVFileReader:
    @staticmethod
    def csvFileReader():
        with open('abc.json') as f:
            data = json.load(f)

        print(data)


cSVFileReader = CSVFileReader()
cSVFileReader.csvFileReader()
