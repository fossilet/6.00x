# Since Apr 10 2013

import pylab

f = open('julyTemps.txt')
hi, lo = [], []
for line in f:
    fields = line.split()
    if len(fields) == 3 and fields[0].isdigit():
        hi.append(fields[1])
        lo.append(fields[2])

pylab.figure(1)
pylab.plot(range(len(hi)), lo, 'bo-', hi, 'r*-')
pylab.title('Maximum and Minimum Temperatures in Boston in July 2012')
pylab.xlabel('Days')
pylab.ylabel('Temperatures')
pylab.legend(('Minimum', 'Maximum'))
pylab.show()
