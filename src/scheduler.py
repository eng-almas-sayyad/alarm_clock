import time
from datetime import datetime

from storage import load_alarms,save_alarms
from sound import play_alarm

def start_scheduler():
    
    print("Alarm scheduler started")

    while True:

        current = datetime.now().strftime("%H:%M")

        alarms = load_alarms()

        for alarm in alarms:

            if (
                alarm["enabled"]
                and alarm["time"] == current
            ):
                print(f"Alarm Triggered {current}")
                play_alarm()

                # Disable alarm after triggering
                alarm["enabled"] = False

                save_alarms(alarms)

        time.sleep(30)