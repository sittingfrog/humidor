from .humidor import THMonitor

if __name__ == "__main__":
	thm = THMonitor()
	thm.read_sensors()
