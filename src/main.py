import click

from alarm_manager import AlarmManager
from scheduler import start_scheduler

manager = AlarmManager()

@click.group()
def cli():
    pass

@cli.command()
@click.argument("alarm_time")
def add(alarm_time):

    manager.add_alarm(alarm_time)

    print(f"Alarm added {alarm_time}")

@cli.command()
def list():

    alarms = manager.list_alarms()

    for alarm in alarms:
        print(alarm)

@cli.command()
@click.argument("alarm_id", type=int)
def delete(alarm_id):

    manager.delete_alarm(alarm_id)

    print("Deleted")

@cli.command()
def run():

    start_scheduler()

if __name__ == "__main__":
    cli()