import tkinter as tk # O tkinter é usado para  criar a interface gráfica (usado na pasta GUI)
from gui.dashboard import Dashboard #Importa a class responsável por mostrar os dados dos sensores na interface
from sensors.weather_api import WeatherSensor # API que mostra dados reais de Temp, AQi e 
from sensors.light import LightSensor
from sensors.noise import NoiseSensor # classes dos sensores
from mqtt.client import MqttClient #Importa a classe responsável por enviar dados via protocolo MQTT

class App:
    def __init__(self, root):
        self.dashboard = Dashboard(root)
        self.weather = WeatherSensor()
        self.light = LightSensor()
        self.noise = NoiseSensor()
        self.mqtt = MqttClient()
        self.update_data()

    def update_data(self):
        climate = self.weather.read()
        data = {
            "temp": climate["temp"],
            "hum": climate["hum"],
            "aqi": climate["aqi"],
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
