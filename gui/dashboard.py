import customtkinter as ctk
import random
from sensors.weather_api import WeatherSensor


class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("🐱‍👤 Ambiente Inteligente")
        self.root.geometry("350x480")

        # Aqui temos o Mapeamento dos sensores
        self.sensor_map = {
            '🌡 Temperatura': ('temp', '°C'),
            '💧 Umidade': ('hum', '%'),
            '🌫 Qualidade do Ar (AQI)': ('AQI', ''),
            '💡 Luminosidade': ('light', 'lux'),
            '🔊 Nível de Ruído': ('noise', 'dB')
        }

        # Título
        titulo = ctk.CTkLabel(self.root, text="📊 Bem-Estar No Ambiente de Trabalho ", font=("Arial", 18, "bold"))
        titulo.pack(pady=20)

        # Dicionário para armazenar labels dos valores
        self.valor_labels = {}

        # Criação dos cards
        for nome, (_, unidade) in self.sensor_map.items():
            frame = ctk.CTkFrame(self.root)
            frame.pack(pady=8, padx=20, fill="x")

            label_titulo = ctk.CTkLabel(frame, text=nome, font=("Arial", 14))
            label_titulo.pack(anchor="w", padx=10, pady=(5, 0))

            label_valor = ctk.CTkLabel(frame, text="---", font=("Arial", 16, "bold"))
            label_valor.pack(anchor="w", padx=10, pady=(0, 5))

            self.valor_labels[nome] = label_valor

    def update(self, data):
        for nome, (chave, unidade) in self.sensor_map.items():
            valor = data.get(chave, '---')
            self.valor_labels[nome].configure(text=f"{valor} {unidade}")

# Configurações tema
ctk.set_appearance_mode("dark")  # "light"
ctk.set_default_color_theme("blue")

# Criar janela principal
app = ctk.CTk()

# Criação do dashboard
dashboard = Dashboard(app)

sensor_clima = WeatherSensor()

def atualizar_dados_reais():
    clima = sensor_clima.read()

    # Verificação para conferir se os dados da API estão disponíveis
    usar_simulacao = clima['temp'] == "---"

    if usar_simulacao:
        print("⚠️ Falha na API. Usando dados simulados.")
        dashboard.mostrar_erro_api(True)

        # Simula tudo
        dados = {
            'temp': round(random.uniform(20, 35), 1),
            'hum': round(random.uniform(40, 70), 1),
            'AQI': random.randint(0, 300),
            'light': random.randint(100, 800),
            'noise': round(random.uniform(30, 90), 1)
        }
    else:
        dashboard.mostrar_erro_api(False)

        # Usa dados reais + sensores locais simulados
        dados = {
            'temp': clima['temp'],
            'hum': clima['hum'],
            'AQI': clima['aqi'],
            'light': random.randint(100, 800),
            'noise': round(random.uniform(30, 90), 1)
        }

    dashboard.update(dados)
    app.after(5000, atualizar_dados_reais)  # Atualiza a cada 5 segundos



# Iniciar simulação
atualizar_dados_reais()
# Rodar interface
app.mainloop()

