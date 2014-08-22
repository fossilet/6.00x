import random
import pylab

# Global Variables
MAXRABBITPOP = 1000
CURRENTRABBITPOP = 500
CURRENTFOXPOP = 30


def rabbitGrowth():
    """
    rabbitGrowth is called once at the beginning of each time step.

    It makes use of the global variables: CURRENTRABBITPOP and MAXRABBITPOP.

    The global variable CURRENTRABBITPOP is modified by this procedure.

    For each rabbit, based on the probabilities in the problem set write-up,
      a new rabbit may be born.
    Nothing is returned.
    """
    global CURRENTRABBITPOP
    p = 1 - CURRENTRABBITPOP / float(MAXRABBITPOP)
    for _i in range(CURRENTRABBITPOP):
        if random.random() <= p and CURRENTRABBITPOP < MAXRABBITPOP:
            CURRENTRABBITPOP += 1


def foxGrowth():
    """
    foxGrowth is called once at the end of each time step.

    It makes use of the global variables: CURRENTFOXPOP and CURRENTRABBITPOP,
        and both may be modified by this procedure.

    Each fox, based on the probabilities in the problem statement, may eat
      one rabbit (but only if there are more than 10 rabbits).

    If it eats a rabbit, then with a 1/3 prob it gives birth to a new fox.

    If it does not eat a rabbit, then with a 1/10 prob it dies.

    Nothing is returned.
    """
    global CURRENTFOXPOP, CURRENTRABBITPOP
    p = CURRENTRABBITPOP / float(MAXRABBITPOP)
    for _i in range(CURRENTFOXPOP):
        if random.random() <= p and CURRENTRABBITPOP > 10:
            CURRENTRABBITPOP -= 1
            if random.random() <= 1 / 3.:
                CURRENTFOXPOP += 1
        else:
            if random.random() <= 0.1 and CURRENTFOXPOP > 10:
                CURRENTFOXPOP -= 1


def runSimulation(numSteps):
    """
    Runs the simulation for `numSteps` time steps.

    Returns a tuple of two lists: (rabbit_populations, fox_populations)
      where rabbit_populations is a record of the rabbit population at the
      END of each time step, and fox_populations is a record of the fox population
      at the END of each time step.

    Both lists should be `numSteps` items long.
    """
    rabbit_population, fox_population = [], []
    for _i in range(numSteps):
        rabbitGrowth()
        foxGrowth()
        rabbit_population.append(CURRENTRABBITPOP)
        fox_population.append(CURRENTFOXPOP)
    return rabbit_population, fox_population

rabbits, foxes = runSimulation(300)
pylab.plot(rabbits, 'r*-')
pylab.plot(foxes, 'go-')
pylab.title('Number of rabbits and foxes simulation')
pylab.xlabel('Time steps')
pylab.ylabel('Number of rabbits/foxes')
pylab.legend(('Rabbits', 'Foxes'))

coeff = pylab.polyfit(range(len(rabbits)), rabbits, 2)
pylab.plot(pylab.polyval(coeff, range(len(rabbits))))
pylab.show()
