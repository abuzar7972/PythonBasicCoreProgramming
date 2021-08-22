"""
*Author : Abuzar Shaikh
*Date   : 17-08-2021
*Time   : 5 PM
*Title  : Flip coin simulation at given range and their percentage

"""
import random
import string

Heads = 'Heads'
Tails = 'Tails'
noOfHead = 0
noOfTails = 0

def flipCoin():
    randomCheck = random.uniform(0,1)
    return Heads if randomCheck<0.5 else Tails

try:
    inputNumber = int(input("Enter Number of Flips::"))
    if inputNumber<=0:
        raise ValueError("************* Invalid Input ********** ")
    else:
        for i in range(0,inputNumber):
            outPut = flipCoin()
            if outPut == 'Heads':
                noOfHead += 1
            else:
                noOfTails += 1
            print(flipCoin())

except ValueError as e:
    print(e)

try:
    if (noOfTails and noOfHead) == 0:
        raise ZeroDivisionError("********Please give another number*******")
    else:
        percentageOfHeads = noOfHead*100/inputNumber
        percentageOfTails = noOfTails*100/inputNumber
        print("Total number of Heads:: ", +noOfHead)
        print("Total number of Tails:: ", +noOfTails)
        print("Percentage of Heads:: ", +percentageOfHeads)
        print("Percentage of Tails:: ", +percentageOfTails)

except ZeroDivisionError as e:
    print(e)



