__author__ = "Derek Heidtke"
__NetID__ = "derek.heidtke"
__GitHubID__ = "derekheidtke"

import random

Cardinality = 2
NumberTrials = 1000

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
	if( random.random() < 0.75 ):
		TrialSequence.append(1)
	else:
		TrialSequence.append(0)

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print EmpiricalDistribution