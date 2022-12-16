# On Air (Video calls)
Script to detect when zoom is open on your computer! Compatible with both Windows and macOS, but only supports Zoom right now.

## Installation (Windows)
- Create a folder called `On Air` in your `Program Files` directory and copy `on_air.py` and `on_air.cmd` into it.
- Open the Windows task scheduler and right click `Task Scheduler Library` and choose `Create Task...`.\
- Make sure `Run with highest priviledges` is checked.
- On the `Triggers` tab add a trigger for `At log on`.
- On the `Actions` tab add an action to `Start a Program` and for the program paste in `"C:\Program Files\On Air\on_air.cmd"`
