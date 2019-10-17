def angryProfessor(k, a):
    cnt=0
    for i in range(0,len(a)):
        if a[i]<=0:
            cnt=cnt+1
    
    if cnt>=k:
        return "NO"
    else:
        return "YES"
# This is a comment.
