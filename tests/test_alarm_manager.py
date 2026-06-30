from alarm_manager import AlarmManager

def test_add_alarm():

    manager = AlarmManager()

    manager.add_alarm("10:30")

    alarms = manager.list_alarms()

    assert len(alarms) > 0