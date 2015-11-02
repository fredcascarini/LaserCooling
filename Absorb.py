def isoEmit(array, listb, lbda):
    import math
    import random
    
    h = 6.62607e-34;
    
    rnumu = random.random();
    rnumv = random.random();
    theta = 2 * math.pi * rnumu;
    phi = math.acos((2 * rnumv) -1);
    x = math.cos(theta)*math.sin(phi);
    y = math.sin(theta)*math.sin(phi);
    z = math.cos(phi);
    
    array[listb][0] = array[listb][0] + x * (h/lbda);
    array[listb][1] = array[listb][1] + y * (h/lbda);
    array[listb][2] = array[listb][2] + z * (h/lbda);
    
    return array
    

def Emit(array, listb, lbda, mass, r, delta):
    from fscatt import fscatt as fs
    
    v = (array[listb][0])/mass
    dt = 1.0e-9
    fscatt = fs(v, lbda, delta) #Probability of stimulated emission s^-1
    fscatt += 1.4e8 #Probability of spontaneous emission s^-1 from NIST
    fscatt *= dt
    
    number = sum(1 for item in r if item <= fscatt)    
    
    for i in range(number):
        array = isoEmit(array, listb, lbda)
    
    return array, number
    
    
def Absorb(array, lista, mass, wavelength, r, delta):
    from fscatt import fscatt as fs

    h = 6.62607e-34;
    dt = 1.0e-9
    v = (array[lista][0])/mass
    fscatt = fs(v, wavelength, delta) #Probability of stimulated absorption s^-1
    fscatt *= dt
    
    number = sum(1 for item in r if item <= fscatt)    
    
    recoil_momentum = (h/wavelength) * number
    #print(recoil_momentum)
    array[lista][0] = array[lista][0] - (number * recoil_momentum);

    return array, number