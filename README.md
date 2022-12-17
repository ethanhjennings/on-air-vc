# On Air (Video calls)
Script to detect when zoom is open on your computer! Compatible with both Windows and macOS, but only supports Zoom right now.

## Installation (Mac)
- Edit `config.py` with the urls/settings you want
- Clone this repo then run this command inside to setup the application:
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

## Installation (Windows)
- Edit `config.py` with the urls/settings you want
- Create a folder called `On Air` in your `Program Files` directory and copy `on_air.py` and `on_air.cmd` into it.
- Open the Windows task scheduler and right click `Task Scheduler Library` and choose `Create Task...`.\
- Make sure `Run with highest priviledges` is checked.
- On the `Triggers` tab add a trigger for `At log on`.
- On the `Actions` tab add an action to `Start a Program` and for the program paste in `"C:\Program Files\On Air\on_air.cmd"`

