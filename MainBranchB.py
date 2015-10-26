# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 15:53:47 2015

@author: tpsgroup
"""

import numpy as np
import math
import random
from Absorb import Emit, Absorb
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from trendline import trendline
from thermalise import thermalise
from testxtemp import testxtemp
from plotvel import plottemp

print('Declaring Variables******************************************')
amu = 1.66053904e-27;
h = 6.62607e-34;
k = 1.38064852e-23;

Mca = 40*amu;
Nion = 20000; 
lmd = 396.908e-9;
tin = 100;
i = 0;
VCA = np.zeros((Nion,4)); #4th dimension = state marker
I = np.zeros(Nion);
Pemm = 1/7.0; #ensure at least one of the numbers is a float
timeint = 10
totaltime = int(10000);
VCAtrack = [];
random.seed()

print('Generating initial distribution******************************')
VCAinit, VCAtrack = thermalise(VCA, VCAtrack, Nion,tin,Mca,1)
ttin = testxtemp(VCAtrack,Mca)

print('Initialised, running loop************************************')
counterp = 1;
counteri = 1;
countdown = 0
tmin = ttin
tmax = ttin
niterations = (totaltime/timeint)+1
Attime = np.ones(niterations)*1.0
ttime1 = ttin
ttrack = ttin

for time in range(0,(totaltime+timeint),timeint):

    countdown1 = (totaltime-time)/(timeint*10);
    if (countdown1 != countdown):
        print "%03d" % countdown1
    countdown = countdown1
    tbefore = testxtemp(VCAtrack,Mca)
    for p in range(0,Nion):
        r = np.zeros(timeint*10)
        for q in range(0,timeint*10):
            r[q] = random.random()
        if (VCAtrack[p][3] != h):
            VCAtrack, number = Absorb(VCAtrack,p, Mca, lmd, r);
            if number != 0:
                VCAtrack[p][3] = 1;
                np.add.at(I,p,number)
        elif (VCAtrack[p][3] == 1):
            VCAtrack, number = Emit(VCAtrack,p,lmd, Mca, lmd, r);
            if number != 0:
                VCAtrack[p][3] = 0;
    tafter = testxtemp(VCAtrack,Mca)
    tdiff = tafter-tbefore
    ttrack = ttin + tdiff
    ttime = tafter
    if ttime < tmin:
        tmin = ttime
    elif ttime > tmax:
        tmax = ttime
    ttime1 = ttime
    VCAtrack = thermalise(VCA, VCAtrack, Nion,ttime,Mca)

    Attime[time/timeint] = ttrack
if tmax == tmin:
    print('no change')
elif tmin < ttin:
    print('Decreased by %e' % (ttin-tmin))
print('Varied by %f' % (tmax-tmin))

print('Running end code*********************************************')
print('Running plotvel**********************************************')
halfsize = 0.5*len(Attime)
threequartersize = halfsize * 1.5
plottemp(Attime[threequartersize:],300,1,'3')
print('Finished plotvel*********************************************')
#VCAfinal = np.array(VCAtrack)
#VCAinit = np.array(VCAinit)
#VCAdiff = np.subtract(VCAinit, VCAfinal)
#V = (VCAdiff[:,0])/Mca
#plt.figure(2)
#plt.plot(V,I,'.')
#plt.legend()
#plt.ylabel('number of photons')
#plt.xlabel('amount slowed down')
#trendline(V,I)
#meaninit = np.mean(VCAinit[:,0:3])
#Tinit = (math.pow(meaninit,2))/(3*k*Mca)
#meanend = np.mean(VCAfinal[:,0:3])
#Tend = (math.pow(meanend,2))/(3*k*Mca)
#meandiff = np.mean(VCAdiff[:,0:3])
