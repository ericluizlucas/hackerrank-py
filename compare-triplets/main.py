import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    aScore = 0
    bScore = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            if a[i] > b[i]:
                aScore += 1
            else:
                bScore += 1
    return [aScore, bScore]

if __name__ == '__main__':
    a = [1, 2, 3]

    b = [3, 2, 1]

    result = compareTriplets(a, b)
    print(result)
