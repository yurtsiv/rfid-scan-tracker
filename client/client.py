import json
import sys, traceback
import paho.mqtt.client as mqtt

settings = json.loads(open('../settings.json').read())

client = mqtt.Client()
client.connect(settings['mqtt_broker']['url'], 1883, 60)

def publish(sub_topic, value):
  client.publish(settings['top_level_topic'] + '/' + sub_topic, value)

publish(settings['sub_topics']['scan_card'], 123)
