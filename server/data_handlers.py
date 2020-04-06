import os
import errno
import json
import uuid
from datetime import datetime
from list_utils import find_by, diff

dirname = os.path.dirname(__file__)

PEOPLE_FILE_PATH = os.path.join(dirname, "data/people.json")
TERMINALS_FILE_PATH = os.path.join(dirname, "data/terminals.json")
SCANS_FILE_PATH = os.path.join(dirname, "data/scans.json")
SCANS_FILE_PATH = os.path.join(dirname, "data/cards.json")

def read_data(path):
    if os.path.isfile(path):
        opened_file = open(path, "r")
        file_content = opened_file.read()
        opened_file.close()
        return json.loads(file_content)

    return []

def write_data(path, array):
    path_dir = os.path.dirname(path)
    if not os.path.exists(path_dir):
        try:
            os.makedirs(path_dir)
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise

    opened_file = open(path, "w")
    json_str = json.dumps(array, indent=4, default=str)
    opened_file.write(json_str)
    opened_file.close()

people = read_data(PEOPLE_FILE_PATH)
terminals = read_data(TERMINALS_FILE_PATH)
scans = read_data(SCANS_FILE_PATH)
cards = read_data(SCANS_FILE_PATH)

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
        raise Exception(f"Card {id} already exists")

    cards.append(id)
    write_data(SCANS_FILE_PATH, cards)
    return id

def delete_card(id):
    global cards

    cards.remove(id)
    write_data(SCANS_FILE_PATH, cards)

def add_terminal(name):
    global terminals

    id = uuid.uuid1().int
    terminal = {'name': name, 'id': id}
    terminals.append(terminal)
    write_data(TERMINALS_FILE_PATH, terminals)
    return terminal

def delete_terminal(id):
    global terminals

    terminals = list(filter(lambda t: t['id'] != id, terminals))
    write_data(TERMINALS_FILE_PATH, terminals)

def add_person(full_name):
    global people

    id = uuid.uuid1().int
    person = {'full_name': full_name, 'id': id}
    people.append(person)
    write_data(PEOPLE_FILE_PATH, people)
    return person

def delete_person(id):
    global people

    people = list(filter(lambda t: t['id'] != id, people))
    write_data(PEOPLE_FILE_PATH, people)

def assign_card_id(person_id, card_id):
    global people

    person = find_person("id", person_id)
    person['card_id'] = card_id
    write_data(PEOPLE_FILE_PATH, people)

def remove_card_id(person_id):
    global people

    person = find_person("id", person_id)
    del person['card_id']
    write_data(PEOPLE_FILE_PATH, people)

def add_scan(terminal_id, card_id):
    global people
    global terminals
    global scans
    global cards

    time = datetime.now()
    person = find_person("card_id", card_id)
    terminal = find_terminal("id", terminal_id)

    if (not card_id in cards) or (terminal is None) or (person is None):
        scans.append({'card_id': card_id, 'terminal_id': terminal_id, 'time': time})
        write_data(SCANS_FILE_PATH, scans)

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

        write_data(SCANS_FILE_PATH, scans)
