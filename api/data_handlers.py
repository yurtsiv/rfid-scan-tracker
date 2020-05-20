"""
Utilities for working with data storage
"""

import errno
import json
import os
import uuid
from datetime import datetime
from api.list_utils import find_by, diff

DIRNAME = os.path.dirname(__file__)

CARDS_FILE_PATH = os.path.join(DIRNAME, "data/cards.json")
PEOPLE_FILE_PATH = os.path.join(DIRNAME, "data/people.json")
SCANS_FILE_PATH = os.path.join(DIRNAME, "data/scans.json")
TERMINALS_FILE_PATH = os.path.join(DIRNAME, "data/terminals.json")

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

def get_cards():
    """
    Get all cards
    """

    return read_data(CARDS_FILE_PATH)

def get_people():
    """
    Get all people
    """

    return read_data(PEOPLE_FILE_PATH)

def get_scans():
    """
    Get all scans
    """

    return read_data(SCANS_FILE_PATH)

def get_terminals():
    """
    Get all terminals
    """

    return read_data(TERMINALS_FILE_PATH)

def filter_people(key):
    """
    Get peopele by the specified condition
    """

    return [p for p in get_people() if key(p)]

def filter_scans(key):
    """
    Get scans by the specified condition
    """

    return [s for s in get_scans() if key(s)]

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

    people_with_cards = get_people_with_card()
    assigned_cards = list(map(lambda w: w['card_id'], people_with_cards))
    return diff(get_cards(), assigned_cards)

def find_person(key, val):
    """
    Get a person by key and value
    """

    return find_by(get_people(), key=lambda person: person.get(key) == val)

def find_terminal(key, val):
    """
    Get a terminal by key and value
    """

    return find_by(get_terminals(), key=lambda terminal: terminal.get(key) == val)

def add_card(card_id):
    """
    Add new card.
    Throw an error if such card already exists.
    """

    if card_id is None or not card_id.isdigit() or len(card_id) != 9:
        raise Exception(f"Invalid card ID {card_id}. It should consist of 9 numbers.")

    cards = get_cards()

    if card_id in cards:
        raise Exception(f"Card {card_id} already exists")

    cards.append(card_id)
    write_data(CARDS_FILE_PATH, cards)

    return card_id

def delete_card(card_id):
    """
    Delete a card
    """

    cards = get_cards()
    cards.remove(card_id)
    write_data(CARDS_FILE_PATH, cards)

def add_terminal(name):
    """
    Add new terminal
    """

    terminal_id = str(uuid.uuid4())
    terminal = {'name': name, 'id': terminal_id}
    terminals = get_terminals()
    terminals.append(terminal)
    write_data(TERMINALS_FILE_PATH, terminals)

    return terminal

def delete_terminal(terminal_id):
    """
    Delete a terminal by ID
    """

    new_terminals = list(filter(lambda t: t['id'] != terminal_id, get_terminals()))
    write_data(TERMINALS_FILE_PATH, new_terminals)

def add_person(full_name):
    """
    Add new person
    """

    person_id = str(uuid.uuid4())
    person = {'full_name': full_name, 'id': person_id}
    people = get_people()
    people.append(person)
    write_data(PEOPLE_FILE_PATH, people)

    return person

def delete_person(person_id):
    """
    Delete a person by ID
    """

    new_people = list(filter(lambda t: t['id'] != person_id, get_people()))
    write_data(PEOPLE_FILE_PATH, new_people)

def assign_card(person_id, card_id):
    """
    Assign a card to a particular person
    """

    people = get_people()
    person = find_by(people, lambda p: p.get("id") == person_id)
    person['card_id'] = card_id
    write_data(PEOPLE_FILE_PATH, people)

def unassign_card(person_id):
    """
    Unassign the card from a paticular person
    """

    people = get_people()
    person = find_by(people, lambda p: p.get("id") == person_id)
    del person['card_id']
    write_data(PEOPLE_FILE_PATH, people)

def add_scan(terminal_id, card_id):
    """
    Register scan of a card from a terminal.
    Check if specified termianl and card exist and if the card
    is assigned to any person. If not, an error is thrown
    but the record is added anyway (without "person_id")
    """

    cards = get_cards()
    scans = get_scans()

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

    scans.append({
        'card_id': card_id,
        'terminal_id': terminal_id,
        'person_id': person['id'],
        'time': time
    })

    write_data(SCANS_FILE_PATH, scans)
