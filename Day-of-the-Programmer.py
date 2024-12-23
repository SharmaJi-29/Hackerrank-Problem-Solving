#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#

def dayOfProgrammer(year):
    
    #Function for Leap Year
    def IsLeapYear(year):
        IsLeap = False 
        if year > 1918:
            if year%400 == 0:
                IsLeap = True
            elif year%4 == 0 and year%100 != 0:
                IsLeap = True
        else:
            if year%4 == 0:
                IsLeap = True
        return IsLeap
        
    if year != 1918:
        if IsLeapYear(year) == True:
            date = 12
        else:
            date = 13
    else:
        date = 26
    
    result = str(str(date) + '.09.' + str(year))
    return result
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
