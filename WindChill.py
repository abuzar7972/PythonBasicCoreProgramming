"""
*Author : Abuzar Shaikh
*Date   : 16-08-2021
*Time   : 3 PM
*Title  :Wind chill

"""
import math

class WindChill:
    @staticmethod
    def theEffectiveTemp():
        flag = True
        while flag == True:
            try:
                w = 0
                t = float(input("Enter temperature t (in Fahrenheit):: "))
                v = float(input("Enter speed v (in miles per hour)::"))
                if t>50:
                    raise ValueError
                elif 3<v<120:
                    w = 35.74 + (0.6215*t) + ((0.4275*t)-35.75) * math.pow(v,0.16)
                else:
                    raise ValueError
                    flag == False
                if flag == False:
                    return -1
                else:
                    flag = True
                    return w
            except ValueError:
                print("********* Invalid Input ************")

windChill = WindChill()
result = windChill.theEffectiveTemp()
print("The effective temperature (the wind chill)::",result)