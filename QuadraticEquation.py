"""
*Author : Abuzar Shaikh
*Date   : 16-08-2021
*Time   : 2-30 PM
*Title  :Quadractic Equation to find real and imaginary roots

"""
import math
class QuadraticEquation:
    @staticmethod
    def calculateRoot():
        flag = True
        while flag == True:
            try:
                a = int(input("Enter Value of 'a'::"))
                b = int(input("Enter Value of 'b'::"))
                c = int(input("Enter Value of 'c'::"))
                if (a and b and c) == 0:
                    raise ValueError
                    flag = False
                else:
                    delta = (b*b) - (4*a*c)
                    print("Value of delta::", delta)
                    rootOneOfX = (-b + math.sqrt(delta))/2*a
                    print("Root 1 for X:: ", rootOneOfX)
                    rootTwoOfX = (-b - math.sqrt(delta))/2*a
                    print("Root 2 of X:: ", rootTwoOfX)
                    flag = False
            except ValueError:
                print('*********** Invalid Number ***********')

quadraticEquation = QuadraticEquation()
quadraticEquation.calculateRoot()