# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 15:54:38 2015

@author: tpsgroup
"""

def thermalise (Ar, Arr, N, temp, mass,init=0):
    
    import math
    from scipy.stats import chi2

    k = 1.38064852e-23;

    for d in range(0,3):
        for p in range(0,N):
            x = math.sqrt(((k * temp) / mass) * (chi2.rvs(3)));
            x = mass * x;
            Ar[[p],[d]] = x;
            
    
    for b in range(0,int(N)):
        Arr.insert(b,[float(Ar[[b],[0]]), float(Ar[[b],[1]]), float(Ar[[b],[2]]), float(Ar[[b],[3]])])

    if (init == 1):
        VCAi = Ar
        VCAi = tuple(VCAi)
        return VCAi    
    
    return