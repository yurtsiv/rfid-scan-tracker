"""
Global settings
"""

MQTT_BROKER = {
    'url': "stepy-pc",
    'port': 8883,
    'server': {
        'username': "server",
        'password': "server"
    },
    'client': {
        'username': "client",
        'password': "client"
    }
}

TOP_LEVEL_TOPIC = "rfid-scan-tracker"
TOPICS = {
    'scan_card': f"{TOP_LEVEL_TOPIC}/scan-card"
}