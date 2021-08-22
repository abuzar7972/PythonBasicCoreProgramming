class TextFileRead:
    @staticmethod
    def textRead():
        with open("abc.txt", 'r') as file:
            contentInFile = file.read();
            print("Content in file\n", contentInFile)

        # Read File by Using readLine Functon

        fileOpne = open("abc.txt", 'r');
        fileContent = fileOpne.readline()
        print("File handling by read line function::", fileContent)
        fileOpne.close()

textFileRead = TextFileRead()
textFileRead.textRead()