from ui import run_ui
import sys, traceback
import paho.mqtt.client as mqtt
from data_handlers import read_data

settings = read_data('../settings.json')

def on_connect(client, userdata, flags, rc):
  print('Server connected to broker with result code ' + str(rc))

  client.subscribe(settings['top_level_topic'] + '/#')

def on_message(client, userdata, msg):
  print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(settings['mqtt_broker']['url'], 1883, 60)

client.loop_forever()
