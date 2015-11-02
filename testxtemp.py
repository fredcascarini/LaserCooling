# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 09:36:03 2015

@author: tpsgroup
"""

def testxtemp(tup, mass):
    import numpy as np
        
    k = 1.38064852e-23;
    
    num = np.array(tup)
    vel = num/mass
    stdattime = np.std(vel[:,0], dtype=np.float64)
    ttime = (stdattime**2)*(mass/k)
    #print(ttime)
    return ttime
    