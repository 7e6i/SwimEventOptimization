import random
import time
import math
import json
from datetime import datetime, timedelta

import pandas as pd
import itertools
import matplotlib.pyplot as plt

TOTAL = 199584000
TOTAL = math.factorial(12)
EVENTS = ['200 MR',
          '200 Free',
          '200 IM',
          '50 Free',
          'Diving',
          '100 Fly',
          '500 Free',
          '100 Free',
          '200 FR',
          '100 Back',
          '100 Breast',
          '400 FR']



def read_csv():
    df = pd.read_csv('../data/EventsBySwimmer_Combined.tsv', delimiter='\t')

    raw_entries = df['Events'].values.tolist()

    # for e in raw_events : print(e)

    return raw_entries


def loss_fcn(string, permutation):
    athlete_events = string.split(',')
    athlete_position = []

    # if only 1 event, rest doesn't matter
    if len(athlete_events) == 1:
        return 0

    # find positions of each event
    for e in athlete_events:
        athlete_position.append(permutation.index(e))
    athlete_position.sort()

    # for each position, calculate distance
    total = 0
    for x in range(len(athlete_position) - 1):
        dif = athlete_position[x + 1] - athlete_position[x] - 1
        total += dif
        # print(dif)

    return total
    # print(athlete_events, athlete_position, total)


def main_loop():
    raw_entries = read_csv()
    print('data read in.')

    permutations = itertools.permutations(EVENTS)

    max_score = 0
    results = []

    x = 0
    for s in permutations:
        x += 1

        if x >500000: break
        p = list(s)
        random.shuffle(p)

        # calculate loss for a given permutation
        loss = 0
        for s in raw_entries:
            l = loss_fcn(s, p)
            loss += l

        results.append(loss)
        if x%1000==0:
            print(x)

        # if the loss is better than the previous record, update the record
        if loss > max_score:
            max_score = loss
            print(f'\033[92m{x}, {loss}, {p}\033[0m')

    return results


results = main_loop()
plt.hist(results, bins=range(800,2900,10))
plt.show()
