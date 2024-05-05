import os
import random
import pygame

sound_floder = r"C:\Users\NekaAlimovv\Desktop\Создающейся проэкты\AKIMA_beta\joke\joke"

pygame.init()

sound_files = os.listdir(sound_floder)


def play_joke_sound():
     random_sound = random.choice(sound_files)

     sound_path = os.path.join(sound_floder, random_sound)

    # Воспроизводим выбранный звуковой файл
     pygame.mixer.music.load(sound_path)
     pygame.mixer.music.play()
     