
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
#df.set_index('event_timestamp', inplace=True)

import bokeh.plotting as bp
from bokeh.models import ColumnDataSource

aspect_ratio = 16/9
width = 800
height = round(width/aspect_ratio)

bp.output_file(thm.HUMIDITY_PLOT_FILE)
p = bp.figure(
    x_axis_type="datetime",
    width=width,
    height=height,
)
color_map = {s['name']: s['label'] for s in thm.sensors}

for g in df.groupby('name'):
    p.line(
        x='event_timestamp',
        y='humidity',
        line_width=1,
        source=ColumnDataSource(g[1]),
        legend_label=g[0],
        color=color_map[g[0]],
    )

p.title.text = 'Humidity'
p.yaxis.axis_label = 'RH (%)'

bp.show(p)

# https://programminghistorian.org/en/lessons/visualizing-with-bokeh