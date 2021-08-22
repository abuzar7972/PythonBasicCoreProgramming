"""
*Author : Abuzar Shaikh
*Date   : 16-08-2021
*Time   : 2PM
*Title  :2D array upto given range

"""
from array import *
from typing import Type


class TwoDimentionalArray:
    def TwoDimentionalCalculation(self):
        i=0
        matrix = []
        arr = []
        flag = True
        while flag == True:
            try:
                noOfRow = int(input("Please Enter Number of Rows::"))
                noOfColum = int(input("Please Enter Number of Coloums::"))
                if (noOfRow and noOfColum) ==0:
                    flag = False
                    raise ValueError()
                else:
                    for i in range(noOfRow):
                        for j in range(noOfColum):
                            print("Enter value for",j,"Coloum &",i,"Row::")
                            inputNumber = int(input())
                            arr.append(inputNumber)
                        matrix.append(arr)
                flag = False
            except ValueError:
                print('*********** Invalid Number ***********')
        print(arr)
        inputCheck = matrix
        for x in inputCheck:
            for y in x:
                print(y, end=" ")
            print()
twoDimentionalArray = TwoDimentionalArray()
twoDimentionalArray.TwoDimentionalCalculation()
