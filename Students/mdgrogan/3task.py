__author__ = "Matthew Grogan"
__NetID__ = "grogan2122"
__GitHubID__ = "mdgrogan"

import random

Cardinality = 2 
NumberTrials = 1000

def biased_flip(p):
	return 0 if random.random()<p else 1

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
	TrialSequence.append(biased_flip(.75))

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
	EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex)/float(NumberTrials))
print EmpiricalDistribution
