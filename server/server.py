import os
import json
import paho.mqtt.client as mqtt
from data_handlers import add_scan
from settings import get_settings

settings = get_settings()
topics = settings['topics']
broker_url = settings['mqtt_broker']['url']

def on_connect(client, userdata, flags, rc):
  if rc == 0:
    print("Connection established") 
    client.subscribe(f"{settings['top_level_topic']}/#")
  else:
    print(f"Couldn't connect to the broker {broker_url}. Error code {rc}")
  
def on_disconnect():
  print("Disconnected from the broker")

def on_message(client, userdata, msg):
  print(f"\nNew message\nTopic: {msg.topic}\nPayload: {msg.payload}\n")
  topic = msg.topic
  payload = None

  try:
    payload = json.loads(msg.payload)
  except json.JSONDecodeError:
    print("ERROR: Invalid JSON\n")
    return None

  if topic == topics['scan_card']:
    add_scan(payload.get('terminal_id'), payload.get('value'))
  else:
    print(f"Unknown topic {topic}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

print(f"Connecting to the broker {broker_url}")
client.connect(broker_url, 1883, 60)
client.loop_forever()
