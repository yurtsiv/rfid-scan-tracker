# settings

Global settings


# server

App server which listens to incoming messages
and collects information on card scannings coming
from clients/terminals


# admin_panel

UI for editing data in the system
and generating reports


## input_int
```python
input_int(min_val, max_val, label)
```

Get integer number from a user between min (inclusive) and max (inclusive).
Loops until the input is correct


## pick_from_list
```python
pick_from_list(target_list, label='Select an item: ')
```

Ask user to select an element from list and return that element


## print_list
```python
print_list(target_list)
```

Print each element in the list prepending indecies (starting from 1)


## print_and_pick_with_cancel
```python
print_and_pick_with_cancel(target_list, label='Select an item: ')
```

Print each element in the list with "Cancel" at the end
then ask user to pick an element and return the selected element
(None if "Cancel" is selected)


## add_person_menu
```python
add_person_menu()
```
Menu for adding new person

## delete_person_menu
```python
delete_person_menu()
```
Menu for deleting a person

## add_card_menu
```python
add_card_menu()
```
Menu for adding new card

## delete_card_menu
```python
delete_card_menu()
```
Menu for deleting a card

## add_terminal_menu
```python
add_terminal_menu()
```
Menu for adding new terminal

## delete_terminal_menu
```python
delete_terminal_menu()
```
Menu for deleting a terminal

## assign_card_menu
```python
assign_card_menu()
```
Menu for assigning a card to a person

## unassign_card_menu
```python
unassign_card_menu()
```
Menu for unassigning a card from a person

## report_menu
```python
report_menu()
```
Menu for generating report for a person

## start_menu
```python
start_menu()
```
Initiate main menu

# client

The client which runs on a RaspberryPI.
Listens to card scanning and publishes card ID


# api.data_handlers

Utilities for working with data storage


## read_data
```python
read_data(path)
```

Read and decode data from a JSON file.
Return [] if no file


## write_data
```python
write_data(path, array)
```

Encode and write data to a JSON file.
If no file the function will create one


## get_cards
```python
get_cards()
```

Get all cards


## get_people
```python
get_people()
```

Get all people


## get_scans
```python
get_scans()
```

Get all scans


## get_terminals
```python
get_terminals()
```

Get all terminals


## filter_people
```python
filter_people(key)
```

Get peopele by the specified condition


## filter_scans
```python
filter_scans(key)
```

Get scans by the specified condition


## get_people_with_card
```python
get_people_with_card()
```

Get people who have some card assigned


## get_people_without_card
```python
get_people_without_card()
```

Get people who don't have any card assigned


## get_not_assigned_cards
```python
get_not_assigned_cards()
```

Get cards which aren't assigned to any person


## find_person
```python
find_person(key, val)
```

Get a person by key and value


## find_terminal
```python
find_terminal(key, val)
```

Get a terminal by key and value


## add_card
```python
add_card(card_id)
```

Add new card.
Throw an error if such card already exists.


## delete_card
```python
delete_card(card_id)
```

Delete a card


## add_terminal
```python
add_terminal(name)
```

Add new terminal


## delete_terminal
```python
delete_terminal(terminal_id)
```

Delete a terminal by ID


## add_person
```python
add_person(full_name)
```

Add new person


## delete_person
```python
delete_person(person_id)
```

Delete a person by ID


## assign_card
```python
assign_card(person_id, card_id)
```

Assign a card to a particular person


## unassign_card
```python
unassign_card(person_id)
```

Unassign the card from a paticular person


## add_scan
```python
add_scan(terminal_id, card_id)
```

Register scan of a card from a terminal.
Check if specified termianl and card exist and if the card
is assigned to any person. If not, an error is thrown
but the record is added anyway (without "person_id")


# api.reports

Report generation functionality


## write_to_csv
```python
write_to_csv(person_name, regs_groups)
```

Helper function for saving generated
report into a CSV file


## generate_report
```python
generate_report(person_id)
```

Generate the report for a particular person


# api.list_utils

A few helpers for working with lists


## find_by
```python
find_by(l, key)
```

Find an element in a list by a specified condition


## group_into_pairs
```python
group_into_pairs(l)
```

Group neighbour elements into pairs

Examples:

group_into_pairs([1,2,3,4]) == [(1,2), (3,4)]
group_into_pairs([1,2,3]) == [(1,2), (3)]


## diff
```python
diff(l1, l2)
```

Find the difference between two lists

