# Since Apr 16 2013

import random


def noReplacementSimulation(numTrials):
    BALLS = ['r', 'r', 'r', 'g', 'g', 'g']
    yes = 0
    for i in range(numTrials):
        balls = BALLS[:]
        three_balls = []
        for i in range(3):
            index = random.choice(range(len(balls)))
            three_balls.append(balls.pop(index))
        if three_balls in (['r'] * 3, ['g'] * 3):
            yes += 1
    return yes/float(numTrials)

print noReplacementSimulation(100000)
