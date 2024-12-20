#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    highest_score_count = 0
    lowest_score_count = 0
    highest_score = scores[0]
    lowest_score = scores[0]
    
    for i in range(1, len(scores)):
        if scores[i] > highest_score:
            highest_score = scores[i]
            highest_score_count += 1
        elif scores[i] < lowest_score:
            lowest_score = scores[i]
            lowest_score_count += 1
            
    result = [highest_score_count, lowest_score_count]
    
    return result
            
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
