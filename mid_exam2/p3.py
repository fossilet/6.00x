#! /usr/bin/env python


'''
https://www.edx.org/courses/MITx/6.00x/2013_Spring/courseware/Exam_2/S2013_Exam_2/

Since May 5 2013
'''

import random
import threading

import pylab

total = 1000
num_trials = 300

balls = [0, 1] * (total/2)
random.shuffle(balls)  # 0: black, 1: white


def lv_choose_ball(balls):
    '''Choose a ball using LV method..
    '''
    num_choices = 0
    while True:
        num_choices += 1
        if random.choice(balls) == 1:
            break
    return num_choices

res = [lv_choose_ball(balls) for i in range(num_trials)]
pylab.hist(res, bins=max(res))
pylab.show()
