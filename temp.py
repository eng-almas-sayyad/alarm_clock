import pygame

pygame.mixer.init()

sound = pygame.mixer.Sound("sounds/alarm.wav")

sound.play()

input("Press Enter to exit...")