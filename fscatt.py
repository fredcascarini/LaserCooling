# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 12:01:57 2015

@author: tpsgroup
"""

def fscatt():
    
    hbar = 1
    lbda = 2
    pi = 3
    k = 2*pi/lbda
    Gamma = 4.0
    IdIsat = 1
    delta = 6.0
    ddg = delta/Gamma
    
    Fscatt = hbar*k
    Fscatt *= 0.5*Gamma
    Fscatt *= IdIsat
    Fscatt /= (1 + IdIsat + 4*(ddg**2))
    
    return Fscatt