# Since Apr 10 2013

import operator
from collections import OrderedDict

import pylab

#d = OrderedDict()
d = {}
with open('problemset4/words.txt') as f:
    for word in f:
        ini = word[0]
        ini = len(word)
        if ini in d:
            d[ini] += 1
        else:
            d[ini] = 1
print d
#d = dict(sorted(d.items(), key=lambda t: t[0]))
#d = sorted(d.iteritems(), key=operator.itemgetter(0))
#print d

def draw():
    global d
    pylab.figure(1)
    pylab.bar(range(len(d)), d.values())
    pylab.title('Number of words starting with each letter')
    pylab.xlabel('First letter of words')
    pylab.ylabel('Word numbers')
    pylab.xticks(range(len(d)), d.keys())
    pylab.grid()
    pylab.show()

draw()
