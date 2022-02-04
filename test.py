
import os
import json
from humidor import THMonitor


thm = THMonitor()
thm.read_sensors()


import pandas as pd
df = pd.read_json(thm.DATA_FILE, lines=True)
df['event_timestamp'] = pd.to_datetime(
    df['event_timestamp'],
    format='%Y-%m-%d %H:%M:%S.%f',
)
df.set_index('event_timestamp', inplace=True)

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 6))

for g in df.groupby('name'):
    plt.plot(g[1]['humidity'], label=g[0])

plt.axhline(y=60, dashes=(1,1,1,1), color='r')

leg = ax.legend()
# leg = ax.legend(loc='center', bbox_to_anchor=(0.5, -0.10), shadow=False, ncol=2)
plt.show()

# https://stackabuse.com/add-a-legend-to-figure-in-matplotlib/