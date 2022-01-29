import os
import json
import yaml
from datetime import datetime

from inkbird import InkbirdIBSTH


class THMonitor():
    def __init__(self, config_yaml='sensors.yaml'):
        print(f'{self._timestamp()} Initializing THMonitor...')
        with open(config_yaml) as file:
            yaml_content = yaml.safe_load(file)
        for d in yaml_content['sensors']:
            d['device'] = InkbirdIBSTH(d['mac_address'], d['sensor_type'])
        self.sensors = yaml_content['sensors']
        print(f'{self._timestamp()} THMonitor initialized.')

    def _timestamp(self):
        return datetime.utcnow()

    def read_sensors(self):
        print(f'{self._timestamp()} Initiating sensor reading...')
        for sensor in self.sensors:
            self._read_sensor_data(sensor)
            
            
    def _read_sensor_data(self, sensor):
        s = sensor
        try:
            print(f'{self._timestamp()} Reading {s["name"]} sensor...')
            last_reading = s['device'].read_sensor()
            last_reading_at = self._timestamp()
            s['last_reading'] = last_reading
            s['last_reading_at'] = last_reading_at
            print(
                f'{last_reading_at} Succesfully read {s["name"]} sensor.',
                f'\nReading for {s["name"]} sensor:',
                f'\n\ttemperature: {last_reading["temperature_farenheit"]}F',
                f'\n\thumidity:    {last_reading["humidity"]}%',
            )
            
        except:
            print(f'{self._timestamp()} Sensor reading failed.')
                
