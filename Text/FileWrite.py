"""
*Author : Abuzar Shaikh
*Date   : 20-08-2021
*Time   : 4 PM
*Title  : Text file write
"""
class TextFileWriter:
    @staticmethod
    def textWriter():
        filePtr = open('abc.txt', 'w')

        filePtr.write("Abuzar")
        filePtr.write("\nAmjad")
        filePtr.write("\nShaikh")
        print("************* Writing complete ****************")

textFileWriter = TextFileWriter()
textFileWriter.textWriter()
