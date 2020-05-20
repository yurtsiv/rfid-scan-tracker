"""
Global settings
"""

MQTT_BROKER = {
    'url': "stepy-pc",
    'port': 8883,
    'use_tls': True,
    'server': {
        'username': "server",
        'password': "server"
    },
    'client': {
        'username': "client",
        'password': "client"
    }
}

TOPICS = {
    'scan_card': "rfid-scan-tracker/scan-card"
}