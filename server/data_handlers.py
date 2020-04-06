"""
Utilities for working with data storage
"""

import errno
import json
import os
import uuid
from datetime import datetime
from list_utils import find_by, diff

DIRNAME = os.path.dirname(__file__)

PEOPLE_FILE_PATH = os.path.join(DIRNAME, "data/PEOPLE.json")
TERMINALS_FILE_PATH = os.path.join(DIRNAME, "data/TERMINALS.json")
SCANS_FILE_PATH = os.path.join(DIRNAME, "data/scans.json")
CARDS_FILE_PATH = os.path.join(DIRNAME, "data/cards.json")

def read_data(path):
    """
    Read and decode data from a JSON file.
    Return [] if no file
    """

    if os.path.isfile(path):
        opened_file = open(path, "r")
        file_content = opened_file.read()
        opened_file.close()
        return json.loads(file_content)

    return []

def write_data(path, array):
    """
    Encode and write data to a JSON file.
    If no file the function will create one
    """

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

PEOPLE = read_data(PEOPLE_FILE_PATH)
TERMINALS = read_data(TERMINALS_FILE_PATH)
SCANS = read_data(SCANS_FILE_PATH)
CARDS = read_data(CARDS_FILE_PATH)

def get_terminals():
    """
    Get all terminals
    """

    global TERMINALS

    return TERMINALS

def get_people():
    """
    Get all people
    """

    global PEOPLE

    return PEOPLE

def get_cards():
    """
    Get all cards
    """

    global CARDS

    return CARDS

def filter_people(key):
    """
    Get peopele by the specified criterion
    """

    global PEOPLE

    return [w for w in PEOPLE if key(w)]

def filter_scans(key):
    """
    Get scans by the specified criterion
    """

    global SCANS

    return [r for r in SCANS if key(r)]

def get_people_with_card():
    """
    Get people who have some card assigned
    """

    return filter_people(lambda w: w.get('card_id') is not None)

def get_people_without_card():
    """
    Get people who don't have any card assigned
    """

    return filter_people(lambda w: w.get('card_id') is None)

def get_not_assigned_cards():
    """
    Get cards which aren't assigned to any person
    """

    global CARDS

    people_with_cards = get_people_with_card()
    assigned_cards = list(map(lambda w: w['card_id'], people_with_cards))
    return diff(CARDS, assigned_cards)

def find_person(key, val):
    """
    Get a person by key and value
    """

    global PEOPLE

    return find_by(PEOPLE, key=lambda person: person.get(key) == val)

def find_terminal(key, val):
    """
    Get a terminal by key and value
    """

    global TERMINALS

    return find_by(TERMINALS, key=lambda terminal: terminal.get(key) == val)

def add_card(card_id):
    """
    Add new card.
    Throw an error if such card already exists.
    """

    global CARDS

    if card_id in CARDS:
        raise Exception(f"Card {card_id} already exists")

    CARDS.append(card_id)
    write_data(CARDS_FILE_PATH, CARDS)

    return card_id

def delete_card(card_id):
    """
    Delete a card
    """

    global CARDS

    CARDS.remove(card_id)
    write_data(CARDS_FILE_PATH, CARDS)

def add_terminal(name):
    """
    Add new terminal
    """

    global TERMINALS

    terminal_id = uuid.uuid1().int
    terminal = {'name': name, 'id': terminal_id}
    TERMINALS.append(terminal)
    write_data(TERMINALS_FILE_PATH, TERMINALS)

    return terminal

def delete_terminal(terminal_id):
    """
    Delete a terminal by ID
    """

    global TERMINALS

    TERMINALS = list(filter(lambda t: t['id'] != terminal_id, TERMINALS))
    write_data(TERMINALS_FILE_PATH, TERMINALS)

def add_person(full_name):
    """
    Add new person
    """

    global PEOPLE

    person_id = uuid.uuid1().int
    person = {'full_name': full_name, 'id': person_id}
    PEOPLE.append(person)
    write_data(PEOPLE_FILE_PATH, PEOPLE)

    return person

def delete_person(person_id):
    """
    Delete a person by ID
    """

    global PEOPLE

    PEOPLE = list(filter(lambda t: t['id'] != person_id, PEOPLE))
    write_data(PEOPLE_FILE_PATH, PEOPLE)

def assign_card(person_id, card_id):
    """
    Assign a card to a particular person
    """

    global PEOPLE

    person = find_person("id", person_id)
    person['card_id'] = card_id
    write_data(PEOPLE_FILE_PATH, PEOPLE)

def unassign_card(person_id):
    """
    Unassign the card from a paticular person
    """

    global PEOPLE

    person = find_person("id", person_id)
    del person['card_id']
    write_data(PEOPLE_FILE_PATH, PEOPLE)

def add_scan(terminal_id, card_id):
    """
    Register scan of a card from a terminal.
    Check if specified termianl and card exist and if the card
    is assigned to any person. If not, an error is thrown
    but the record is added anyway (without "person_id")
    """

    global PEOPLE
    global TERMINALS
    global SCANS
    global CARDS

    time = datetime.now()
    person = find_person("card_id", card_id)
    terminal = find_terminal("id", terminal_id)

    if (not card_id in CARDS) or (terminal is None) or (person is None):
        SCANS.append({'card_id': card_id, 'terminal_id': terminal_id, 'time': time})
        write_data(SCANS_FILE_PATH, SCANS)

        err_msg = ""
        if not card_id in CARDS:
            err_msg = f"Card {card_id} isn't registered in the system"
        elif terminal is None:
            err_msg = f"Terminal {terminal_id} isn't registered in the system"
        else:
            err_msg = f"Card {card_id} isn't assigned to any person"

        raise Exception(err_msg)

    SCANS.append({
        'card_id': card_id,
        'terminal_id': terminal_id,
        'person_id': person['id'],
        'time': time
    })

    write_data(SCANS_FILE_PATH, SCANS)
