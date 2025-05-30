import paho.mqtt.client as mqtt
import json

class MqttClient:
    def __init__(self, broker="broker.hivemq.com", port=1883, topic_base="smart/environment"):
        self.topic_base = topic_base
        self.client = mqtt.Client()
        self.client.connect(broker, port, 60)
        self.client.loop_start()

    def publish(self, data: dict):
        payload = json.dumps(data)
        self.client.publish(f"{self.topic_base}/data", payload)
        print(f"Publicado em {self.topic_base}/data: {payload}")
