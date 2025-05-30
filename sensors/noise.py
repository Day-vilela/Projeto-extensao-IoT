import random

class NoiseSensor:
    def read(self):
        return round(random.uniform(30.0, 90.0), 1)
