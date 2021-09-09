import paho.mqtt.client as mqtt
from random import uniform
import time
import PySimpleGUI as sg

layout = [  [sg.Text('Informe a temperatura: '),],
            [sg.InputText(key='temp')],
            [sg.Button('Enviar'), sg.Button('Sair')] ]

window = sg.Window('Controlador de Temperatura', layout)

broker = 'mqtt.eclipseprojects.io'
client = mqtt.Client('TemperaturaInterna')
client.connect(broker)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Sair':
        break
    else:
        randNumber = values['temp']
        client.publish("TemperaturaInterna", randNumber)
        print(f"Acabado de publicar {randNumber} para o tópico TEMPERATURA")

window.close()

    