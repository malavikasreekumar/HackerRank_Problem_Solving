import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    c1=c2=c3=0
    for i in range(len(arr)):
        if arr[i]<0:
            c1=c1+1
        elif arr[i]>0:
            c2=c2+1
        else:
            c3=c3+1
    a=c1/len(arr)
    b=c2/len(arr)
    c=c3/len(arr)

    
    print('%.6f'% b)
    print('%.6f'% a)
    print('%.6f'% c)
    return b,a,c

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
