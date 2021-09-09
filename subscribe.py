import paho.mqtt.client as mqtt
import time

msg = ''
def on_message(client, userdata, message):
    print(f"Mensagem recebida: {message.payload.decode('utf-8')} ")
    
nome = input('nome do dispositivo: ')
broker = 'mqtt.eclipseprojects.io'
client = mqtt.Client(nome)
client.connect(broker)

client.loop_start()
client.subscribe("TemperaturaInterna")
client.on_message = on_message

time.sleep(120)
client.loop_stop()