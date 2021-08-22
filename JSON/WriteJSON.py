import json


class CSVFileWrite:
    @staticmethod
    def csvwrite():
        student = {
            "Name": "Peter",
            "Roll_no": "0090014",
            "Grade": "A",
            "Age": 20,
            "Subject": ["Computer Graphics", "Discrete Mathematics", "Data Structure"]
        }

        with open("abc.json", "w") as write_file:
            json.dump(student, write_file)
        print("************* Writing complete ****************")


cSVFileWrite = CSVFileWrite()
cSVFileWrite.csvwrite()
