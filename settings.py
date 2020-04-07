MQTT_BROKER = {
    'url': "mqtt.eclipse.org",
    'username': "",
    'password': ""
}

TOP_LEVEL_TOPIC = "rfid-scan-tracker"
TOPICS = {
    'scan_card': f"{TOP_LEVEL_TOPIC}/scan_card"
}