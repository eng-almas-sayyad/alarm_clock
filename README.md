# Python CLI Alarm Clock

A lightweight, production-oriented Alarm Clock application built using Python and the Command Line Interface (CLI).

The application allows users to create, list, delete, and execute alarms directly from the terminal. Alarm data is persisted locally using a JSON file, and alarm notifications are delivered through audio playback using Pygame.

## Features

* Set alarms using HH:MM format
* Multiple alarm support
* Persistent storage using JSON
* Alarm sound notifications
* List configured alarms
* Delete alarms
* Input validation
* Logging support
* Unit testing support
* Cross-platform (Windows, Linux, macOS)

## Technology Stack

| Component   | Version |
| ----------- | ------- |
| Python      | 3.11+   |
| Click       | 8.2.1   |
| Pygame      | 2.6.1   |
| Pytest      | 8.4.1   |
| APScheduler | 3.11.0  |
| Rich        | 14.1.0  |

## Project Structure

```text
alarm-clock/
│
├── alarms.json
├── requirements.txt
├── README.md
│
├── src/
│   ├── main.py
│   ├── scheduler.py
│   ├── alarm_manager.py
│   ├── storage.py
│   ├── sound.py
│   └── models.py
│
├── sounds/
│   └── alarm.wav
│
├── tests/
│   ├── test_alarm_manager.py
│   └── test_storage.py
│
└── logs/
    └── app.log
```

## Prerequisites

Install one of the following Python versions:

* Python 3.11.x
* Python 3.12.x
* Python 3.13.x

Verify installation:

```bash
python --version
```

Expected output:

```text
Python 3.11.x
```

## Setup Instructions

### 1. Clone Repository

```bash
git clone <repository-url>
cd alarm-clock
```

### 2. Create Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Verify installation:

```bash
pip list
```

## Create Required Files

### alarms.json

Create a file named `alarms.json` in the project root:

```json
[]
```

### Alarm Sound

Place a valid audio file inside:

```text
sounds/alarm.wav
```

Note: WAV files are recommended for better compatibility with Pygame.

## Running the Application

### Add an Alarm

```bash
python src/main.py add 18:30
```

Output:

```text
Alarm added 18:30
```

### View All Alarms

```bash
python src/main.py list
```

Example Output:

```text
{'id': 1, 'time': '18:30', 'enabled': True}
```

### Delete an Alarm

```bash
python src/main.py delete 1
```

Output:

```text
Deleted
```

### Start Alarm Scheduler

```bash
python src/main.py run
```

Output:

```text
Alarm scheduler started
```

Keep the terminal open while the scheduler is running.

## Example Workflow

### Add Alarm

```bash
python src/main.py add 19:00
```

### Verify Alarm

```bash
python src/main.py list
```

### Start Scheduler

```bash
python src/main.py run
```

When system time reaches 19:00, the alarm sound will be played automatically.

## Running Tests

Execute all unit tests:

```bash
pytest
```

Expected output:

```text
========================
2 passed
========================
```

## Logging

Application logs are stored in:

```text
logs/app.log
```

Example log entries:

```text
2026-06-30 18:00:00 INFO Alarm Added
2026-06-30 19:00:00 INFO Alarm Triggered
```

## Troubleshooting

### Alarm Not Triggering

Verify:

* Scheduler is running
* Alarm time is correct
* Alarm is enabled
* System clock is accurate

### No Sound Playing

Verify:

* `alarm.wav` exists
* System volume is not muted
* Pygame is installed correctly

Test audio independently:

```bash
python -c "from src.sound import play_alarm; play_alarm()"
```

### JSON Decode Error

Ensure `alarms.json` contains valid JSON:

```json
[]
```

## Future Enhancements

* Snooze functionality
* Recurring alarms
* Alarm categories
* Desktop notifications
* Alarm editing
* Rich CLI dashboard
* Configuration management
* Packaging as executable using PyInstaller
* APScheduler-based scheduling engine

## Author

Developed as a production-oriented Python CLI MVP demonstrating:

* Python application design
* CLI development
* File-based persistence
* Scheduling concepts
* Audio handling
* Testing practices
* Clean project structure
