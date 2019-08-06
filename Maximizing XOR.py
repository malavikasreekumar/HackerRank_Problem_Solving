def maximizingXor(l, r):
    ans=0
    a=[]
    for i in range(l,r+1):
        for j in range(l,r+1):
            ans=i^j
            a.append(ans)
    return max(a)
