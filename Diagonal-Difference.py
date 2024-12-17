#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    n = len(arr)
    left_diagonal = []
    right_diagonal = []
    
    for i in range(0, n):
        left_diagonal.append(arr[i][i])
    arr = arr[::-1]
    for i in range(0, n):
        right_diagonal.append(arr[i][i])
        
    absolute_sum = abs(sum(left_diagonal) - sum(right_diagonal))
    return absolute_sum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()