import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    cnt=0
    a=[int(i) for i in str(n)]
    print(a)
    for i in range(0,len(a)):
        if a[i]!=0:
            if n%a[i]==0:
             cnt=cnt+1
        else:
            cnt=cnt+0

    return cnt
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
