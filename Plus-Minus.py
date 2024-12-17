#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    a=0
    b=0
    c=0
    arr = list(arr)
    for i in arr:
        if i > 0 :
            a += 1
        elif i < 0:
            b += 1
        elif i == 0:
            c += 1
    print(f"{a/len(arr):.6f}")
    print(f"{b/len(arr):.6f}")
    print(f"{c/len(arr):.6f}")
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
