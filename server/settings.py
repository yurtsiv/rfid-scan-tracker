import json
import os
import sys

dirname = os.path.dirname(__file__)
settings_path = os.path.join(dirname, '../settings.json')

def get_settings():
  return json.loads(open(settings_path).read())

