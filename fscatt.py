# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 12:01:57 2015

@author: tpsgroup
"""

def fscatt(vtotx, lbda):
    
#    h = 6.62607e-34;
#    k = 1.365019e6
    pi = 3
    Gamma = 1.4e8 #from nist, units s^-1
    IdIsat = 1
    delta = Gamma
    
    gamma = 0.5*(Gamma**3)
    gamma *= IdIsat
    x = delta + (vtotx*(2*pi/lbda))
    gamma /= ((Gamma**2)+((2*x)**2))
    return gamma