def hurdleRace(k, height):
    a=max(height)
    for i in range(0,len(height)):
        if a<=k:
            maxi=1
        else:
            return a-k
        
    if maxi==1:
        return 0
