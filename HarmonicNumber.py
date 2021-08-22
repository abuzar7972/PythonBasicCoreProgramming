"""
*Author : Abuzar Shaikh
*Date   : 17-08-2021
*Time   : 5-30 PM
*Title  : Harmonic numbers upto N

"""
class HarmonicNumber:
    def CheckHarmonic(self):
        try:
            inputNumber = int(input("Enter Number to Calculate Harmonic::"))
            if inputNumber!=0:
                print("The total Harmonic of", inputNumber, "Are::")
                for i in range(1,inputNumber+1):
                    print("1/",i,'+', end=" ")
            else:
                raise ValueError("*********** Invalid Input *************")
        except ValueError as e:
            print(e)
harmonicNumber = HarmonicNumber()
harmonicNumber.CheckHarmonic()