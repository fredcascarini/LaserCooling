# -*- coding: utf-8 -*-
"""
Created on Wed Oct 07 15:06:17 2015

@author: tpsgroup
"""

import numpy as np
import math
from scipy.stats import chi2
import random
from Absorb import Emit, threedabs
import matplotlib.pyplot as plt
from trendline import trendline

amu = 1.66053904e-27;
h = 6.62607e-34;
k = 1.38064852e-23;

Mca = 40*amu;
Nion = 50;
lmd = 396.958e-9;
tin = 298;
i = 0;
a = math.sqrt(k*tin/Mca);
VCAI = np.zeros((Nion,4)); #4th dimension = state marker
I = np.zeros(Nion);
Pabs = 0.5;
Pemm = 1.0/7.0; #ensure at least one of the numbers is a float
timeint = 1;
totaltime = 2000;

for d in range(0,3):
    for p in range(0,Nion):
        x = math.sqrt(((k * tin) / Mca) * (chi2.rvs(3)));
        x = Mca * x;
        VCAI[[p],[d]] = x;

VCAIinit = VCAI;
VCAID = []

for b in range(0,int(Nion)):
    VCAID.insert(b,[float(VCAI[[b],[0]]), float(VCAI[[b],[1]]), float(VCAI[[b],[2]]), float(VCAI[[b],[3]])])

counterp = 1;
counteri = 1;
countdown = 0

for time in range(0,(totaltime+timeint),timeint):
    countdown1 = (totaltime-time+1)/(10*timeint);
    if (countdown1 != countdown):   
        print(countdown1)
    countdown = countdown1
    for p in range(0,Nion):
        random.seed()
        r = np.zeros(timeint)
        for q in range(0,timeint):
            r[q] = random.random()
        if (VCAID[p][3] == 0):
            rabs = random.random();
            number = sum(1 for item in r if item <= Pabs)
            gt = threedabs(VCAID,p,lmd, number, Mca);
            if (gt != 0.0):
                VCAID[p][3] = 1;
                np.add.at(I,p,number)
        elif (VCAID[p][3] == 1):
            number = sum(1 for item in r if item <= Pemm)
            Emit(VCAID,p,lmd, number);
            VCAID[p][3] = 0;

VCAIDnum = np.array(VCAID)
VCAIDdiff = np.zeros((Nion,4));
np.subtract(VCAIinit, VCAIDnum, VCAIDdiff)
V = (VCAIDdiff[:,0])/Mca
plt.plot(V,I,'.')
plt.ylabel('number of photons')
plt.xlabel('amount slowed down')
trendline(V,I)
meaninit = np.mean(VCAIinit[:,0:3])
Tinit = (math.pow(meaninit,2))/(3*k*Mca)
meanend = np.mean(VCAIDnum[:,0:3])
Tend = (math.pow(meanend,2))/(3*k*Mca)
meandiff = np.mean(VCAIDdiff[:,0:3])
