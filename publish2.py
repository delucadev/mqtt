import paho.mqtt.client as mqtt
from random import uniform
import time

broker = 'mqtt.eclipseprojects.io'
client = mqtt.Client('TemperaturaExterna')
client.connect(broker)

while True:
    randNumber = uniform(20.0, 22.0)
    client.publish("TEMPERATURA", randNumber)
    print(f"Acabado de publicar {randNumber} para o tópico TEMPERATURA")
    time.sleep(2)