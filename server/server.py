import os
import json
import paho.mqtt.client as mqtt
from data_handlers import add_scan

dirname = os.path.dirname(__file__)
settings_path = os.path.join(dirname, '../settings.json')
settings = json.loads(open(settings_path).read())
topics = settings['topics']

def on_connect(client, userdata, flags, rc):
  print(f"Server connected to broker with result code {str(rc)}\n")

  client.subscribe(f"{settings['top_level_topic']}/#")

def on_message(client, userdata, msg):
  print(f"New message\nTopic: {msg.topic}\nPayload: {msg.payload}\n")
  
  topic = msg.topic
  payload = None

  try:
    payload = json.loads(msg.payload)
  except json.JSONDecodeError:
    print("ERROR: Invalid JSON\n")
    return None

  if topic == topics['scan_card']:
    add_scan(payload['client_id'], payload['value'])
  else:
    print(f"Unknown topic {topic}")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(settings['mqtt_broker']['url'], 1883, 60)
client.loop_forever()
