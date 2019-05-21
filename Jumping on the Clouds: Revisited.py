def jumpingOnClouds(c, k):
    energy=100
    for i in range(0,n,k):
        energy-=(1+2*c[i])
    return energy
            
