import os
import json
import yaml
from datetime import datetime

from inkbird import InkbirdIBSTH


class THMonitor():
    def __init__(self, config_yaml='sensors.yaml'):
        print(f'{self._timestamp()} Initializing THMonitor...')
        with open(config_yaml) as f:
            yaml_content = yaml.safe_load(f)
        f.close()
        for d in yaml_content['sensors']:
            d['device'] = InkbirdIBSTH(d['mac_address'], d['sensor_type'])
        self.sensors = yaml_content['sensors']
        print(f'{self._timestamp()} THMonitor initialized.')
    
    FLASH_DRIVE_PATH = '/media/pi/humidor/'
    DATA_FILE = FLASH_DRIVE_PATH + 'data.json'
    
    def _timestamp(self):
        return datetime.utcnow()

    def read_sensors(self, write_to_file=True):
        print(f'{self._timestamp()} Initiating sensor reading...')
        for sensor in self.sensors:
            self._read_sensor_data(sensor)
            payload = self._reading_to_json(sensor)
            self._reading_to_file(payload)     
            
    def _read_sensor_data(self, sensor):
        s = sensor
        try:
            print(f'{self._timestamp()} Reading {s["name"]} sensor...')
            reading = s['device'].read_sensor()
            event_timestamp = self._timestamp()
            s['reading'] = reading
            s['reading']['event_timestamp'] = event_timestamp
            print(
                '\n'+ '#'*32 + '\n'
                f'{event_timestamp} Succesfully read {s["name"]} sensor.',
                f'\nReading for {s["name"]} sensor:',
                f'\n\ttemperature: {reading["temperature_farenheit"]}F',
                f'\n\thumidity:    {reading["humidity"]}%',
                '\n'+ '#'*32 + '\n'
            )
            
        except:
            print(f'{self._timestamp()} Sensor reading failed.')
        
    def _reading_to_json(self, sensor):
        try:
            READING_KEYS = [
                'event_timestamp',
                'temperature_farenheit',
                'humidity',
            ]
            payload = {rk: sensor['reading'][rk] for rk in READING_KEYS}
            payload['mac_address'] = sensor['mac_address']
            payload['label'] = sensor['label']
            payload['name'] = sensor['name']
            return json.dumps(payload, default=str, sort_keys=True)
        except:
            print(f'{self._timestamp()} Unable to parse reading.')
    
    def _reading_to_file(self, payload):
        with open(self.DATA_FILE, 'a', encoding='utf-8') as f:
            try:
                f.write(payload + '\n')
            except:
                print(
                    f'{self._timestamp()} Unable to append reading to file {DATA_FILE}',
                    f'\treading: {payload}',
                )
        f.close()
