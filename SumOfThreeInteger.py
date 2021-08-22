"""
*Author : Abuzar Shaikh
*Date   : 16-08-2021
*Time   : 2-30 PM
*Title  :Calculated sum of three intger equals to zero

"""
class Triplets:

    def find_triples(Self,arr, n):

        #local variable
        found = True
        count = 0

        for i in range(0, n - 2):

            for j in range(i + 1, n - 1):

                for k in range(j + 1, n):

                    if arr[i] + arr[j] + arr[k] == 0:
                        print(arr[i], arr[j], arr[k])
                        found = True
                        count = count + 1

        print("The number of triples are:: ", count)

        if not found:
            print(" not exist ")

#object
obj = Triplets()

while True:
    try:
        array = []
        length = int(input("Enter length of array:: "))
        for i in range(length):
            temp = int(input("Enter numbers:: "))
            array.append(temp)
        obj.find_triples(array, length)
        break

    except ValueError:
        print("Check the input")
        continue