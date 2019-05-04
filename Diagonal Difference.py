import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr,n):
    l=sum(arr[i][i] for i in range(n))
    r = sum(arr[i][n-i-1] for i in range(n))
    return abs(l-r)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr,n)

    fptr.write(str(result) + '\n')

    fptr.close()
