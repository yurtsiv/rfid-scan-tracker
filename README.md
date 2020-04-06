### Uruchominie projektu

* Ściągnąć kod
* Uruchomić plik `main.py`

### Struktura aplikacji
```
data/
--cards.json
--scans.json
--terminals.json
--people.json  
data_handlers.py
list_utils.py
main.py
reports.py
ui.py
```


`data/` - folder w którym znajdują się pliki `.json` z danymi

`data/cards.json` - plik zawierający dane o kartach

  przykład:
  ```
  [
    [148, 35, 65, 119],
    [150, 50, 90, 200],
  ]
  ```

`data/scans.json` - plik zawierający dane o skanowaniu kart

  pzykład:
  ```
  [
    {
      "card_id": [148, 35, 65, 119],
      "terminal_id": 144751913515096091035495503208707423722,
      "time": "2020-03-30 19:38:15.594836",
      "person_id": 1
    },
    {
      "card_id": [130, 21, 65, 119],
      "terminal_id": 12344913515096091035495503208707543,
      "time": "2020-03-30 19:39:15.594836",
    }
  ]

  ```
  P.S. jeśli niema "person_id" to ktoś zczytał niewadomą kartę lub na niewiadomy terminale)


`data/terminals.json` - plik zawierający dany o terminalach (klientach)

  przykład:
  ```
  [
    {
      "id": 16576223788569598977048293633576304106,
      "name": "Entrance 1"
    }
  ]
  ```
  
`data/people.json` - plik zawierający dany o pracownikach

  przykład:
  ```
  [
    {
      "id": 1,
      "full_name": "John Doe",
      "card_id": [148, 35, 65, 119]
    },
    
    {
      "id": 2,
      "full_name": "Michael Smith"
    }
  ]
  ```

`data_handlers.py` - zawiera funkcje pomocnicze dla pracy z danymi
* `read_data` - czyta i prasuje dane z pliku JSON
* `write_data` - koduje i zapisuje dane do pliku JSON
* `get_terminals` - zwraca listę wszystkich terminalów
* `get_people` - zwraca listę wszystkich pracowników
* `get_cards` - zwraca listę wszystkich kart
* `filter_people` - filtruje personów po zadanym predykacie
* `filter_scans` - filtruje personów po zadanym predykacie
* `get_people_with_card` - zwraca listę pracowników którzy mają kartę
* `get_people_without_card` - zwraca listę pracowników którzy nie mają karty
* `get_not_assigned_cards` - zwraca listę kart które nie są przypisane do pracownika
* `find_person` - zwraca jednego pracownika po zadanym kluczu i znaczeniu
* `find_terminal` - zwraca jeden terminal po zadanym kluczu i znaczeniu
* `add_card` - dodje kartę
* `delete_card` - usuwa kartę
* `add_terminal` - dodaje terminal generując unikalny `id`
* `delete_terminal` - usuwa terminal po `id`
* `assign_card` - przypisuje kartę do pracownika
* `unassign_card` - usuwa kartę z pracownika 
* `add_scan` - dodaje rejestrację (sprawdzając czy jest taki terminal i robotnik)

`list_utils.py` - zawiera funkcje pomocnicze dla pracy z listami

* `find_by` - zwraca jeden element z listy po zadanym predukacie
* `group_into_pairs` - grupuje sąsiednie elementy listy w pary'

  prykład:
  `group_into_pairs([1,2,3,4,5]) == [(1,2), (3,4), (5)]` 
* `diff` - zwraca różnice miedzy listami

`main.py` - główny plik aplikacji który startuje interfejs tekstowy

`reports.py` - zawiera funkcje pomocnicze do generowanie raportów
* `write_to_csv` - zapisuje do CSV dane o wejściach i wyjściach danego pracownika
* `generate_report` - generuje raport dla zadanego pracownika
  

`ui.py` - zawiera funkcjonalność związaną z interfejsem użytkownika
