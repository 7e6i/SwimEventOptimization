import pandas as pd

def entries_to_events():
    df = pd.read_csv('../data/NYSPHSAA_22-23_Girls.csv')

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

    f = open('../data/EventsBySwimmer_Girls.tsv', 'w')
    f.write('Swimmer\tEvents')
    for key in keys:
        print(key, mydict[key])
        f.write(f'\n{key}\t{",".join(mydict[key])}')
    f.close()

    return mydict.values()

entries_to_events()
