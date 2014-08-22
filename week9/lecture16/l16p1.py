#! /usr/bin/env python

'''
Monte Carlo simulation of sum of rolling serveral 6-sided dice

Since Apr 26 2013
'''

import random
from collections import Counter
import math

import pylab

num_dice = 9  # number of dices to toss
sides = 6  # number of sides on a die
num_trials = 10000

pylab.figure(1)
for die in range(1, num_dice + 1):
    res, legend = [], []
    for i in range(num_trials):
        sum_ = 0
        for i in range(die):
            side = random.choice(range(1, sides + 1))
            sum_ += side
        res.append(sum_)
    data = sorted(Counter(res).most_common())
    x, y = [], []
    for t in data:
        x.append(t[0]), y.append(t[1])
    pylab.ylim(ymin=0)
    pylab.subplot(int(math.ceil(num_dice / 2.)), 2, die)
    pylab.plot(x, y, 'b*-')
pylab.figtext(0.5, 0.95, 'Sum of rolling %(num_dice)d fair %(sides)d-sided '
              'dice in %(num_trials)d trials' % locals(), ha='center')
pylab.show()
