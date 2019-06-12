def icecreamParlor(m, arr):
    for i in range(0,len(arr)-1):
        for j in range(1,len(arr)):
            if arr[i]+arr[j]==m and j>i:
                return i+1,j+1
