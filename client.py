"""
The client which runs on a RaspberryPI.
Listens to card scanning and publishes card ID
"""

import json
import time
import sys, traceback
import paho.mqtt.client as mqtt
from settings import MQTT_BROKER as BROKER, TOPICS

TERMINAL_ID = None

try:
    TERMINAL_ID = int(sys.argv[1])
except Exception:
    print("\nPlease provide a valid Terminal ID by running:\n\npython3 client.py <Terminal ID>\n")
    sys.exit()
 
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connection established\n") 
    else:
        print(f"Couldn't connect to the broker {BROKER['url']}. Error code {rc}\n")

def on_disconnect():
    print("Disconnected from the broker\n")

client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect

def attach_meta_info(value):
    return {
        'terminal_id': TERMINAL_ID,
        'value': value
    }

def publish(topic, value):
    payload = json.dumps(attach_meta_info(value))
    res = client.publish(topic, payload)

    if res.rc == mqtt.MQTT_ERR_SUCCESS:
        print(f"Published\nTopic: {topic}\nPayload: {payload}\n")
    else:
        print(f"Publish to {topic} failed. Error code {res.rc}")

client.username_pw_set(BROKER['client']['username'], BROKER['client']['password'])
client.tls_set("ca.crt")

print(f"Connecting to the broker {BROKER['url']}")
client.connect(BROKER['url'], BROKER['port'], 60)
client.loop_start()

cards = [
    "123123123",
    "123123122",
    "432432432"
]

while True:
    for card in cards:
        time.sleep(5)
        publish(TOPICS['scan_card'], card)
