import pygame
import time
from pathlib import Path

pygame.mixer.init()


BASE_DIR = Path(__file__).resolve().parent.parent
ALARM_FILE = BASE_DIR / "sounds" / "alarm.wav"
if not ALARM_FILE.exists():
    raise FileNotFoundError(
        f"Alarm sound not found: {ALARM_FILE}"
    )
def play_alarm():
    sound = pygame.mixer.Sound(str(ALARM_FILE))
    sound.play()

    time.sleep(sound.get_length())