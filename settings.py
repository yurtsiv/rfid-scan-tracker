"""
Global settings
"""

MQTT_BROKER = {
    'url': "stepy-pc",
    'port': 8883,
    'username': "",
    'password': ""
}

TOP_LEVEL_TOPIC = "rfid-scan-tracker"
TOPICS = {
    'scan_card': f"{TOP_LEVEL_TOPIC}/scan_card"
}