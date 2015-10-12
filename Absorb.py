
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
    
    fwhm = 5000*5e5
    reswave = 396.847e-9
    laswave = 396.859e-9
    resfreq = c/reswave
    lasfreq = c/laswave
    delta = (lasfreq/resfreq)-1
    #used wavelength = 396.958901nm

    gx = gsn(fwhm, resfreq, (array[lista][0]/(mass*1.0)), delta)
    gy = gsn(fwhm, resfreq, (array[lista][1]/(mass*1.0)), delta)
    gz = gsn(fwhm, resfreq, (array[lista][2]/(mass*1.0)), delta)
    
    gt = gx + gy + gz
    
    h = 6.62607e-34;
    array[lista][0] = array[lista][0] - gx * number * (h/lbda);
    array[lista][1] = array[lista][1] - gy * number * (h/lbda);
    array[lista][2] = array[lista][2] - gz * number * (h/lbda);
    
    return gt