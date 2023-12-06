import time
import math
import json
import pandas as pd
import itertools

TOTAL = math.factorial(12)-2*math.factorial(11)
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
    df = pd.read_csv('../data files/EventsBySwimmer_Combined.tsv', delimiter='\t')

    raw_entries = df['Events'].values.tolist()

    # for e in raw_events : print(e)

    return raw_entries


def write_json(last=None, score=None, score_iter=None, events=None):
    f = open('resumable_data.json', "r")
    data = json.load(f)
    f.close()

    if last is not None:
        data['last iteration'] = last
    elif score is not None and score_iter is not None and events is not None:
        data['top score'] = score
        data['top score iteration'] = score_iter
        data['top score order'] = events

    json_object = json.dumps(data, indent=4)

    f = open('resumable_data.json', "w")
    f.write(json_object)
    f.close()

def read_json():
    f = open('resumable_data.json', "r")
    data = json.load(f)
    f.close()
    return data


def loss_fcn(string, permuation):
    athlete_events = string.split(',')
    athlete_position = []

    # if only 1 event, rest doesn't matter
    if len(athlete_events)==1:
        return 0

    # find positions of each event
    for e in athlete_events:
        athlete_position.append(permuation.index(e))
    athlete_position.sort()

    # for each position, calculate distance
    total = 0
    for x in range(len(athlete_position)-1):
        dif = athlete_position[x+1]-athlete_position[x]-1
        total += dif
        # print(dif)

    return total
    # print(athlete_events, athlete_position, total)


def main_loop():
    raw_entries = read_csv()
    print('data read in.')

    start = read_json()
    start_max = start['top score iteration']
    last_iter = start['last iteration']

    permuatations = itertools.permutations(EVENTS)

    max_score = 0
    top_scores = {}
    t0 = time.time()
    x=0

    for p in permuatations:
        # make it resumable by writing every 10k to json file
        x+=1
        # if x>10: break
        if x < start_max: continue
        elif x in [start_max]: pass
        elif x < last_iter: continue

        if p[0]=='Diving' or p[-1]=='Diving':
            continue

        loss = 0
        for s in raw_entries:
            l = loss_fcn(s, p)
            loss += l

        if (loss > max_score):
            top_scores[p] = loss
            max_score = loss
            print(f'\033[92m{x}, {loss}, {p}\033[0m')
            write_json(score=max_score, score_iter=x, events=str(p))


        if x%10000==0:
            t1 = time.time()
            tc = t1-t0
            left = (TOTAL - x)/10000
            print(x, round(tc,2), round(tc*left), loss, p)
            t0 = t1
            write_json(last=x)

main_loop()


