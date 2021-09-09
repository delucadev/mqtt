import paho.mqtt.client as mqtt
from random import uniform
import time

broker = 'mqtt.eclipseprojects.io'
client = mqtt.Client('TemperaturaInterna')
client.connect(broker)

while True:
    randNumber = uniform(18.0, 20.0)
    client.publish("TEMPERATURA", randNumber)
    print(f"Acabado de publicar {randNumber} para o tópico TEMPERATURA")
    time.sleep(5)