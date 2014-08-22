# 6.00 Problem Set 9

import numpy
import random
import pylab
#from ps8b import *
from ps8b_precompiled_27 import *

#
# PROBLEM 1
#
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    def do_plot(delays, final_pops):
        for i in range(len(delays)):
            pylab.subplot(len(delays), 1, i + 1)
            pylab.hist(final_pops[i])
            pylab.xlabel('Final Virus Population')
            pylab.ylabel('No. of trials')

    final_steps = 150
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False}
    mutProb = 0.005
    drug_list = resistances.keys()

    delays = [300, 150, 75, 0]
    final_pops = []
    for delay in delays:
        tot_pop = []
        for _i in range(numTrials):
            viruses = [ResistantVirus(maxBirthProb,
                                      clearProb,
                                      resistances,
                                      mutProb)
                        for _i in range(numViruses)]
            patient = TreatedPatient(viruses, maxPop)
            for _i in range(delay + final_steps):
                if _i == delay:
                    for drug in drug_list:
                        patient.addPrescription(drug)
                patient.update()
            tot_pop.append(patient.getTotalPop())
        final_pops.append(tot_pop)

    do_plot(delays, final_pops)
    pylab.show()

#simulationDelayedTreatment(100)


#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    def do_plot(delays, final_pops):
        for i in range(len(delays)):
            pylab.subplot(len(delays), 1, i + 1)
            pylab.hist(final_pops[i])
            pylab.xlabel('Final Virus Population')
            pylab.ylabel('No. of trials')

    const_steps = 150
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False, 'grimpex': False}
    mutProb = 0.005

    delays = [300, 150, 75, 0]
    final_pops = []
    for delay in delays:
        tot_pop = []
        for _i in range(numTrials):
            viruses = [ResistantVirus(maxBirthProb,
                                      clearProb,
                                      resistances,
                                      mutProb)
                        for _i in range(numViruses)]
            patient = TreatedPatient(viruses, maxPop)
            for _i in range(const_steps + delay + const_steps):
                if _i == const_steps:
                    patient.addPrescription('guttagonol')
                if _i == const_steps + delay:
                    patient.addPrescription('grimpex')
                patient.update()
            tot_pop.append(patient.getTotalPop())
        final_pops.append(tot_pop)

    do_plot(delays, final_pops)
    pylab.show()

simulationTwoDrugsDelayedTreatment(200)
