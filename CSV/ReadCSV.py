import pandas

class CSVFileReader:
    @staticmethod
    def csvRead():
        df = pandas.read_csv('abc.csv')
        print(df)

cSVFileReader = CSVFileReader()
cSVFileReader.csvRead()