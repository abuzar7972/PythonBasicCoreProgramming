"""
*Author : Abuzar Shaikh
*Date   : 17-08-2021
*Time   : 5 PM
*Title  : Table of 2 upto given value

"""
class PowerOfTwo:
    def PowerCalculation(self):
        inputNumber = int(input("Enter Number to Calculate Table::"))
        try:
            if inputNumber>31:
                raise ValueError("********** Invalid Input *********")
            elif inputNumber<0:
                raise ValueError("********** Invalid Input *********")
            else:
                for i in range(1,inputNumber+1):
                    table = 2*i
                    print("2 ^",i,":",table)
        except ValueError as e:
            print(e)
powerOfTwo = PowerOfTwo()
powerOfTwo.PowerCalculation()