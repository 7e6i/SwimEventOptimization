from collections import Counter

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/EventsBySwimmer_Combined.tsv', delimiter='\t')


print(df)
data = []

for x in df['Events'].values.tolist():
    events = x.split(',')
    temp = []
    for y in events:
        if y not in ['200 FR','400 FR','200 MR']:
            temp.append(y)

    if len(temp)>1:
        data.append(str(temp))

count = Counter(data)
df = pd.DataFrame.from_dict(count, orient='index')
df.plot(kind='bar')
plt.show()

# maybe make an EventCount_All and EventCount_Individual_Only
