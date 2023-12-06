from collections import Counter

import pandas as pd
import matplotlib.pyplot as plt

def entries_to_events():
    df = pd.read_csv('NYSPHSAA_22-23_Girls.csv')

    mydict = {}
    for col in df.columns:
        # print(col)

        x = df[col].dropna()

        for y in x.values:
            if y in mydict.keys():
                mydict[y].append(col)
            else:
                mydict[y] = [col]


    keys = sorted(list(mydict.keys()))

    f = open('EventsBySwimmer_Girls.tsv', 'w')
    f.write('Swimmer\tEvents')
    for key in keys:
        print(key, mydict[key])
        f.write(f'\n{key}\t{",".join(mydict[key])}')
    f.close()

    return mydict.values()


def events_to_counts():
    events = entries_to_events()
    data = []

    for x in events:
        temp = []
        for e in x:
            if e not in ['200 FR','400 FR','200 MR']:
                temp.append(e)

        if len(temp)>=2:
            data.append(str(temp))


    count = Counter(data)
    df = pd.DataFrame.from_dict(count, orient='index')
    df.plot(kind='bar')
    plt.show()

events_to_counts()