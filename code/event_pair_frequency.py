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
        # if y not in ['50 Free','100 Free', '200 Free', '500 Free', '100 Back', '100 Breast', '100 Fly', '200 IM']:
        if y not in ['200 FR', '400 FR', '200 MR']:
            temp.append(y)

    if len(temp)>1:
        data.append(f'{temp[0]}, {temp[1]}')

count = Counter(data)

fig = plt.figure(figsize = (10, 7))
plt.bar(count.keys(), count.values())
plt.subplots_adjust(bottom=.3)
plt.xticks(rotation=90)
plt.xlabel("Individual Event Pairs")
plt.ylabel("Frequency")
plt.title("NYSPHSAA Girls '22/Boys '233 Championship Individual Event Groupings")
plt.show()