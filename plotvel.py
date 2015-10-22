# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 10:14:34 2015

@author: tpsgroup
"""

def plottemp(A, smoothing):
    import numpy as np
    from scipy.interpolate import spline
    import matplotlib.pyplot as plt

    Aindex = range(0,(len(A)))    
    Aindex = np.array(Aindex)
    xnew = np.linspace(Aindex.min(),Aindex.max(),smoothing)
    A_smooth = spline(Aindex,A,xnew)
    
    plt.plot(xnew,A_smooth)
    plt.show()