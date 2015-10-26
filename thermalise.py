# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 15:54:38 2015

@author: tpsgroup
"""

def thermalise (Ar, Arr, N, temp, mass,init=0):
    
    import math
    from scipy.stats import norm
    import numpy as np

    k = 1.38064852e-23;
    #while (int(0.1*y) != int(0.1*temp)):   
    for d in range(0,3):
        for p in range(0,N):
            sc = math.sqrt((k*temp)/mass)
            x = norm.rvs(scale = sc);
            x = mass * x;
            Ar[[p],[d]] = x;
        
    Arr = []
    for b in range(0,int(N)):
        Arr.insert(b,[float(Ar[[b],[0]]), float(Ar[[b],[1]]), 
                      float(Ar[[b],[2]]), float(Ar[[b],[3]])])
    
    if (init == 1):
        Arry = tuple(Arr)
        for p in range(0,N):
            randbool = np.random.choice([0,1])
            Ar[[p],[3]] = randbool
        return Arry, Arr  
    
    return Arr