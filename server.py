"""
App server which listens to incoming messages
and collects information on card scannings coming
from clients/terminals
"""

import sys
import json
import paho.mqtt.client as mqtt
from api.data_handlers import add_scan
from settings import MQTT_BROKER as BROKER, TOPICS

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connection established") 
        client.subscribe(TOPICS['scan_card'])
    else:
        print(f"Couldn't connect to the broker {BROKER['url']}. Error code {rc}")

def on_disconnect():
    print("Disconnected from the broker")

def handle_message(topic, payload):
    if topic == TOPICS['scan_card']:
        add_scan(payload.get('terminal_id'), payload.get('value'))
    else:
        print(f"Unknown topic {topic}")

def on_message(client, userdata, msg):
    print(f"\nMessage received\nTopic: {msg.topic}\nPayload: {msg.payload}\n")

    try:
        payload = json.loads(msg.payload)
        handle_message(msg.topic, payload)
    except json.JSONDecodeError:
        print("ERROR: Invalid JSON\n")
    except Exception as err:
        print(f"ERROR: {str(err)}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

client.username_pw_set(BROKER['server']['username'], BROKER['server']['password'])

if BROKER['use_tls']:
  client.tls_set("ca.crt")

print(f"Connecting to the broker {BROKER['url']}")
client.connect(BROKER['url'], BROKER['port'], 60)
client.loop_forever()
