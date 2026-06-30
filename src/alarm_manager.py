from storage import load_alarms, save_alarms

class AlarmManager:

    def add_alarm(self, alarm_time):
        alarms = load_alarms()

        alarm = {
            "id": len(alarms) + 1,
            "time": alarm_time,
            "enabled": True
        }

        alarms.append(alarm)
        save_alarms(alarms)

    def list_alarms(self):
        return load_alarms()

    def delete_alarm(self, alarm_id):
        alarms = load_alarms()

        alarms = [
            a for a in alarms
            if a["id"] != alarm_id
        ]

        save_alarms(alarms)