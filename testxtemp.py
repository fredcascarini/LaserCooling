# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 09:36:03 2015

@author: tpsgroup
"""

def testxtemp(tup, mass):
    import numpy as np
    import math
    
    #used for debugging/testing
    
    k = 1.38064852e-23;
    
    num = np.array(tup)
    meanattime = np.mean(num[:,0])
    ttime = (math.pow(meanattime,2))/(k*mass)
    print(ttime)
    return