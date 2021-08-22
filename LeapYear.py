"""
*Author : Abuzar Shaikh
*Date   : 17-08-2021
*Time   : 5 PM
*Title  : Leap Year

"""
class LeapYear:
    def LeapYearCalcualtion(self):
        inputNumber = int(input("Please Enter Number ot Check Leap Year:: "))
        try:
            if inputNumber<999:
                raise ValueError("********** Invalid Input *********")
            elif inputNumber>9999:
                raise ValueError("********** Invalid Input *********")
            else:
                if inputNumber%4 == 0:
                    print(+inputNumber, "is a Leap Year")
                else:
                    print(+inputNumber, "is Not a Leap Year")
        except ValueError as e:
            print(e)
leapYear = LeapYear()
leapYear.LeapYearCalcualtion()