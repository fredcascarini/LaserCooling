# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 15:53:47 2015

@author: tpsgroup
"""

import numpy as np
import math
import random
from Absorb import Emit, threedabs
import matplotlib.pyplot as plt
from trendline import trendline
from thermalise import thermalise
from testxtemp import testxtemp

print('Declaring Variables******************************************')
amu = 1.66053904e-27;
h = 6.62607e-34;
k = 1.38064852e-23;

Mca = 40*amu;
Nion = 200;
lmd = 396.908e-9;
tin = 60;
i = 0;
a = math.sqrt(k*tin/Mca);
VCAI = np.zeros((Nion,4)); #4th dimension = state marker
I = np.zeros(Nion);
Pabs = 0.5;
Pemm = 1.0/7.0; #ensure at least one of the numbers is a float
timeint = 1;
totaltime = 100;
VCAID = [];

print('Generating initial distribution******************************')
VCAIi, VCAID = thermalise(VCAI, VCAID, Nion,tin,Mca,1)
    
print('Initialised, running loop************************************')
counterp = 1;
counteri = 1;
countdown = 0
    
for time in range(0,(totaltime+timeint),timeint):
    countdown1 = (totaltime-time+1)/(10*timeint);
    if (countdown1 != countdown):   
        print "%03d"% countdown1
    countdown = countdown1
    for p in range(0,Nion):
        random.seed()
        r = np.zeros(timeint)
        for q in range(0,timeint):
            r[q] = random.random()
        if (VCAID[p][3] == 0):
            rabs = random.random();
            number = sum(1 for item in r if item <= Pabs)
#            gt = threedabs(VCAID,p,lmd, number, Mca);
#            if (gt != 0.0):
#                VCAID[p][3] = 1;
#            gt *= number
            np.add.at(I,p,1)
        elif (VCAID[p][3] == 1):
            number = sum(1 for item in r if item <= Pemm)
#            Emit(VCAID,p,lmd, number);
            VCAID[p][3] = 0;
    print('********************************')
    #VCAID = thermalise(VCAI, VCAID, Nion,ttime,Mca)
    
print('Running end code*********************************************')
VCAIDnum = np.array(VCAID)
VCAIDdiff = np.zeros((Nion,4));
VCAIi = np.array(VCAIi)
np.subtract(VCAIi, VCAIDnum, VCAIDdiff)
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
