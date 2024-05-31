import ctypes
import os
import random
import time
import speech_recognition as sr
import pygame
from googleapiclient.discovery import build
import webbrowser as wb
import subprocess
from PIL import ImageGrab
from colorama import Fore, Style
import sys
sys.path.append(r'C:\Users\NekaAlimovv\Desktop\Создающейся проэкты\AKIMA_beta\ScreenShot\screen.py')
sys.path.append(r'C:\Users\NekaAlimovv\Desktop\Создающейся проэкты\AKIMA_beta\joke\random_meme.py')  
from joke.random_meme import play_joke_sound, sound_floder
from Screen.screen import take_screenshot,save_path

API_KEY = 'AIzaSyAjJz-wQtZ5BQT_yMf2Y6eFSVIiaQg3sio'
pygame.mixer.init()

# Функция Поиск в Браузере
def search_in_browser(query, browser="chrome"):
    search_url = "http://www.google.com/search?q=" + query
    try:
        if browser.lower() == "chrome":
            subprocess.Popen([r'C:\Program Files\Google\Chrome\Application\chrome.exe', search_url])
        elif browser.lower() == "firefox":
            subprocess.Popen([r'C:\Program Files\Mozilla Firefox\firefox.exe', search_url])
        else:
            subprocess.Popen([browser, search_url])
    except Exception as e:
        print("Error:", e)

# Функция Поиск в Юутбе

def search_video(query):
    youtube = build('youtube', 'v3', developerKey=API_KEY)
    request = youtube.search().list(
        part='snippet',
        q=query,
        maxResults=1,
        type='video'
    )
    response = request.execute()
    video_id = response['items'][0]['id']['videoId']
    return f'https://www.youtube.com/watch?v={video_id}'

def play_video(video_url):
    wb.open(video_url)

def search_in_youtube(query):
    search_url = "https://www.youtube.com/results?search_query=" + query
    wb.open(search_url)
# Функция для воспроизведения случайного звука из папки
def play_random_sound(sound_folder):
    sound_files = [f for f in os.listdir(sound_folder) if f.endswith('.wav')]
    if sound_files:
        random_sound = random.choice(sound_files)
        sound_path = os.path.join(sound_folder, random_sound)
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play()

# Функция для открытия программ
def open_programs(programs):
    for program_name in programs:
        os.startfile(program_name)
        play_random_sound(r'C:\Users\NekaAlimovv\Desktop\Создающейся проэкты\AKIMA_beta\sound\OK')

# Функция для закрытия программ
def close_programs(programs):
    for program_name in programs:
        os.system(f"taskkill /f /im {program_name}")
        play_random_sound(r'C:\Users\NekaAlimovv\Desktop\Создающейся проэкты\AKIMA_beta\sound\OK')

# Функция для воспроизведения звука при запуске
def play_startup_sound():
    startup_sound_path = r'C:\Users\NekaAlimovv\Desktop\Создающейся проэкты\AKIMA_beta\sound\Run\run.wav'
    pygame.mixer.music.load(startup_sound_path)
    pygame.mixer.music.play()

# Функция для воспроизведения звука при выключении
def play_shutdown_sound():
    shutdown_sound_path = r'C:\Users\NekaAlimovv\Desktop\Создающейся проэкты\AKIMA_beta\sound\Run\off.wav'
    pygame.mixer.music.load(shutdown_sound_path)
    pygame.mixer.music.play()

def play_error():
    error_file = 'C:\\Users\\NekaAlimovv\\Desktop\\Создающейся проэкты\\AKIMA_beta\\sound\\error\\not_found.wav'
    if os.path.exists(error_file):
        pygame.mixer.init()
        pygame.mixer.music.load(error_file)
        pygame.mixer.music.play()
    else:
        print("Error: Sound file not found.")

# Функция для распознавания речи
def voice_command():
    recognizer = sr.Recognizer()

    print("Говорите что-то...")
    with sr.Microphone() as source:
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language='ru-RU')
        print("Вы сказали:", command)
        return command.lower()
    except sr.UnknownValueError:
        print("Извините, не удалось распознать команду.")
        return ""
    except sr.RequestError:
        print("Проблема с подключением к сервису распознавания речи.")
        return ""

sound_folder = r'C:\Users\NekaAlimovv\Desktop\Создающейся проэкты\AKIMA_beta\sound\OK'

play_startup_sound()

