
def Emit(array, listb, lbda, number):
    
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
    array[listb][0] = array[listb][0] + number * x * (h/lbda);
    array[listb][1] = array[listb][1] + number * y * (h/lbda);
    array[listb][2] = array[listb][2] + number * z * (h/lbda);
    return
    
def threedabs(array, lista, lbda, number, mass):
    from gaussian import gaussian as gsn
    
    c = 299792458 
    
    fwhm = 5e5
    reswave = 396.847e-9
    laswave = reswave #+ 1e-14
    resfreq = c/reswave
    lasfreq = c/laswave
    delta = (lasfreq-resfreq)
    #used wavelength = 396.958901nm

    gx = gsn(fwhm, resfreq, (array[lista][0]/(mass*1.0)), delta)
    
    gt = 0
    if gx > 0:
        gt = 1

    
    h = 6.62607e-34;
    
    array[lista][0] = array[lista][0] - gx * number * (h/lbda);
    
    return gt