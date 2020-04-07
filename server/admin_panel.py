"""
UI for controlling the server
"""

import sys
import data_handlers as dh
import reports

def input_int(min_val, max_val, label):
    """
    Get integer number from a user between min (inclusive) and max (inclusive).
    Loops until the input is correct
    """

    while True:
        try:
            num = int(input(f"\n{label}"))

            if min_val <= num <= max_val:
                return num

            print(f"Enter a number between {str(min_val)} and {str(max_val)}")
        except Exception:
            print("Invalid input. Try again!")

def pick_from_list(target_list, label="Select an item: "):
    """
    Ask user to select an element from list and return that element
    """

    selected_item_index = input_int(1, len(target_list), label) - 1
    return target_list[selected_item_index]

def print_list(target_list):
    """
    Print each element in the list prepending indecies (starting from 1)
    """

    print("\n")
    for i, elem in enumerate(target_list):
        print(f"{str(i + 1)}. {str(elem)}")

def print_and_pick_with_cancel(target_list, label="Select an item: "):
    """
    Print each element in the list with "Cancel" at the end
    then ask user to pick an element and return the selected element
    (None if "Cancel" is selected)
    """

    print_list(target_list + ['Cancel'])
    picked_item = pick_from_list(target_list + [None], label=label)
    return picked_item

def add_person_menu():
    """Menu for adding new person"""

    full_name = input("\nEnter full name: ")
    person = dh.add_person(full_name)
    print("\nPerson added")
    print(person)

def delete_person_menu():
    """Menu for deleting a person"""

    people = dh.get_people()
    if people == []:
        print("\nNo people")
    else:
        selected_person = print_and_pick_with_cancel(people, "Select person: ")
        if selected_person is None:
            return

        dh.delete_person(selected_person['id'])
        print("\nPerson deleted")

def add_card_menu():
    """Menu for adding new card"""

    card_id = input_int(0, 9999999999, "Enter RFID Number: ")
    card = dh.add_card(card_id)
    print("\nCard added")
    print(card)

def delete_card_menu():
    """Menu for deleting a card"""

    cards = dh.get_cards()

    if cards == []:
        print("\nNo cards")
    else:
        selected_card = print_and_pick_with_cancel(cards, "Select card: ")
        if selected_card is None:
            return

        dh.delete_card(selected_card)
        print("\nCard deleted")


def add_terminal_menu():
    """Menu for adding new terminal"""

    name = input("\nEnter terminal name: ")
    terminal = dh.add_terminal(name)
    print("\nTerminal added")
    print(terminal)

def delete_terminal_menu():
    """Menu for deleting a terminal"""

    terminals = dh.get_terminals()

    if terminals == []:
        print("\nNo terminals")
    else:
        selected_terminal = print_and_pick_with_cancel(terminals, "Select terminal: ")
        if selected_terminal is None:
            return

        dh.delete_terminal(selected_terminal['id'])
        print("\nTerminal deleted")

def assign_card_menu():
    """Menu for assigning a card to a person"""

    cards = dh.get_not_assigned_cards()
    people = dh.get_people_without_card()

    if cards == []:
        print("\nAll cards are already assigned")
    elif people == []:
        print("\nNo people or all of them have card assigned")
    else:
        selected_person = print_and_pick_with_cancel(people, "Select person: ")
        if selected_person is None:
            return

        selected_card = print_and_pick_with_cancel(cards, "Select card: ")
        if selected_card is None:
            return

        dh.assign_card(selected_person['id'], selected_card)
        print("\nCard assigned")

def unassign_card_menu():
    """Menu for unassigning a card from a person"""

    people = dh.get_people_with_card()

    if people == []:
        print("\nNo people to unassign card from")
    else:
        selected_person = print_and_pick_with_cancel(people, "Select person: ")
        if selected_person is None:
            return

        dh.unassign_card(selected_person['id'])
        print("\nCard unassigned")

def report_menu():
    """Menu for generating report for a person"""

    people = dh.get_people()

    selected_person = print_and_pick_with_cancel(people, "Select person: ")
    if selected_person is None:
        return

    reports.generate_report(selected_person['id'])
    print("\nReport generated. Look for CSV file in the current direcotry")

MENU_ITEMS = [
    ("Add person", add_person_menu),
    ("Delete person", delete_person_menu),
    ("Add card", add_card_menu),
    ("Delete card", delete_card_menu),
    ("Add terminal", add_terminal_menu),
    ("Delete terminal", delete_terminal_menu),
    ("Assign card", assign_card_menu),
    ("Unassign card", unassign_card_menu),
    ("Generate report", report_menu),
    ("Exit", sys.exit)
]

def start_menu():
    """Initiate main menu"""

    print("\n")
    for i, item in enumerate(MENU_ITEMS):
        print(str(i + 1) + ". " + item[0])

    _, selected_func = pick_from_list(MENU_ITEMS)
    selected_func()

while True:
    try:
        start_menu()
    except Exception as err:
        print(err)
