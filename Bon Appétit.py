def bonAppetit(bill, k, b):
    sum=0
    for i in range(0,len(bill)):
        sum+=bill[i]

    payanna=(sum-bill[k])/2
    if payanna==b:
        print("Bon Appetit")
        
    else:
        print(int(b- payanna))
