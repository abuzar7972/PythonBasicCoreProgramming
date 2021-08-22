"""
*Author : Abuzar Shaikh
*Date   : 16-08-2021
*Time   : 11 AM
*Title  :Gambler Problem

"""

import random

class Gambler:
    def mainMethod(self):
        noOfWon = 0
        noOfLose = 0
        initialMoney = int(input("Enter initial Ammount:: "))
        goal = int(input("Enter goal:: "))
        flag = True
        noOfRandom = 0
        goalCheck = initialMoney

        while flag:
            betAmmount = int(input("Enter Betting Ammount::"))
            randomCheck = random.uniform(0,1)
            requiredMoney = initialMoney-betAmmount
            noOfRandom += 1
            if initialMoney<0:
                flag = False
                break
            elif initialMoney==goal:
                break
            elif requiredMoney<0:
                print("\n********* Not Enough Money *********")
                print("Money Available:: ", +initialMoney)
                break
            elif goal<goalCheck:
                print("********** Invalid Goal **********")
            elif randomCheck<0.5:
                print("Lose")
                initialMoney = initialMoney-betAmmount
                noOfLose += 1
            else :
                print("Won")
                initialMoney = initialMoney+betAmmount
                noOfWon += 1

        wonPercentage = (noOfWon*100)/noOfRandom
        losePercentage = (noOfLose*100)/noOfRandom
        print("At the end of game Total Money::", +initialMoney)
        print("Won Percentage::", +wonPercentage)
        print("Lose Percentage::", +losePercentage)

gambler = Gambler()
gambler.mainMethod()