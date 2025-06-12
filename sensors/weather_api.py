import requests

class WeatherSensor:
    def __init__(self, lat=-22.7556, lon=-43.4603):  # Nova Iguaçu - RJ
        self.api_url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude={lat}&longitude={lon}"
            f"&current_weather=true&hourly=relative_humidity_2m,pm10"
        )

    def read(self):
        try:
            response = requests.get(self.api_url, timeout=5)
            response.raise_for_status()
            json_data = response.json()

            # Dados atuais
            current = json_data.get("current_weather", {})
            hourly = json_data.get("hourly", {})
            time_now = current.get("time")  # Ex: '2025-06-11T15:00'

            # Achar o índice do horário atual na lista 'hourly'
            if time_now and "time" in hourly:
                try:
                    index = hourly["time"].index(time_now)
                    hum = hourly.get("relative_humidity_2m", [])[index]
                    aqi = hourly.get("pm10", [])[index]
                except ValueError:
                    hum = "---"
                    aqi = "---"
            else:
                hum = "---"
                aqi = "---"

            return {
                "temp": current.get("temperature", "---"),
                "hum": hum,
                "aqi": aqi  # PM10 como proxy de AQI
            }
        except Exception as e:
            print(f"[Erro na API Open-Meteo] {e}")
            return {"temp": "---", "hum": "---", "aqi": "---"}
