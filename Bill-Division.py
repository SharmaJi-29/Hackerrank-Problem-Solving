#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    #Calculating total cost of the bill
    total_cost = 0
    for i in bill:
        total_cost += i
    split_cost = total_cost - bill[k]
    #Actual cost of the bill 
    b_actual = split_cost // 2
    #Output condition
    if (b == b_actual):
        print("Bon Appetit")
    else :
        print(b - b_actual)
        

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
