import json
import os
import sys

dirname = os.path.dirname(__file__)
settings_path = os.path.join(dirname, '../settings.json')

def get_settings():
    """
    Combine settings from settings.json and argv
    """

    global_settings = json.loads(open(settings_path).read())
    _, terminal_id = sys.argv

    return {
        'terminal_id': terminal_id,
        'global_settings': global_settings
    }
