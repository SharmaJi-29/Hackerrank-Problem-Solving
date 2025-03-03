#!/bin/python3

import os
import sys


#
# Complete the catAndMouse function below.
#
def catAndMouse(x, y, z):
    dist_catA = abs(x - z)
    dist_catB = abs(y - z)
    
    if dist_catA == dist_catB:
        return 'Mouse C'
        
    elif dist_catA < dist_catB:
        return 'Cat A'
    
    elif dist_catB < dist_catA:
        return 'Cat B'


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        f.write(result + '\n')

    f.close()
