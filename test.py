import json
from humidor import THMonitor

thm = THMonitor()
thm.get_sensor_data()

print(json.dumps(thm.sensors, indent=2, default=str))