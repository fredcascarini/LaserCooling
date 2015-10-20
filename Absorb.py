
def Emit(array, listb, lbda, number):
    
    import math
    import random
    
    h = 6.62607e-34;
    
    for i in range(number+1):    
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
        
    return
    
def threedabs(array, lista, lbda, number, mass):
    from gaussian import gaussian as gsn
    
    c = 299792458
    h = 6.62607e-34;
    
    fwhm = 5e5
    reswave = 396.847e-9
    laswave = reswave + 0.04e-9
    resfreq = c/reswave
    lasfreq = c/laswave

    gx = gsn(fwhm, resfreq, (array[lista][0]/(mass*1.0)), lasfreq)
    
    array[lista][0] = array[lista][0] - gx * number * (h/lbda);
    
    return gx