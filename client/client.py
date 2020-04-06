import json
import sys, traceback
import paho.mqtt.client as mqtt

settings = json.loads(open('../settings.json').read())
_, client_id = sys.argv

client = mqtt.Client()
client.connect(settings['mqtt_broker']['url'], 1883, 60)

def wrap_value(value):
  return {
    'client_id': int(client_id),
    'value': value
  }

def publish(topic, value):
  client.publish(
    topic,
    json.dumps(wrap_value(value))
  )

publish(settings['topics']['scan_card'], 123)
