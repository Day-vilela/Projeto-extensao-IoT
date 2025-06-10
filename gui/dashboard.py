import customtkinter as ctk
import random

class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("🐱‍👤 Ambiente Inteligente")
        self.root.geometry("350x480")

        # Mapeamento dos sensores
        self.sensor_map = {
            '🌡 Temperatura': ('temp', '°C'),
            '💧 Umidade': ('hum', '%'),
            '🌫 Qualidade do Ar (AQI)': ('AQI', ''),
            '💡 Luminosidade': ('light', 'lux'),
            '🔊 Nível de Ruído': ('noise', 'dB')
        }

        # Título
        titulo = ctk.CTkLabel(self.root, text="📊 Monitoramento de Ambiente", font=("Arial", 18, "bold"))
        titulo.pack(pady=20)

        # Dicionário para armazenar labels dos valores
        self.valor_labels = {}

        # Criar cards
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

# Configurações iniciais do tema
ctk.set_appearance_mode("dark")  # ou "dark"
ctk.set_default_color_theme("blue")

# Criar janela principal
app = ctk.CTk()

# Criar dashboard
dashboard = Dashboard(app)

# Simular atualizações periódicas de dados
def simular_dados():
    dados = {
        'temp': round(random.uniform(20, 35), 1),
        'hum': round(random.uniform(40, 70), 1),
        'AQI': random.randint(0, 300),
        'light': random.randint(100, 800),
        'noise': round(random.uniform(30, 90), 1)
    }
    dashboard.update(dados)
    app.after(2000, simular_dados)  # Atualiza a cada 2 segundos

# Iniciar simulação
simular_dados()

# Rodar interface
app.mainloop()
