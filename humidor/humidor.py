import os
import json
import yaml

from inkbird import InkbirdIBSTH


class THMonitor():
    def __init__(self, config_yaml='sensors.yaml'):
        with open(config_yaml) as file:
            yaml_content = yaml.safe_load(file)
        for d in yaml_content['sensors']:
            d['device'] = InkbirdIBSTH(d['mac_address'], d['sensor_type'])
        self.sensors = yaml_content['sensors']

    def get_sensor_data(self):
        for d in self.sensors:
            d['last_reading'] = d['device'].read_sensor()
