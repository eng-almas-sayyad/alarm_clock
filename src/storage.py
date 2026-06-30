import json
from pathlib import Path

FILE = Path("alarms.json")

def load_alarms():
    if not FILE.exists():
        return []

    with open(FILE, "r") as f:
        return json.load(f)

def save_alarms(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)