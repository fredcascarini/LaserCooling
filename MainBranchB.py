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

print('Declaring Variables******************************************')
amu = 1.66053904e-27;
h = 6.62607e-34;
k = 1.38064852e-23;

Mca = 40*amu;
Nion = 2000;
lmd = 396.908e-9;
tin = 4;
i = 0;
VCAI = np.zeros((Nion,4)); #4th dimension = state marker
I = np.zeros(Nion);
Pabs = 1;
Pemm = 1/7.0; #ensure at least one of the numbers is a float
timeint = 10;
totaltime = 1000;
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

for time in range(0,(totaltime+timeint),timeint):

    countdown1 = (totaltime-time)/(timeint*10);
    if (countdown1 != countdown):   
        print "%03d" % countdown1
    countdown = countdown1

    for p in range(0,Nion):
#        r = np.zeros(timeint*10)
#        for q in range(0,timeint*10):
#            r[q] = random.random()
        if (VCAID[p][3] != h):
#            number = sum(1 for item in r if item <= Pabs)
            gt, VCAID = Absorb(VCAID,p,lmd, 1000 , Mca);
#            if (gt != 0.0):
#                VCAID[p][3] = 1;
            gt = 1 #*= number
            np.add.at(I,p,gt)
#        elif (VCAID[p][3] == 1):
#            number = sum(1 for item in r if item <= Pemm)
#            Emit(VCAID,p,lmd, number);
#            VCAID[p][3] = 0;

    ttime = testxtemp(VCAID,Mca)
    if ttime < tmin:
        tmin = ttime
    elif ttime > tmax:
        tmax = ttime

    #VCAID = thermalise(VCAI, VCAID, Nion,ttime,Mca)
if tmax == tmin:
    print('no change')
elif tmin < ttin:
    print('Decreased by %e' % (ttin-tmin))
print('Varied by %f' % (tmax-tmin))
#print('Running end code*********************************************')
#VCAIDnum = np.array(VCAID)
#VCAIDdiff = np.zeros((Nion,4));
#VCAIi = np.array(VCAIi)
#np.subtract(VCAIi, VCAIDnum, VCAIDdiff)
#V = (VCAIDdiff[:,0])/Mca
#plt.figure(2)
#plt.plot(V,I,'.')
#plt.legend()
#plt.ylabel('number of photons')
#plt.xlabel('amount slowed down')
#trendline(V,I)
#meaninit = np.mean(VCAIi[:,0:3])
#Tinit = (math.pow(meaninit,2))/(3*k*Mca)
#meanend = np.mean(VCAIDnum[:,0:3])
#Tend = (math.pow(meanend,2))/(3*k*Mca)
#meandiff = np.mean(VCAIDdiff[:,0:3])