# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 15:53:47 2015

@author: tpsgroup
"""

import numpy as np
import math
import random
from Absorb import Emit, Absorb
import matplotlib.pyplot as plt
from trendline import trendline
from thermalise import thermalise
from testxtemp import testxtemp
from plotvel import plotvel

print('Declaring Variables******************************************')
amu = 1.66053904e-27;
h = 6.62607e-34;
k = 1.38064852e-23;

Mca = 40*amu;
Nion = 200;
lmd = 396.908e-9;
tin = 15;
i = 0;
VCAI = np.zeros((Nion,4)); #4th dimension = state marker
I = np.zeros(Nion);
Pemm = 1/7.0; #ensure at least one of the numbers is a float
timeint = 1
totaltime = int(10000);
VCAID = [];
random.seed()

print('Generating initial distribution******************************')
VCAIi, VCAID = thermalise(VCAI, VCAID, Nion,tin,Mca,1) 
ttin = testxtemp(VCAID,Mca) 
  
print('Initialised, running loop************************************')
counterp = 1;
counteri = 1;
countdown = 0
tmin = 1e10
tmax = 0
niterations = (totaltime/timeint)+1
Attime = np.ones(niterations)*1.0

for time in range(0,(totaltime+timeint),timeint):

    countdown1 = (totaltime-time)/(timeint*10);
    if (countdown1 != countdown):   
        print "%03d" % countdown1
    countdown = countdown1

    for p in range(0,Nion):
        r = np.zeros(timeint*10)
        for q in range(0,timeint*10):
            r[q] = random.random()
        if (VCAID[p][3] != h):
            VCAID, number = Absorb(VCAID,p, Mca, lmd, r);
            VCAID[p][3] = 1;
            gt = number
            np.add.at(I,p,gt)
        elif (VCAID[p][3] == 1):
            VCAID, number = Emit(VCAID,p,lmd, Mca, lmd, r);
            VCAID[p][3] = 0;

    ttime = testxtemp(VCAID,Mca)
    if ttime < tmin:
        tmin = ttime
    elif ttime > tmax:
        tmax = ttime

    VCAID = thermalise(VCAI, VCAID, Nion,ttime,Mca)

    Attime[time] = ttime   
if tmax == tmin:
    print('no change')
elif tmin < ttin:
    print('Decreased by %e' % (ttin-tmin))
print('Varied by %f' % (tmax-tmin))

print('Running end code*********************************************')
plotvel(Attime,300)
VCAIDnum = np.array(VCAID)
VCAIi = np.array(VCAIi)
VCAIDdiff = np.subtract(VCAIi, VCAIDnum)
V = (VCAIDdiff[:,0])/Mca
plt.figure(2)
plt.plot(V,I,'.')
plt.legend()
plt.ylabel('number of photons')
plt.xlabel('amount slowed down')
trendline(V,I)
meaninit = np.mean(VCAIi[:,0:3])
Tinit = (math.pow(meaninit,2))/(3*k*Mca)
meanend = np.mean(VCAIDnum[:,0:3])
Tend = (math.pow(meanend,2))/(3*k*Mca)
meandiff = np.mean(VCAIDdiff[:,0:3])