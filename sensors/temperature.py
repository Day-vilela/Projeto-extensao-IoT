import random

class TemperatureSensor:
    def read(self):
        return round(random.uniform(20.0, 30.0), 2)
