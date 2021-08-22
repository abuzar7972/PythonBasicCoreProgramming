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