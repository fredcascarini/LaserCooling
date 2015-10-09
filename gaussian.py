# -*- coding: utf-8 -*-
"""
Created on Thu Oct 08 11:30:31 2015

@author: tpsgroup
"""
def gaussian(f,r,v,d):
    #f = fwhm r = resonant freq  v = velocity  d = detuning = (new freq/r)/r
    
    import math
    import numpy as np

    c = 299792458 

    while True:    
        try:
            g = np.float_(1)
            g *= math.pow(f,2)
            g /= -1*(16.0 * (math.log(2)))
            diff= r*((v/c)-d)
            g *= math.pow(diff,2)
            g = math.exp(g)            
            break
        except OverflowError:
            g = 0
            break
    return g