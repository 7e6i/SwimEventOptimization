import time
import math
import json
from datetime import datetime, timedelta

import pandas as pd
import itertools

TESTING = ('400 FR',)

EVENTS = [
    'Diving',
    '50 Free',
    '100 Free',
    '200 Free',
    '500 Free',
    '100 Back',
    '100 Breast',
    '100 Fly',
    '200 IM',
    '200 FR',
    '400 FR',
    '200 MR',
]


loc = EVENTS.index(TESTING[0])
finalized = set(EVENTS[:loc])

EVENTS.remove(TESTING[0])


def write_json(score=None, events=None):
    data = {'top score': score, 'top events': events}

    json_object = json.dumps(data, indent=4)

    f = open('J.json', "w")
    f.write(json_object)
    f.close()

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


    TOTAL = math.factorial(11)
    max_score = 0
    x = 0

    t0 = time.time()
    for s in permutations:
        x += 1

        # let the user know when the program will be done
        if x % 10000 == 0:
            tc = time.time() - t0
            rate = x / tc
            todo = TOTAL - x
            print(x, str(datetime.now() + timedelta(seconds=todo/rate))[5:19])

        p = TESTING+s
        # because the fitness function is the same for reversed events
        if p[-1] in finalized: continue

        # calculate loss for a given permutation
        loss = 0
        for s in raw_entries:
            l = loss_fcn(s, p)
            loss += l

        # if the loss is better than the previous record, update the record
        if loss > max_score:
            max_score = loss
            print(f'\033[92m{x}, {loss}, {p}\033[0m')
            write_json(loss, p)




main_loop()
