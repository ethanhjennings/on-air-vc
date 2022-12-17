import platform
import re
import subprocess
import sys
import time

import requests
import config

'''
Script that continously checks for Zoom running and makes a url request when a meeting starts or ends.
'''

def make_request(url, retries=5):
    print("Making request...")
    tries = 0
    while tries < 5:
        try:
            r = requests.get(url)
            if r.status_code == 200:
                print("Success!")
                return
            else:
                print("Request had bad response retrying...", file=sys.stderr)
        except Exception:
            print("Unable to make request retrying...", file=sys.stderr)
        tries += 1
        time.sleep(30)
    print("Giving up!", file=sys.stderr)

def on_start_meeting(os_name):
    make_request(config.START_MEETING_URL)

def on_end_meeting(os_name):
    make_request(config.END_MEETING_URL)

def in_meeting(os_name):
    if os_name == 'Darwin':
        return in_meeting_mac()
    elif os_name == 'Windows':
        return in_meeting_windows()

def in_meeting_mac():
    p = subprocess.Popen(['ps', 'x'], stdout=subprocess.PIPE)
    output, err = p.communicate()

    return str(output).find("CptHost.app") > -1

def in_meeting_windows():
    p = subprocess.Popen(['tasklist', '/fo', 'table', '/v', '/fi', 'imagename eq CptHost.exe'], shell=True, stdout=subprocess.PIPE)
    output, err = p.communicate()[0]

    return str(output).find("CptHost.exe") > -1

def get_os():
    os_name = platform.system()
    if os_name == 'Darwin':
        print("Detected running on macOS")
    elif os_name == 'Windows':
        print("Detected running on Windows")
    else:
        print(f"Detected running on unsupported os: {os_name}", file=sys.stderr)
        sys.exit(1)

    return os_name

if __name__ == '__main__':
    os_name = get_os() 

    # Start with inverted so that it will trigger the first time
    last_state = not in_meeting(os_name)

    while True:
        is_in_meeting = in_meeting(os_name)

        if is_in_meeting and not last_state:
            print("New meeting started!")
            on_start_meeting(os_name)

        if not is_in_meeting and last_state:
            print("Meeting ended.")
            on_end_meeting(os_name)

        last_state = is_in_meeting
        sys.stdout.flush()
        time.sleep(config.CHECK_INTERVAL)
