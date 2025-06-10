import tkinter as tk # O tkinter é usado para  criar a interface gráfica (usado na pasta GUI)
from gui.dashboard import Dashboard #Importa a class responsável por mostrar os dados dos sensores na interface
from sensors.temperature import TemperatureSensor
from sensors.humidity import HumiditySensor
from sensors.air_quality import AirQualitySensor
from sensors.light import LightSensor
from sensors.noise import NoiseSensor # classes dos sensores
from mqtt.client import MqttClient #Importa a classe responsável por enviar dados via protocolo MQTT

class App:
    def __init__(self, root):
        self.dashboard = Dashboard(root)
        self.temp = TemperatureSensor()
        self.hum = HumiditySensor()
        self.aqi = AirQualitySensor()
        self.light = LightSensor()
        self.noise = NoiseSensor()
        self.mqtt = MqttClient()
        self.update_data()

    def update_data(self):
        data = {
            "temp": self.temp.read(),
            "hum": self.hum.read(),
            "aqi": self.aqi.read(),
            "light": self.light.read(),
            "noise": self.noise.read()
        }
        self.dashboard.update(data)
        self.mqtt.publish(data)
        self.dashboard.root.after(2000, self.update_data)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
