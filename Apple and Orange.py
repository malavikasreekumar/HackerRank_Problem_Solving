def countApplesAndOranges(s, t, a, b, apples, oranges):
    app=[]
    org=[]
    cn1=0
    cn2=0
    for i in range(0,m):
        app.append(a+apples[i])

    for j in range(0,n):
        org.append(b+oranges[j])

    for k in range(0,m):
        if app[k]>=s and app[k]<=t:
            cn1=cn1+1
        else:
            continue
            
    for k in range(0,n):
        if org[k]>=s and org[k]<=t:
            cn2=cn2+1
        else:
            continue
    print(cn1)
    print(cn2)
  
