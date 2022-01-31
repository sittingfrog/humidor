import json
from humidor import THMonitor
import blynklib
# import blynklib_mp as blynklib # micropython import

BLYNK_AUTH = 'IGDwtWzLwTuyhjI4Mk5VBIWbdk67DXzx' 
blynk = blynklib.Blynk(BLYNK_AUTH)

thm = THMonitor()
thm.read_sensors()

readings = [thm._format_reading(s) for s in thm.sensors]
# [print(reading) for reading in readings]

pin = 'V0'
@blynk.handle_event('read V0')
def read_virtual_pin_handler(pin):
    
    sensor_data = str(readings[0]['temperature_farenheit'])
    print(sensor_data)
    blynk.virtual_read(pin, sensor_data)

while True:
    blynk.run()