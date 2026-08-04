#!/usr/bin/python3
import json
import datetime
import os

CACHE_FILE = os.path.expanduser('~/.cache/waybar-ycal/events.json')

def load_events():
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE) as f:
                return json.load(f)
        except Exception:
            pass
    return {}

now = datetime.datetime.now()
today = now.date()
events = load_events()
today_events = events.get(today.isoformat(), [])

date_tooltip = f"<big>{now.strftime('%d of %B, %Y')}</big>"
formatted_list = "\n".join([f"- {event}" for event in today_events])
events_tooltip = f"<big><b>Today events:</b></big>\n{formatted_list if formatted_list else "\n- no events"}"

output = {
    "text": f"\U000f00ed  {now.strftime('%A %H:%M')}",
    "alt": f"\U000f00ed  {now.strftime('%d/%m/%Y %H:%M')}",
    "tooltip": f"{date_tooltip}\n\n{events_tooltip}",
}

print(json.dumps(output))
