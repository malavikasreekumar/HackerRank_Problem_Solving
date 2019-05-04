import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    for i in range(0,len(ar)):
        first=ar[i]
        
        for j in range(i+1,len(ar)):
            if ar[j]==first:
                cnt=cnt+1
            
    return ar.count(max(ar))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
