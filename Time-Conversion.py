#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    format = s[-2:]
    if format == 'AM':
        if s[:2] == '12':
            x = '00'
            return x + s[2:-2]
        return s[:-2]
    elif format == 'PM':
        if s[:2]=='12':
            return (s[:-2])
        x = str(int(s[:2])+12) 
        s = x + s[2:-2] 
        return s
        
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
