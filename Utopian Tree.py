def utopianTree(n):
    h=1
    for i in range(0,n):
        if i%2==0:
            h=h*2
        else:
            h+=1
    return h
