# On Air (Video calls)
Background application to detect when zoom is open on your computer and make web requests for home/computer automation! Compatible with both Windows and macOS, but only supports Zoom right now.

This project is inspired by similar projects/ideas, but works for both Windows and mac, and can run as a background daemon/service:
https://www.easyprogramming.net/raspberrypi/aiim.php
https://community.home-assistant.io/t/zoom-meeting-monitoring-to-ha/246336

## Running in the terminal
If you just want to play with it in the terminal, first edit `config.py` with the urls and other settings you want and then install dependencies:
```
pip3 install -r requirements.txt
```

and run it with:
```
python3 on_air.py
```

## Installing as a background daemon/service

### Mac
- Clone this repo and edit `config.py` with the urls and other settings you want.
- Run this command from inside the repo to setup the application:
```
mkdir /Applications/on_air/; cp -r * /Applications/on_air/
```

- Then, run this command to setup the virtual environment:
```
cd /Applications/on_air/; python3 -m venv venv; source venv/bin/activate; pip3 install -r requirements.txt; deactivate
```

- Finally, run this command to setup and start the daemon: (Note: this one requires `sudo` access)
```
sudo cp me.ethanj.onair.plist /Library/LaunchAgents; launchctl load /Library/LaunchAgents/me.ethanj.onair.plist
```

### Windows
- Edit `config.py` with the urls/settings you want
- Create a folder called `On Air` in your `Program Files` directory and copy `on_air.py` and `on_air.cmd` into it.
- Open the Windows task scheduler and right click `Task Scheduler Library` and choose `Create Task...`.\
- Make sure `Run with highest priviledges` is checked.
- On the `Triggers` tab add a trigger for `At log on`.
- On the `Actions` tab add an action to `Start a Program` and for the program paste in `"C:\Program Files\On Air\on_air.cmd"`
