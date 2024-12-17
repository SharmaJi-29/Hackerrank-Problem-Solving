#!/bin/python3

import math
import os
import random
import re
import sys

def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_range = []
    orange_range = []
    
    for x in apples:
        apples_range.append(a + x)
    for x in oranges:
        orange_range.append(b + x)
     
    apple_count, orange_count = 0,0   
    for i in apples_range:
        if (s <= i <= t):
            apple_count = apple_count + 1
    for i in orange_range:
        if (s <= i <= t):
            orange_count = orange_count + 1
    print(apple_count)
    print(orange_count)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
