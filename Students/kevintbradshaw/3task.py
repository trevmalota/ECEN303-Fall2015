__author__ = "Kevin Bradshaw"
__NetID__ = "kevintbradshaw"
__GitHubID__ = "kevintbradshaw"

import random

Cardinality = 2
NumberTrials = 1000
coin = 2                            # Arbitrary value just so the coin doesn't start at heads or tails
probability = 0.75

TrialSequence = []
for TrialIndex in range(0, NumberTrials):
    TrialSequence.append(random.randrange(Cardinality))
    if random.random() < probability:
        coin = 1                    # Heads
    else:
        coin = 0                    # Tails
    TrialSequence.append(coin)      # Outcome added to Sequence

EmpiricalDistribution = []
for OutcomeIndex in range(0, Cardinality):
    EmpiricalDistribution.append(TrialSequence.count(OutcomeIndex) / float(NumberTrials))
print EmpiricalDistribution

