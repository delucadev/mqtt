import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print(f"Mensagem recebida: {message.payload.decode('utf-8')}")

broker = 'mqtt.eclipseprojects.io'
client = mqtt.Client('Dispositivo')
client.connect(broker)

client.loop_start()
client.subscribe("TEMPERATURA")
client.on_message = on_message
time.sleep(60)
client.loop_stop()