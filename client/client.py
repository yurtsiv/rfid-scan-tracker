import json
import sys, traceback
import paho.mqtt.client as mqtt
from settings import get_settings

settings = get_settings()

client = mqtt.Client()
client.connect(settings['global_settings']['mqtt_broker']['url'], 1883, 60)

def wrap_value(value):
  return {
    'client_id': int(settings['client_id']),
    'value': value
  }

def publish(topic, value):
  payload = json.dumps(wrap_value(value))
  res = client.publish(topic, payload)

  if res.rc == mqtt.MQTT_ERR_SUCCESS:
    print(f"Published\nTopic: {topic}\nPayload: {payload}\n")
  else:
    print(f"Publish to {topic} failed. Error code {res.rc}")

topics = settings['global_settings']['topics']

publish(topics['scan_card'], 123)
