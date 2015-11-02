# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 15:53:47 2015

@author: tpsgroup
"""

import numpy as np
import random
from Absorb import Emit, Absorb
import matplotlib
matplotlib.use('Agg')
from thermalise import thermalise
import matplotlib.pyplot as plt

print('Declaring Variables******************************************')
amu = 1.66053904e-27;
h = 6.62607e-34;
k = 1.38064852e-23;

Mca = 40*amu;
Nion = 50; 
lmd = 396.908e-9;
tin = 100;
i = 0;
VCA = np.zeros((Nion,4)); #4th dimension = state marker
I = np.zeros(Nion);
Pemm = 1/7.0; #ensure at least one of the numbers is a float
timeint = 100
totaltime = int(1e7);
VCAtrack = VCA;
random.seed()
ttin = 1e8
VCAtime = np.zeros((Nion,(totaltime/timeint)+1))
delta = 1e7
base = 150

print('Generating initial distribution******************************')
VCAinit, VCAtrack = thermalise(VCA, VCAtrack, Nion,tin,Mca,1)
VCAinit = np.array(VCAinit)
for n in range(Nion):
    m = int(n)
    VCAinit[m][0] = (base+m)*Mca
    VCAtrack[m][0] = (base+m)*Mca

print('Initialised, running loop************************************')
counterp = 1;
counteri = 1;
countdown = 0
tmin = ttin
tmax = ttin
niterations = (totaltime/timeint)+1
Attime = np.ones(niterations)*1.0
ttrack = ttin

for time in range(0,(totaltime+timeint),timeint):

    countdown1 = (totaltime-time)/(timeint*10);
    if (countdown1 != countdown):
        print "%03d" % countdown1
    countdown = countdown1
    #tbefore = testxtemp(VCAtrack,Mca)
    for p in range(0,Nion):
        r = np.zeros(timeint*10)
        for q in range(0,timeint*10):
            r[q] = random.random()
        if (VCAtrack[p][3] != h):
            VCAtrack, number = Absorb(VCAtrack,p, Mca, lmd, r, delta);
            if number != 0:
                VCAtrack[p][3] = 1;
                np.add.at(I,p,number)
        elif (VCAtrack[p][3] == 1):
            VCAtrack, number = Emit(VCAtrack,p,lmd, Mca, r, delta);
            if number != 0:
                VCAtrack[p][3] = 0;

    for N in range(Nion):
        VCAtime[N,time/timeint] = VCAtrack[N][0]/Mca
plt.clf()
for N in range(Nion):
    plt.plot(VCAtime[N][:])
plt.savefig('delta %s' % str(delta))