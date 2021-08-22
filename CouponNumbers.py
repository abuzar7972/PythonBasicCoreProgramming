"""
*Author : Abuzar Shaikh
*Date   : 16-08-2021
*Time   : 10-30 AM
*Title  :Generating different coupon numbers up to given range

"""

import math
import random

class CoupenNumber:
    @staticmethod
    def randomCoupon():
        i=0
        flag = True
        couponList = []
        noOfCoupon = int(input("How Many Coupons You want to generate?"))
        while noOfCoupon>=(i+1):
            randomNumber = random.randrange(1,100)
            if (not (couponList.__contains__(randomNumber))):
                couponList.append(randomNumber)
                i += 1
            elif noOfCoupon:
                flag = False
            else:
                print("No contain")
            print(couponList)

coupenNumber = CoupenNumber()
coupenNumber.randomCoupon()