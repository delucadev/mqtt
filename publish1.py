import paho.mqtt.client as mqtt
from random import randrange
import time

broker = 'mqtt.eclipseprojects.io'
client = mqtt.Client('TemperaturaInterna')
client.connect(broker)

while True:
    randNumber = randrange(10)
    client.publish("TEMPERATURA", randNumber)
    print(f"Acabado de publicar {randNumber} para o tópico TEMPERATURA")
    time.sleep(5)