while True:
    command = voice_command()

    if "открой" in command:
        programs = []

        if "chrome" in command:
            programs.append(r'C:\Users\NekaAlimovv\Desktop\Создающейся проэкты\AKIMA_beta\Application\chrome\ahk\open_chrome.exe')
        if "discord" in command:
            programs.append(r'C:\Users\NekaAlimovv\Desktop\Создающейся проэкты\AKIMA_beta\Application\discord\ahk\discord.exe')
        if "cs2" in command:
            programs.append(r'C:\Users\NekaAlimovv\Desktop\Создающейся проэкты\AKIMA_beta\Application\cs2\ahk\open_cs2.exe')
        if "explorer" in command:
            programs.append(r'C:\Users\NekaAlimovv\Desktop\Создающейся проэкты\AKIMA_beta\Application\explorer\ahk\explorer.exe')
        if "FL Stduio" in command:
            programs.append(r'C:\Users\NekaAlimovv\Desktop\Создающейся проэкты\AKIMA_beta\Application\flstudio\ahk\flstudio.exe')
        if "minecraft" in command:
            programs.append(r'C:\Users\NekaAlimovv\Desktop\Создающейся проэкты\AKIMA_beta\Application\minecraft\ahk\minecraft.exe')
        if "steam" in command:
            programs.append(r'C:\Users\NekaAlimovv\Desktop\Создающейся проэкты\AKIMA_beta\Application\steam\ahk\open_steam.exe')
        if "sublime" in command:
            programs.append(r'C:\Users\NekaAlimovv\Desktop\Создающейся проэкты\AKIMA_beta\Application\sublime\ahk\open_sublime.exe')
        if "visual studio" in command:
            programs.append(r'C:\Users\NekaAlimovv\Desktop\Создающейся проэкты\AKIMA_beta\Application\vscode\ahk\open_vscode.exe')
        if "диспетчер задач" in command:
            programs.append('taskmgr.exe')
        if "диспетчер устройств" in command:
            programs.append('mmc.exe')
        if "пуск" in command:
            programs.append('explorer.exe')
        if "командную строку" in command:
            programs.append('cmd.exe')
        if "настройки" in command:
            programs.append(r'C:\Windows\ImmersiveControlPanel\SystemSettings.exe')
        open_programs(programs)
    elif "закрой" in command:
        programs = []
        if "диспетчер задач" in command:
            programs.append("taskkill /f /fi taskmgr.exe")
        if "диспетчер устройств" in command:
            programs.append("taskkill /f /fi mmc.exe")
        if "пуск" in command:
            programs.append("explorer.exe")
        elif "закрой панель управления" in command:
          os.system("taskkill /f /fi \"WINDOWTITLE eq Панель управления\"")
        play_random_sound(sound_folder)  
        if "командную строку" in command:
            programs.append("cmd.exe")
        if "настройки" in command:
            programs.append("SystemSettings.exe")
        if "chrome" in command:
            programs.append("chrome.exe")
        if "discord" in command:
            programs.append("Discord.exe")
        if "cs2" in command:
            programs.append("cs2.exe")
        if "Explorer" in command:
            programs.append("explorer.exe")
        if "FL Studio" in command:
            programs.append("FL64.exe")
        if "minecraft" in command:
            programs.append("java.exe")
        if "steam" in command:
            programs.append("steam.exe")
        if "sublime" in command:
            programs.append("sublime_text.exe")
        if "Visual Studio" in command:
            programs.append("Code.exe")
        if "Не принимай игру" in command:
            programs.append("autoaccept.exe")

        close_programs(programs)
    elif "Закрой все вкладки" in command:
        programs = []
        programs.append(r'C:\Users\NekaAlimovv\Desktop\Создающейся проэкты\AKIMA_beta\Application\listing\all_close_bowser.exe')
        open_programs(programs)
    elif "Закрой вкладку" in command:
        programs = []
        programs.append(r'C:\Users\NekaAlimovv\Desktop\Создающейся проэкты\AKIMA_beta\Application\listing\close_browser_openwik.exe')
        open_programs(programs)
    elif "сверни все окна" in command:
        programs = []
        programs.append(r'C:\Users\NekaAlimovv\Desktop\Создающейся проэкты\AKIMA_beta\Application\listing\open_okon.exe')
        open_programs(programs)
    elif "разверни все окна" in command:
        programs = []
        programs.append(r'C:\Users\NekaAlimovv\Desktop\Создающейся проэкты\AKIMA_beta\Application\listing\open_okon.exe')
        open_programs(programs)
    elif   command in["звук на макс", "звук на 100%"]:
        programs = []
        programs.append(r"C:\Users\NekaAlimovv\Desktop\Создающейся проэкты\AKIMA_beta\Application\volume\ahk\volume_max.exe")
        open_programs(programs)
    elif "звук на мин" in command:
        programs = []
        programs.append(r"C:\Users\NekaAlimovv\Desktop\Создающейся проэкты\AKIMA_beta\Application\volume\ahk\volume_min.exe")
        open_programs(programs)
    elif "звук на 10%" in command:
         programs = []
         programs.append(r"C:\Users\NekaAlimovv\Desktop\Создающейся проэкты\AKIMA_beta\Application\volume\ahk\volume_10.exe")
         open_programs(programs)
    elif "звук на 20%" in command:
         programs = []
         programs.append(r"C:\Users\NekaAlimovv\Desktop\Создающейся проэкты\AKIMA_beta\Application\volume\ahk\volume_20.exe")
         open_programs(programs)
    elif "звук на 30%" in command:
         programs = []
         programs.append(r"C:\Users\NekaAlimovv\Desktop\Создающейся проэкты\AKIMA_beta\Application\volume\ahk\volume_30.exe")
         open_programs(programs)
    elif "звук на 40%" in command:
         programs = []
         programs.append(r"C:\Users\NekaAlimovv\Desktop\Создающейся проэкты\AKIMA_beta\Application\volume\ahk\volume_40.exe")
         open_programs(programs)
    elif "звук на 50%" in command:
         programs = []
         programs.append(r"C:\Users\NekaAlimovv\Desktop\Создающейся проэкты\AKIMA_beta\Application\volume\ahk\volume_50.exe")
         open_programs(programs)
    elif "ищи в браузере" in command:
        query = command.replace("ищи в браузере", "").strip()
        search_in_browser(query)
        play_random_sound(sound_folder)  
    elif "ютуби" in command:
        query = command.replace("ищи в ютуби", "").strip()
        search_in_youtube(query)
        play_random_sound(sound_folder)  
    # auto accept counter-strike 2
    elif command in ["стоп видео", "Stop video", "поставь видео на паузу"]:
        programs = []
        programs.append(r"C:\Users\NekaAlimovv\Desktop\Создающейся проэкты\AKIMA_beta\Application\youtube-function\pause-video.exe")
        open_programs(programs)  
    elif command in ["Следующий видео", "следующий видео", "next video", "next видео"]:
        programs = []
        programs.append(r"C:\Users\NekaAlimovv\Desktop\Создающейся проэкты\AKIMA_beta\Application\youtube-function\next video.exe")
        open_programs(programs)  
    elif command in ["Преведущий видео", "преведущий видео", "last video", "last видео"]:
        programs = []
        programs.append(r"C:\Users\NekaAlimovv\Desktop\Создающейся проэкты\AKIMA_beta\Application\youtube-function\last.exe")
        open_programs(programs)
    elif command in ["5 сек вперёд", "пять сек вперёд"]:
        programs = []
        programs.append(r"C:\Users\NekaAlimovv\Desktop\Создающейся проэкты\AKIMA_beta\Application\youtube-function\10right.exe")
        open_programs(programs)
    elif command in ["5 сек назад", "пять сек назад", "5 sec left", "five sec left"]:
        programs = []
        programs.append(r"C:\Users\NekaAlimovv\Desktop\Создающейся проэкты\AKIMA_beta\Application\youtube-function\10left.exe")
        open_programs(programs)
    elif "выключи компьютер" in command:
        os.system("shutdown /s /t 1")
    elif "спящий режим" in command:
        ctypes.windll.PowrProf.SetSuspendState(0, 1, 0)
    elif "перезагрузка" in command:
        os.system("shutdown /r /t 1")
    elif command in ["выход", "сменить пользователя", "блокировка"]:
        os.system("shutdown /l")
    elif command in ["выключись", "я устал", "Заверши работу", "Уйди", "Заткнись"]:
        # Проигрываем звук при выключении
        play_shutdown_sound()
        time.sleep(1)
        break
    elif command in["шутка","скажи шутку","joke", "Tell a joke","Скажи шутку", "Joke"]:
     play_joke_sound()
    if command.startswith("ищи музыку"):
        query = command.replace("ищи музыку", "").strip()
        video_url = search_video(query)
        play_video(video_url)
        play_random_sound(sound_folder)
    elif command in ["Прими игру", "прими игру", "Accept game", "accept game" ]:
        programs = []
        programs.append(r"C:\Users\NekaAlimovv\Desktop\Создающейся проэкты\AKIMA_beta\Application\cs2\autoaccept.exe")
        open_programs(programs)
    elif command in ["Сделай скриншот", "сделай скриншот", "Сделай скрин", "сделай скрин"]:
        take_screenshot(save_path)
        play_random_sound(sound_folder)
