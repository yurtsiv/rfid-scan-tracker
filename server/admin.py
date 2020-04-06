from data_handlers import *
from reports import generate_report
import sys, traceback

def input_int(min, max, label):
  while True:
    try:
      num = int(input("\n" + label))

      if num >= min and num <= max:
        return num

      print("Enter a number between " + str(min) + " and " + str(max))
    except Exception:
      print("Invalid input. Try again!")

def pick_from_list(l, label="Select an item: "):
  selected_item_index = input_int(1, len(l), label) - 1
  return l[selected_item_index]

def print_list(l):
  print("\n")
  for i in range(len(l)):
    print(str(i + 1) + ".  " + str(l[i]))

def print_and_pick_with_cancel(l, label="Select an item: "):
  print_list(l + ['Cancel'])
  picked_item = pick_from_list(l + [None], label=label)
  return picked_item

def add_person_menu():
  full_name = input("\nEnter full name: ")
  person = add_person(full_name)
  print("\nPerson added")
  print(person)

def delete_person_menu():
  people = get_people()
  if people == []:
    print("\nNo people")
  else:
    selected_person = print_and_pick_with_cancel(people, "Select a person: ")
    if selected_person is None:
      return
    
    delete_person(selected_person['id'])
    print("\nPerson deleted")

def add_terminal_menu():
  name = input("\nEnter terminal name: ")
  terminal = add_terminal(name)
  print("\nTerminal added")
  print(terminal)

def delete_terminal_menu():
  terminals = get_terminals()
  
  if terminals == []:
    print("No terminals")
  else:
    selected_terminal = print_and_pick_with_cancel(terminals, "Select terminal: ")
    if selected_terminal is None:
      return

    delete_terminal(selected_terminal['id'])
    print("\nTerminal deleted")

def assign_card_menu():
  cards = get_not_assigned_cards()
  people = get_people_without_card()

  if cards == []:
    print("\nAll cards are already assigned")
  elif people == []:
    print("\nNo emplyees or all of them have card assigned")
  else:
    selected_person = print_and_pick_with_cancel(people, "Select employee: ")
    if selected_person is None:
      return

    selected_card = print_and_pick_with_cancel(cards, "Select card: ")
    if selected_card is None:
      return

    assign_card_id(selected_person['id'], selected_card)
    print("\nCard assigned")

def unassign_card_menu():
  people = get_people_with_card()

  if people == []:
    print("\nNo employees to unassign card from")
  else:
    selected_person = print_and_pick_with_cancel(people, "Select person: ")
    if selected_person is None:
      return

    remove_card_id(selected_person['id'])
    print("\nCard unassigned")

def report_menu():
  people = get_people()

  selected_person = print_and_pick_with_cancel(people, "Select person: ")
  if selected_person is None:
    return
  
  generate_report(selected_person['id'])
  print("Report generated")

menu_items = [
  ("Add person", add_person_menu),
  ("Delete person", delete_person_menu),
  ("Add terminal", add_terminal_menu),
  ("Delete terminal", delete_terminal_menu),
  ("Assign card", assign_card_menu),
  ("Unassign card", unassign_card_menu),
  ("Generate report", report_menu),
  ("Exit", sys.exit)
]

def start_menu():
  print("\n")
  for i in range(len(menu_items)):
    print(str(i + 1) + ". " + menu_items[i][0])

  _, selected_func = pick_from_list(menu_items)
  selected_func()

while True:
  try:
    start_menu()
  except Exception as err:
    print(err)
