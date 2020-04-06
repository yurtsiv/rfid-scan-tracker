import json
import os
import sys

dirname = os.path.dirname(__file__)
settings_path = os.path.join(dirname, '../settings.json')

def get_settings():
  global_settings = json.loads(open(settings_path).read())
  _, client_id = sys.argv

  return {
    'client_id': 123,
    'global_settings': global_settings
  }

