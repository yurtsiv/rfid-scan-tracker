import json
import time
import sys, traceback
import paho.mqtt.client as mqtt
from settings import get_settings

settings = get_settings()
broker_url = settings['global_settings']['mqtt_broker']['url']
topics = settings['global_settings']['topics']

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connection established\n") 
    else:
        print(f"Couldn't connect to the broker {broker_url}. Error code {rc}\n")

def on_disconnect():
    print("Disconnected from the broker\n")

client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect

def attach_meta_info(value):
    return {
        'terminal_id': int(settings['terminal_id']),
        'value': value
    }

def publish(topic, value):
    payload = json.dumps(attach_meta_info(value))
    res = client.publish(topic, payload)

    if res.rc == mqtt.MQTT_ERR_SUCCESS:
        print(f"Published\nTopic: {topic}\nPayload: {payload}\n")
    else:
        print(f"Publish to {topic} failed. Error code {res.rc}")

print(f"Connecting to the broker {broker_url}")
client.connect(broker_url, 1883, 60)
client.loop_start()

cards = [
    [148, 35, 65, 119],
    [150, 60, 90, 200],
    [130, 75, 80, 130]
]

while True:
    for card in cards:
        time.sleep(2)
        publish(topics['scan_card'], card)
