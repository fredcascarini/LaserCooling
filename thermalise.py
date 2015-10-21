# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 15:54:38 2015

@author: tpsgroup
"""

def thermalise (Ar, Arr, N, temp, mass,init=0):
    
    import math
    from scipy.stats import norm
    import numpy as np
    from scipy.interpolate import UnivariateSpline
    import matplotlib.pyplot as plt
    from testxtemp import testxtemp

    k = 1.38064852e-23;
    
    tempinit = temp
    for d in range(0,3):
        for p in range(0,N):
            sc = math.sqrt((k*temp)/mass)
            x = norm.rvs(scale = sc);
            x = mass * x;
            Ar[[p],[d]] = x;
    
    tempend = testxtemp(Ar,mass)
    
    print(tempinit-tempend)
            
    p, x = np.histogram(sorted(Ar[:,0]), bins = 50)
    x = x[:-1] + (x[1]-x[0])/2
    n= 100
    f = UnivariateSpline(x,p,s=n)
    plt.plot(x,f(x),'.', label='%e' % temp)
    plt.legend()
    
    Arr = []
    for b in range(0,int(N)):
        Arr.insert(b,[float(Ar[[b],[0]]), float(Ar[[b],[1]]), 
                      float(Ar[[b],[2]]), float(Ar[[b],[3]])])

    
    if (init == 1):
        VCAi = Ar
        VCAi = tuple(VCAi)
        return VCAi, Arr  
    
    return Arr