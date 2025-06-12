import requests
import os
from dotenv import load_dotenv


load_dotenv() # Carrega variáveis do .env

class WeatherSensor:
    def __init__(self):
        self.api_key = os.getenv("OPENWEATHER_API_KEY") 
        self.cidade = "Nova Iguaçu,BR"
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def read(self):
        try:
            params = {
                'q': self.cidade,
                'appid': self.api_key,
                'units': 'metric',
                'lang': 'pt_br'
            }
            resposta = requests.get(self.base_url, params=params)
            if resposta.status_code == 200:
                dados = resposta.json()
                return {
                    'temp': round(dados['main']['temp'], 1),
                    'hum': round(dados['main']['humidity'], 1),
                    'aqi': self.simular_aqi()  # AQI não vem pela API gratuita, vamos simular
                }
            else:
                print(f"Erro na API: {resposta.status_code}")
                return {'temp': '---', 'hum': '---', 'aqi': '---'}
        except Exception as e:
            print("Erro ao acessar a API:", e)
            return {'temp': '---', 'hum': '---', 'aqi': '---'}

    def simular_aqi(self):
        # Simula valor entre 0 e 300
        import random
        return random.randint(30, 120)
