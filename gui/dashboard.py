import tkinter as tk
from tkinter import ttk

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Ambiente Inteligente")

        self.labels = {}
        for sensor in ['Temperatura', 'Umidade', 'Qualidade do Ar', 'Luz', 'Ruído']:
            lbl = ttk.Label(root, text=f"{sensor}: ---")
            lbl.pack(padx=10, pady=5)
            self.labels[sensor] = lbl

    def update(self, data):
        self.labels['Temperatura'].config(text=f"Temperatura: {data['temp']} °C")
        self.labels['Umidade'].config(text=f"Umidade: {data['hum']} %")
        self.labels['Qualidade do Ar'].config(text=f"AQI: {data['aqi']}")
        self.labels['Luz'].config(text=f"Luz: {data['light']} lux")
        self.labels['Ruído'].config(text=f"Ruído: {data['noise']} dB")
