## Installation and running

### Preparation
1. Clone the repository
```
git clone https://github.com/yurtsiv/rfid-scan-tracker.git
```

2. Go to the project root directory
```
cd rfid-scan-tracker
```
3. Install packages
```
pip install -r requirements.txt --user
```

4. Change MQTT broker in `settings.py` if needed. The default is public `mqtt.eclipse.org`


### Running the server

First of all you want to add some data to the system. There's a handy UI which I'll call "admin panel" from now on. You can start it by running
```
python3 admin_panel.py
```

The admin panel allows you to add/remove people, cards, terminals as well as generate reports.

For demonstration purposes there's some dummy data already.

In order to start the actual server run

```
python3 server.py
```

It will start listening to incoming messages, log those to the console and collect information on cards scanning comming from terminals.

### Running the client on a terminal

In order to start the client run
```
python3 client.py <Terminal ID>
```

where  `<Terminal ID>` is a uniq ID of a terminal which you get when adding a terminal from the admin panel.

For quick testing you can use the predefined dummy terminal

```
python3 client.py 116556985421650370293137446037868150250
```

For now it just simulates scanning of predefined cards each 5 seconds.

TODO: listening to actual cards scanning from RFID detector


## Code

For detailed code documentation look into CODE_DOCS.md