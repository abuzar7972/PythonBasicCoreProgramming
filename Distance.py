"""
*Author : Abuzar Shaikh
*Date   : 16-08-2021
*Time   : 2PM
*Title  :Distance between two lines

"""
import math
class Distance:
    def DistanceClaculation(self):
        flag = True
        while flag == True:
            try:
                valueOfX = int(input("Enter value of 'X':: "))
                valueOfY = int(input("Enter value of 'Y':: "))
                if (valueOfY and valueOfX) == 0:
                    raise ValueError()
                    flag = False
                else:
                    num = (valueOfX*valueOfY)+(valueOfY*valueOfY)
                    distance = math.sqrt(num)
                    print("Distance Of point from the origin:: ", distance)
                    flag = False
            except ValueError:
                print('*********** Invalid Number ***********')

distance = Distance()
distance.DistanceClaculation()