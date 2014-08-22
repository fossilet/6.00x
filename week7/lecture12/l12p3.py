# Since Apr 10 2013
import pylab

f = open('julyTemps.txt')
hi, lo = [], []
for line in f:
    fields = line.split()
    if len(fields) == 3 and fields[0].isdigit():
        hi.append(fields[1])
        lo.append(fields[2])

diffs = [int(hi[i]) - int(lo[i]) for i in range(len(hi))]
pylab.figure(1)
pylab.plot(diffs, 'bo-')
pylab.title('Temperature Ranges in Boston in July 2012')
pylab.xlabel('Days')
pylab.ylabel('Temperature Ranges')
pylab.show()
