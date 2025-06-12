# 🌿 Projeto de Extensão - IoT: Monitoramento Inteligente de Ambiente

Este projeto é um sistema de **monitoramento ambiental inteligente** voltado para o **bem-estar no ambiente de trabalho**, utilizando sensores físicos e/ou dados reais de clima via API, com visualização em tempo real e integração com MQTT.

---

## 🎯 Objetivo

Criar um sistema que **monitore as condições ambientais** (temperatura, umidade, qualidade do ar, ruído e luz) em tempo real para promover o conforto, a saúde e o desempenho de pessoas em ambientes fechados — como escritórios, salas de aula, coworkings ou laboratórios.

O projeto busca:

- Sensibilizar sobre a importância de ambientes saudáveis.
- Fornecer uma ferramenta visual e prática de monitoramento.
- Facilitar a coleta e envio de dados para futuras análises ou automações.

---

## 🧰 Funcionalidades

- 📡 Leitura de dados reais via [Open-Meteo API](https://open-meteo.com/) (temperatura, umidade, AQI/PM10).
- 💡 Simulação de sensores de ruído e luz.
- 📊 Dashboard interativo com `customtkinter`.
- ☁️ Envio de dados para um broker MQTT público (HiveMQ).

---

## 🔧 Tecnologias Utilizadas

- Python 3
- Tkinter + CustomTkinter (interface gráfica)
- MQTT com Paho MQTT
- Open-Meteo API (clima em tempo real)
- Requests (requisições HTTP)
- Simulação de sensores com Python

---

## 📁 Estrutura do Projeto

```
Projeto-extensao-IoT/
├── main.py                      # Script principal
├── requirements.txt             # Dependências
├── gui/
│   └── dashboard.py             # Interface gráfica com CustomTkinter
├── mqtt/
│   └── client.py                # Cliente MQTT
├── sensors/
│   ├── weather_api.py           # Consulta dados reais de clima
│   ├── light.py                 # Simulação de luminosidade
│   └── noise.py                 # Simulação de ruído
```

---

## 🚀 Como Executar o Projeto

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/Projeto-extensao-IoT.git
cd Projeto-extensao-IoT
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Execute o projeto
```bash
python main.py
```

---

## 📌 Observações

- Os dados de temperatura, umidade e qualidade do ar são obtidos **em tempo real da cidade de Nova Iguaçu - RJ**.
- Os sensores de luz e ruído ainda são simulados com valores aleatórios, podendo futuramente ser integrados a sensores físicos via GPIO.
- Os dados são enviados a cada 2 segundos para um tópico MQTT no broker HiveMQ.

---

## 💡 Ideias Futuras

- Integração com sensores físicos reais (ESP32, Raspberry Pi, etc.)
- Visualização gráfica dos dados históricos com Streamlit
- Gatilhos automáticos para alertas ou ações com base nas condições
- Registro em banco de dados

---

## 👩‍💻 Desenvolvido para projeto de extensão com foco em IoT, dados e bem-estar ambiental. 
