### Uruchominie projektu

* Ściągnąć kod
* Uruchomić plik `main.py`

### Struktura aplikacji

`data/`
---- `cards.json`
---- `registrations.json`
---- `terminals.json`
---- `workers.json`  
`data_handlers.py`
`list_utils.py`
`main.py`
`reports.py`
`ui.py`


`data/` - folder w którym znajdują się pliki `.json` z danymi

`data/cards.json` - plik zawierający dane o kartach
  przykład:
  ```
  [
    [148, 35, 65, 119],
    [150, 50, 90, 200],
  ]
  ```

`data/registrations.json` - plik zawierający dane o skanowaniu kart
  pzykład:
  ```
  [
    {
      "cardId": [148, 35, 65, 119],
      "terminalId": 144751913515096091035495503208707423722,
      "time": "2020-03-30 19:38:15.594836",
      "workerId": 1
    },
    {
      "cardId": [130, 21, 65, 119],
      "terminalId": 12344913515096091035495503208707543,
      "time": "2020-03-30 19:39:15.594836",
    }
  ]

  ```
  P.S. jeśli niema "workerId" to ktoś zczytał niewadomą kartę lub na niewiadomy terminale)


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

`data_handlers.py` - zawiera funkcje pomocnicze dla pracy z danymi
* `read_data` - czyta i prasuje dane z pliku JSON
* `write_data` - koduje i zapisuje dane do pliku JSON
* `get_terminals` - zwraca listę wszystkich terminalów
* `get_workers` - zwraca listę wszystkich pracowników
* `get_cards` - zwraca listę wszystkich kart
* `filter_workers` - filtruje workerów po zadanym predykacie
* `filter_registrations` - filtruje workerów po zadanym predykacie
* `get_workers_with_card` - zwraca listę pracowników którzy mają kartę
* `get_workers_without_card` - zwraca listę pracowników którzy nie mają karty
* `get_not_assigned_cards` - zwraca listę kart które nie są przypisane do pracownika
* `find_worker` - zwraca jednego pracownika po zadanym kluczu i znaczeniu
* `find_terminal` - zwraca jeden terminal po zadanym kluczu i znaczeniu
* `add_card` - dodje kartę
* `delete_card` - usuwa kartę
* `add_terminal` - dodaje terminal generując unikalny `id`
* `delete_terminal` - usuwa terminal po `id`
* `assign_card_id` - przypisuje kartę do pracownika
* `remove_card_id` - usuwa kartę z pracownika 
* `add_registration` - dodaje rejestrację (sprawdzając czy jest taki terminal i robotnik)

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
