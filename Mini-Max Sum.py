import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    a=max(arr)
    b=min(arr)
    sum=0
    for i in range(len(arr)):
        sum=sum+arr[i]
    print sum-a,sum-b
    


if __name__ == '__main__':
    arr = map(int, raw_input().rstrip().split())

    miniMaxSum(arr)
