import time
from datetime import datetime

from storage import load_alarms
from sound import play_alarm

def start_scheduler():
    
    current = datetime.now().strftime("%H:%M")
    print(f"Checking alarms at {current}")
    print("Alarm scheduler started")

    while True:

        current = datetime.now().strftime("%H:%M")

        print(f"Checking alarms at {current}")
        
        alarms = load_alarms()

        for alarm in alarms:

            if (
                alarm["enabled"]
                and alarm["time"] == current
            ):
                print(f"Alarm Triggered {current}")
                play_alarm()

        time.sleep(30)