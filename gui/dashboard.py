import tkinter as tk
from tkinter import ttk

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Ambiente Inteligente") #Atualizar: titulo

        self.sensor_map = {
            'Temperatura' : ('temp', '°C'),
            'Umidade' : ('hum', '%'),
            'Qualidade do Ar' : ('AQI', ''),
            'Luz' : ('light', 'lux'),
            'Ruído' : ('noise', 'dB')
        }

        self.labels = {}
        for i, (nome, (chave, unidade)) in enumerate(self.sensor_map.items()):
            lbl = ttk.Label(root, text=f"{nome}: ---")
            lbl.grid(row=i, column=0, sticky='w', padx=10, pady=5)
            self.labels[nome] = lbl

    def update(self, data):
        for nome, (chave, unidade) in self.sensor_map.items():
            valor = data.get(chave, '---')
            self.labels[nome].config(text=f"{nome}: {valor} {unidade}")