import os
import json
import uuid 
from datetime import datetime
from list_utils import find_by, diff

dirname = os.path.dirname(__file__)

people_file = os.path.join(dirname, "data/people.json")
terminals_file = os.path.join(dirname, "data/terminals.json")
scans_file = os.path.join(dirname, "data/scans.json")
cards_file = os.path.join(dirname, "data/cards.json")

def read_data(path):
  f = open(path, "r")
  fContent = f.read()
  return json.loads(fContent)

def write_data(path, array):
  f = open(path, "w")
  jsonTxt = json.dumps(array, indent=2, default=str)
  f.write(jsonTxt)

people = read_data(people_file)
terminals = read_data(terminals_file)
scans = read_data(scans_file)
cards = read_data(cards_file)

def get_terminals():
  global terminals

  return terminals

def get_people():
  global people

  return people

def get_cards():
  global cards
  
  return cards

def filter_people(key):
  global people

  return [w for w in people if key(w)]

def filter_scans(key):
  global scans

  return [r for r in scans if key(r)]
  

def get_people_with_card():
  return filter_people(lambda w: w.get('card_id') is not None)

def get_people_without_card():
  return filter_people(lambda w: w.get('card_id') is None)

def get_not_assigned_cards():
  global cards

  people_with_cards = get_people_with_card()
  assigned_cards = list(map(lambda w: w['card_id'], people_with_cards))
  return diff(cards, assigned_cards)

def find_person(key, val):
  global people

  return find_by(people, key=lambda person: person.get(key) == val)

def find_terminal(key, val):
  global terminals

  return find_by(terminals, key=lambda terminal: terminal.get(key) == val)

def add_card(id):
  global cards

  if id in cards:
    raise Exception("Card already registered")

  cards.append(id)
  write_data(cards_file, cards)

def delete_card(id):
  global cards

  cards.remove(id)
  write_data(cards_file, cards)

def add_terminal(name):
  global terminals

  id = uuid.uuid1().int
  terminal = { 'name': name, 'id': id }
  terminals.append(terminal)
  write_data(terminals_file, terminals)
  return terminal

def delete_terminal(id):
  global terminals

  terminals = list(filter(lambda t: t['id'] != id, terminals))
  write_data(terminals_file, terminals)

def add_person(full_name):
  global people

  id = uuid.uuid1().int
  people.append({ 'full_name': full_name, 'id': id })
  write_data(people_file, people)

  
def delete_person(id):
  global people

  people = list(filter(lambda t: t['id'] != id, people))
  write_data(people_file, people)
  

def assign_card_id(person_id, card_id):
  global people

  person = find_person("id", person_id)
  person['card_id'] = card_id
  write_data(people_file, people)

def remove_card_id(person_id):
  global people

  person = find_person("id", person_id)
  del person['card_id']
  write_data(people_file, people)

def add_scan(terminal_id, card_id):
  global people
  global terminals
  global scans
  global cards

  time = datetime.now()
  person = find_person("card_id", card_id)
  terminal = find_terminal("id", terminal_id)
 
  if (not card_id in cards) or (terminal is None) or (person is None):
    scans.append({ 'card_id': card_id, 'terminal_id': terminal_id, 'time': time })

    err_msg = ""
    if not card_id in cards:
      err_msg = f"Card {card_id} isn't registered in the system"
    elif terminal is None:
      err_msg = f"Terminal {terminal_id} isn't registered in the system"
    else:
      err_msg = f"Card {card_id} isn't assigned to any person"

    raise Exception(err_msg)
  else:
    scans.append({
      'card_id': card_id,
      'terminal_id': terminal_id,
      'person_id': person['id'],
      'time': time
    })
  
  write_data(scans_file, scans)
