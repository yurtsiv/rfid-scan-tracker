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

It will start listening to cards scanning and publish card ID over MQTT.
