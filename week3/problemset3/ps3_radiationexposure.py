def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)


def radiationExposure(start, stop, step):
    l = [start + k * step for k in range(int((stop - start) / step))]
    print sum(f(x) * step for x in l)
        
radiationExposure(0, 5, 1)
radiationExposure(5, 11, 1)
radiationExposure(0, 11, 1)
radiationExposure(40, 100, 1.5)
radiationExposure(0, 3, 0.1)
