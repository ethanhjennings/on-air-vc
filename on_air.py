import platform
import subprocess
import sys
import time

import requests

DISPLAY_NAME = '' # Friendly display name: "Noam (work)" for example
START_MEETING_URL = '' # URL that will be called when a new meeting starts
END_MEETING_URL = '' # URL that will be called when a meeting ends

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
    make_request(START_MEETING_URL)

def on_end_meeting(os_name):
    make_request(END_MEETING_URL)

def in_meeting(os_name):
    if os_name == 'Darwin':
        return in_meeting_mac()
    elif os_name == 'Windows':
        return in_meeting_windows()

def in_meeting_mac():
    p1 = subprocess.Popen(['ps', 'x'], stdout=subprocess.PIPE)

    # zoom meeting ids have 9-10 digits, this may need to be updated in the future!
    p2 = subprocess.Popen(['grep', '-E', '\-key [0-9]{9,10}'], stdin=p1.stdout, stdout=subprocess.PIPE)
    p1.stdout.close()
    output = p2.communicate()[0] 
    
    if output:
        meeting_id = output.split()[-1].decode()
        return True
    else:
        return False

def in_meeting_windows():
    p = subprocess.Popen(['tasklist', '/fo', 'table', '/v', '/fi', 'imagename eq CptHost.exe'], stdout=subprocess.PIPE)
    output = p.communicate()[0]

    for line in str(output).splitlines():
        if line.find('CptHost.exe') > -1:
            return True
    return False

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
    last_state = False
    while True:
        is_in_meeting = in_meeting(os_name)

        if is_in_meeting and not last_state:
            print("New meeting started!")
            on_start_meeting(os_name)

        if not is_in_meeting and last_state:
            print("Meeting ended.")
            on_end_meeting(os_name)

        last_state = is_in_meeting
        time.sleep(1)
